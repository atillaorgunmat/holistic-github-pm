import os
import re
import datetime

# Open GitHub Actions step summary file
with open(os.getenv("GITHUB_STEP_SUMMARY"), "a") as step_summary:
    today = datetime.date.today()
    step_summary.write(f"# 📊 Daily Summary — {today}\n\n")

    # Read tasks
    with open("Tasks.md") as f:
        text = f.read()

    open_count  = len(re.findall(r"\[Open\]", text))
    done_count  = len(re.findall(r"\[Done\]", text))
    blocked_count = len(re.findall(r"\[Blocked\]", text))

    step_summary.write("## Task Status Counts\n")
    step_summary.write(f"- **Open Tasks:** {open_count}\n")
    step_summary.write(f"- **Done Tasks:** {done_count}\n")
    step_summary.write(f"- **Blocked Tasks:** {blocked_count}\n\n")

    step_summary.write("_Generated automatically._\n")

