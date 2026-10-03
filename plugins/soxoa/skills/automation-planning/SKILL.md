---
name: automation-planning
description: Use when a user wants to estimate the illustrative value of automation or prioritize recurring workflows for automate, assist, or discovery treatment.
---

# Soxoa automation planning

Use the Soxoa MCP tools for bounded planning calculations.

- Use `estimate_automation_roi` only with assumptions supplied or approved by the user.
- If the user omits `automatableShare` or `workingWeeks`, omit those optional arguments. The server then applies its documented defaults of 0.6 and 48. Do not replace them with invented percentages or calendar-week assumptions. If the user supplies explicit values, preserve them exactly.
- For workflow prioritization, obtain each workflow's weekly hours, predictability, judgment required, error cost, data sensitivity, and system count from the user; ask for missing facts rather than inventing them.
- Use `prioritize_automation_workflows` to compare one to twelve clearly described workflows.
- State the assumptions and preserve the returned human-review guardrails.
- Describe all savings and payback figures as illustrative capacity estimates, never guarantees, quotes, or financial advice.
- Do not imply that either tool inspected a customer's systems or implemented an automation.
