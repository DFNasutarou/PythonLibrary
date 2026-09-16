"""
Safe delete helper for this workspace.

Guards:
  1. Target must resolve (realpath) inside the workspace root (acpython/).
     Anything outside -> refused (blocks path traversal / symlink escape).
  2. Directories are refused unless --recursive is explicitly passed.
  3. A fixed set of protected paths (this script, .git, .vscode config
     files) are refused even with --recursive.
  4. Non-existent paths are reported and skipped (not an error for the
     whole batch).

Usage:
  python .vscode/_safe_delete.py <path> [<path> ...]
  python .vscode/_safe_delete.py --recursive <dir>
  python .vscode/_safe_delete.py --dry-run <path>
"""
import argparse
import shutil
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
PROTECTED = {
    Path(__file__).resolve(),
    WORKSPACE_ROOT / ".git",
    WORKSPACE_ROOT / ".vscode" / "settings.json",
    WORKSPACE_ROOT / ".vscode" / "tasks.json",
    WORKSPACE_ROOT / ".vscode" / "launch.json",
}


def resolve_target(raw: str) -> Path:
    p = Path(raw)
    if not p.is_absolute():
        p = WORKSPACE_ROOT / p
    return p.resolve()


def check_target(target: Path, recursive: bool) -> str | None:
    """Returns an error message, or None if the target is safe to delete."""
    try:
        target.relative_to(WORKSPACE_ROOT)
    except ValueError:
        return f"refused: outside workspace root ({WORKSPACE_ROOT})"
    if target == WORKSPACE_ROOT:
        return "refused: workspace root itself"
    if target in PROTECTED or any(target == p or p in target.parents for p in PROTECTED):
        return "refused: protected path"
    if not target.exists():
        return "skipped: does not exist"
    if target.is_dir() and not recursive:
        return "refused: is a directory (pass --recursive to allow)"
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="+", help="File/dir paths (relative to workspace root or absolute)")
    ap.add_argument("--recursive", action="store_true", help="Allow deleting directories")
    ap.add_argument("--dry-run", action="store_true", help="Only print what would happen")
    args = ap.parse_args()

    exit_code = 0
    for raw in args.paths:
        target = resolve_target(raw)
        reason = check_target(target, args.recursive)
        if reason is not None:
            print(f"[{reason}] {raw} -> {target}")
            if reason.startswith("refused"):
                exit_code = 1
            continue
        if args.dry_run:
            print(f"[dry-run] would delete: {target}")
            continue
        if target.is_dir():
            shutil.rmtree(target)
        else:
            target.unlink()
        print(f"[deleted] {target}")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
