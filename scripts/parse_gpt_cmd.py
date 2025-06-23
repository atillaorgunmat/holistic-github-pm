#!/usr/bin/env python3
import sys
import json
import re

def apply_directive(directive):
    file_path = directive.get("file")
    op = directive.get("op")
    if not file_path or not op:
        print("Directive missing 'file' or 'op'", file=sys.stderr)
        sys.exit(1)

    if op == "CREATE":
        content = directive.get("content", "")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    elif op == "UPDATE":
        pattern = directive.get("pattern")
        replacement = directive.get("replacement", "")
        if not pattern:
            print("UPDATE directive missing 'pattern'", file=sys.stderr)
            sys.exit(1)
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
        new_text = re.sub(pattern, replacement, text, flags=re.MULTILINE)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_text)

    elif op == "DELETE":
        pattern = directive.get("pattern")
        if not pattern:
            print("DELETE directive missing 'pattern'", file=sys.stderr)
            sys.exit(1)
        lines = []
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if not re.search(pattern, line):
                    lines.append(line)
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)

    else:
        print(f"Unknown operation: {op}", file=sys.stderr)
        sys.exit(1)

def main():
    input_data = sys.stdin.read()
    if not input_data:
        print("No input provided. Please pipe JSON directives to this script.", file=sys.stderr)
        sys.exit(1)
    try:
        directives = json.loads(input_data)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)
    # Ensure we have a list of directives
    if isinstance(directives, dict):
        directives = [directives]
    for directive in directives:
        apply_directive(directive)
    print("All directives applied successfully.")

if __name__ == "__main__":
    main()
