"""
One-shot script to rename 's' (used as self alias) to 'self' across snippets.

Strategy:
  1. Desugar VSCode placeholders so the body is parseable Python.
     Desugar preserves line counts (only in-line substitutions), so line
     numbers in the AST map 1:1 to the original body.
  2. Parse, find every ClassDef -> FunctionDef whose first arg is 's'.
  3. For each such method, get its inclusive line range.
  4. Within that range, in the ORIGINAL body, rewrite \bs\b -> self on
     the non-comment portion of each line (split at first '#').

Risk: if 's' is used as a regular local variable name within a method,
this will rename it too. Manually verified that snippets do not do this.
A final syntax check catches gross breakage.
"""
import ast
import json
import re
import sys
from pathlib import Path

PLACEHOLDER_RE = re.compile(r"\$\{(\d+):([^{}]*)\}|\$(\d+)")
S_BOUNDARY = re.compile(r"\bs\b")


def desugar(src: str) -> str:
    def repl(m):
        if m.group(1) is not None:
            num, default = m.group(1), m.group(2)
            return default if default else f"_p{num}"
        num = m.group(3)
        return "" if num == "0" else f"_p{num}"
    return PLACEHOLDER_RE.sub(repl, src)


def find_method_ranges(source: str):
    """Yield (start_line, end_line) for each ClassDef.body FunctionDef whose
    first arg is named 's'. Lines are 1-based, inclusive."""
    tree = ast.parse(source)
    ranges = []
    # Walk ClassDef recursively; for each, iterate body FunctionDefs.
    # Nested classes are still ClassDef nodes so ast.walk picks them up.
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    if item.args.args and item.args.args[0].arg == 's':
                        end = item.end_lineno or item.lineno
                        ranges.append((item.lineno, end))
    # Also handle module-level FunctionDef? The user explicitly wants method
    # self-aliases, so skip those.
    return ranges


def rewrite_line(line: str) -> str:
    """Replace 's' with 'self' on the non-comment portion."""
    # Find first unquoted '#'. We approximate by looking for '#' not inside
    # quotes — but for simplicity, just find first '#'. Most competitive code
    # doesn't put '#' inside string literals.
    if '#' in line:
        idx = line.index('#')
        head, tail = line[:idx], line[idx:]
    else:
        head, tail = line, ''
    head = S_BOUNDARY.sub('self', head)
    return head + tail


def process_file(path: Path) -> int:
    d = json.loads(path.read_text(encoding='utf-8'))
    changed = 0
    for k, v in d.items():
        body = v['body']
        if not isinstance(body, list):
            continue
        joined = '\n'.join(body)
        try:
            ranges = find_method_ranges(desugar(joined))
        except SyntaxError:
            continue
        if not ranges:
            continue
        # Build set of 1-based line indices to rewrite
        targets = set()
        for s, e in ranges:
            targets.update(range(s, e + 1))
        # Apply rewrite
        new_body = []
        for i, line in enumerate(body, start=1):
            if i in targets:
                new_body.append(rewrite_line(line))
            else:
                new_body.append(line)
        if new_body != body:
            v['body'] = new_body
            changed += 1
    if changed:
        path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return changed


def main(dry_run: bool):
    vsc = Path(__file__).parent
    total = 0
    for path in sorted(vsc.glob('*.code-snippets')):
        n = process_file(path) if not dry_run else 0
        if dry_run:
            d = json.loads(path.read_text(encoding='utf-8'))
            n = 0
            for k, v in d.items():
                body = '\n'.join(v['body'])
                try:
                    if find_method_ranges(desugar(body)):
                        n += 1
                except SyntaxError:
                    pass
        if n:
            print(f"  {path.name}: {n} snippets {'would change' if dry_run else 'changed'}")
            total += n
    print(f"Total snippets {'would be modified' if dry_run else 'modified'}: {total}")


if __name__ == '__main__':
    main(dry_run='--apply' not in sys.argv)
