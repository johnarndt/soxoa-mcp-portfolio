#!/usr/bin/env python3
"""Build platform packages from the portable skill catalog; never contact a service."""
import argparse
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def zip_tree(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(source).as_posix())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--portal-template", type=Path)
    args = parser.parse_args()
    catalog = json.loads((ROOT / "skills-catalog.json").read_text())
    products = json.loads((ROOT / "products.json").read_text())
    marketplace_path = ROOT / ".claude-plugin/marketplace.json"
    marketplace = json.loads(marketplace_path.read_text())
    receipts = []
    for product in catalog["products"]:
        slug = product["slug"]
        version = product["version"]
        plugin = ROOT / "plugins" / slug
        skills_dir = plugin / "skills"
        if skills_dir.exists():
            shutil.rmtree(skills_dir)
        skills_dir.mkdir()
        for skill in product["skills"]:
            shutil.copytree(ROOT / "skills" / skill["name"], skills_dir / skill["name"])
        for rel in [".codex-plugin/plugin.json", ".claude-plugin/plugin.json", "openclaw.plugin.json"]:
            path = plugin / rel
            data = json.loads(path.read_text())
            data.update(version=version, description=product["description"])
            if isinstance(data.get("mcpServers"), dict):
                for server in data["mcpServers"].values():
                    if slug in {"mentionedon", "intakra"}:
                        server["auth"] = "oauth"
            write_json(path, data)
        for row in marketplace["plugins"]:
            if row["name"] == slug:
                row.update(version=version, description=product["description"])
        for row in products["products"]:
            if row["slug"] == slug:
                row.update(description=product["description"], authentication=product["authentication"],
                           packageVersion=version, skills=[s["name"] for s in product["skills"]],
                           defaultPrompts=product["defaultPrompts"], workflowBounds=product["bounds"])
        lines = [f"# {product['name']} MCP integration", "", product["description"], "",
                 "## Connection", "", f"Endpoint: {product['endpoint']}", "",
                 "Transport: Streamable HTTP (client config type `http`).", "",
                 product["authDescription"], "",
                 "Use the client's normal remote-MCP authorization flow. Credentials stay in the client's secure credential store; do not paste them into chat.", "",
                 "## Included workflows", ""]
        lines += [f"- [{s['name']}](skills/{s['name']}/SKILL.md): {s['description']}" for s in product["skills"]]
        lines += ["", "## Example requests", ""] + [f"- {p}" for p in product["defaultPrompts"]]
        lines += ["", "## Workflow boundaries", "", product["bounds"], "",
                  "Connection does not authorize unrelated writes, paid work, purchases, or communication. Follow the user's actual request and the current server schema. Recover uncertain jobs and orders before starting another.", "",
                  f"Documentation: {product['documentation']}", "",
                  "These MIT-licensed files contain public configuration and skill instructions. Hosted services retain their terms and implementation rights.", ""]
        (plugin / "README.md").write_text("\n".join(lines))
        archive = args.output / "public" / f"{slug}-{version}.zip"
        zip_tree(plugin, archive)
        receipt = {"product": slug, "version": version, "skills": len(product["skills"]),
                   "publicArchive": str(archive.resolve()), "publicSha256": hashlib.sha256(archive.read_bytes()).hexdigest()}
        if args.portal_template:
            source = args.portal_template / slug
            target = args.output / "openai" / slug
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(source, target)
            shutil.rmtree(target / "skills")
            shutil.copytree(skills_dir, target / "skills")
            manifest_path = target / "plugin.json"
            manifest = json.loads(manifest_path.read_text())
            manifest.update(version=version, description=product["longDescription"])
            ext = manifest.setdefault("extensions", {}).setdefault("com.openai", {})
            interface = ext.setdefault("interface", {})
            interface.update(longDescription=product["longDescription"], defaultPrompt=product["defaultPrompts"])
            ext.setdefault("publication", {})["release_notes"] = f"{version}: Updated portable workflow skills and current account, consent and recovery guidance. Package validation is separate from connected account acceptance and directory review."
            write_json(manifest_path, manifest)
            portal_archive = args.output / "openai" / f"{slug}-{version}.zip"
            zip_tree(target, portal_archive)
            receipt.update(openaiArchive=str(portal_archive.resolve()),
                           openaiSha256=hashlib.sha256(portal_archive.read_bytes()).hexdigest())
        receipts.append(receipt)
    write_json(marketplace_path, marketplace)
    write_json(ROOT / "products.json", products)
    write_json(args.output / "build-receipt.json", {"skills": sum(r["skills"] for r in receipts), "products": receipts,
               "status": "built_not_submitted", "networkRequests": 0})
    print(json.dumps({"products": len(receipts), "skills": sum(r["skills"] for r in receipts), "output": str(args.output.resolve())}))


if __name__ == "__main__":
    main()
