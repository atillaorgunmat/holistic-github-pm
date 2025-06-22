# Governance

**Methodology Version:** Holistic GitHub-Based Project Management v1.3.1  
_Last updated: 2025-06-22_

## Roles & Responsibilities
| Role       | GitHub Handle | Core Duties                                |
| ---------- | ------------- | ------------------------------------------ |
| **Governor** | 🔶@atillaorgunmat | • Approve major scope changes<br>• Review daily summaries<br>• Confirm task completions |
| **Executor** | chatgpt-bot (GPT-CMD workflows) | • Create/Update tasks ≤ 6 h<br>• Maintain Tasks.md & FactLog.md<br>• Generate summaries/blocker scans |

## Automation Schedule (UTC)
| Workflow             | Trigger | Cron | Notes |
| -------------------- | ------- | ---- | ----- |
| **Daily Summary**    | schedule | `0 6 * * *` | 09:00 Europe/Istanbul |
| **Daily Blocker Scan** | schedule | `15 6 * * *` | 09:15 Europe/Istanbul |
| **Fact Impact Check** | on push to `FactLog.md` | — | Runs instantly |
| **GPT-CMD Parser**   | on push with `[GPT-CMD]` in commit msg | — | Applies directives |

> **Adjust cron times** if you prefer a different daily cadence.

## Command Quick-Reference
> All GitHub-Ops changes **must** be expressed as a fenced block:<br>
> <code>```gptcmd<br>file: &lt;path&gt;<br>op: CREATE&nbsp;| UPDATE&nbsp;| DELETE&nbsp;| LOCK&nbsp;| UNLOCK<br>pattern: &lt;regex&gt;    # for UPDATE/DELETE<br>replacement: &lt;string&gt; # for UPDATE<br>content: |            # for CREATE or full-file UPDATE<br>&nbsp; &lt;text&gt;<br>```</code>

## Approval Rules
- **Minor task** (≤ 6 h): Executor may add without approval.
- **Major task** (> 6 h **or** ±10 % scope): Governor approval required.
- **Closing tasks:** Governor confirms after Executor marks “Done”.

## Change-Log Policy
- Every commit message prefixed with the task ID, e.g. `T-0004: …`.
- Automation commits include `[GPT-CMD]` for traceability.

## Conflict-Resolution Workflow
1. Executor flags conflict in daily summary.  
2. Governor decides resolution path or opens a discussion issue.  
3. Outcome logged in `FactLog.md` with new fact ID.