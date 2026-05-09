"""
Sanity-check every snippet body as Python source.

For each entry:
  1. Join body lines into a Python source string
  2. Substitute snippet placeholders ($1, ${1:default}, $0) with valid tokens
  3. compile() the result
  4. Report any SyntaxError / IndentationError / TabError

Notes:
  - We only check syntactic validity, not import/name resolution.
  - Snippets are typically class/func *definitions*, so a successful compile
    means the body parses; whether it runs depends on caller-supplied args.
"""
import ast
import glob
import json
import re
from pathlib import Path

VSCODE_DIR = Path(__file__).parent
PLACEHOLDER_RE = re.compile(r"\$\{(\d+):([^{}]*)\}|\$(\d+)")


def desugar(src: str) -> str:
    """Replace VSCode snippet placeholders with valid Python tokens."""
    def repl(m: re.Match) -> str:
        if m.group(1) is not None:
            num, default = m.group(1), m.group(2)
            return default if default else f"_p{num}"
        num = m.group(3)
        # $0 is the final cursor sentinel — strip it.
        return "" if num == "0" else f"_p{num}"
    return PLACEHOLDER_RE.sub(repl, src)


def check_file(path: Path) -> list[tuple[str, str]]:
    """Returns list of (key, error_msg) for entries that failed."""
    errs: list[tuple[str, str]] = []
    with path.open(encoding="utf-8") as f:
        d = json.load(f)
    for key, entry in d.items():
        body = entry.get("body", [])
        src = "\n".join(body) if isinstance(body, list) else body
        src = desugar(src)
        try:
            compile(src, f"{path.name}:{key}", "exec")
        except (SyntaxError, IndentationError, TabError, ValueError) as e:
            line = getattr(e, "lineno", "?")
            offset = getattr(e, "offset", "?")
            text = getattr(e, "text", "") or ""
            errs.append((key, f"{type(e).__name__}: {e.msg} (line {line}, col {offset}) :: {text.rstrip()}"))
    return errs


def main():
    total = 0
    failed_total = 0
    by_file: dict[str, list[tuple[str, str]]] = {}
    for path_str in sorted(glob.glob(str(VSCODE_DIR / "*.code-snippets"))):
        path = Path(path_str)
        with path.open(encoding="utf-8") as f:
            d = json.load(f)
        total += len(d)
        errs = check_file(path)
        failed_total += len(errs)
        if errs:
            by_file[path.name] = errs

    print(f"Checked: {total} snippets")
    print(f"Failed:  {failed_total}")
    print()
    if not by_file:
        print("All snippets parsed successfully.")
        return
    for name, errs in by_file.items():
        print(f"## {name} ({len(errs)} failed)")
        for key, msg in errs:
            print(f"  - {key}: {msg}")
        print()


if __name__ == "__main__":
    main()
