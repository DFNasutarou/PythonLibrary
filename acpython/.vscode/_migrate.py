"""
One-shot migration script for python.code-snippets.

Steps:
1. Load existing python.code-snippets
2. Apply rename map (key/prefix unification + typo fix)
3. Apply description fixes (dedup _old suffixes, etc.)
4. Split into 10 category files (.vscode/NN-category.code-snippets)
5. Remove original python.code-snippets
"""
import json
import os
import sys
from pathlib import Path

VSCODE_DIR = Path(__file__).parent
SRC = VSCODE_DIR / "python.code-snippets"

# old_key -> (new_key, new_prefix). new_prefix = new_key if same.
# Only listed entries are renamed; the rest keep key == prefix.
RENAME = {
    "unionFind":               ("union",          "union"),
    "convolve":                ("convolve_ll",    "convolve_ll"),
    "gridMan":                 ("grid",           "grid"),
    "Inverse":                 ("inv",            "inv"),
    "maxFlow":                 ("maxflow",        "maxflow"),
    "segment_tree":            ("seg",            "seg"),
    "sorted":                  ("sort",           "sort"),
    "tree64":                  ("tree64",         "tree64"),  # only prefix case fix
    "bunkatu":                 ("bunkatu",        "bunkatu"),  # only prefix case fix
    "unionFindPersistentPart": ("union_persist",  "union_persist"),
    # typos
    "dinamic_segtree":         ("dynamic_segtree","dynamic_segtree"),
    "squarespilit":            ("squaresplit",    "squaresplit"),
    "unionFindPotensial":      ("union_potential","union_potential"),
}

# Description overrides (clarify duplicates / fix vague ones)
DESC = {
    "lazyseg":           "遅延評価セグメント木 (自前実装)",
    "lazysegold":        "遅延評価セグメント木 (旧版・参考)",
    "lazysegacl":        "遅延評価セグメント木 (ACL 移植版)",
    "seg":               "セグメント木 (汎用 op/e 渡し)",
    "segment_tree_old":  "セグメント木 (旧版・参考)",
    "tree":              "木構造 (一般)",
    "tree_old":          "木構造 (旧版・参考)",
    "prime":             "素数列挙・素因数分解",
    "primeold":          "素数列挙 (旧版・参考)",
    "graph":             "グラフアルゴリズム (有向/重み対応)",
    "graphUndirected":   "無向グラフアルゴリズム (旧版・参考)",
    "Sample":            "[内部用テンプレ] 新規スニペット追加用ひな型",
    "list":              "1行を int リストに",
    "listfor":           "N 行を int リストの 2D に",
    "saiki":             "再帰上限の引き上げ",
    "abc":               "アルファベット定数",
}

# key -> category. Categories define output files.
CAT = {
    # 01-basic
    "input": "01-basic", "list": "01-basic", "listfor": "01-basic",
    "queue": "01-basic", "saiki": "01-basic", "abc": "01-basic",
    "sort": "01-basic", "deque": "01-basic", "itertools": "01-basic",
    "heapq": "01-basic", "query": "01-basic",

    # 02-data-structure
    "avl": "02-data-structure", "BIT": "02-data-structure",
    "lazyseg": "02-data-structure", "union": "02-data-structure",
    "seg": "02-data-structure", "multiset": "02-data-structure",
    "linkedlist": "02-data-structure", "trie": "02-data-structure",
    "union_potential": "02-data-structure", "BinaryTrie": "02-data-structure",
    "sortedSet": "02-data-structure", "rangeList": "02-data-structure",
    "union_persist": "02-data-structure", "dynamic_segtree": "02-data-structure",
    "packed2dlist": "02-data-structure", "map": "02-data-structure",
    "cartesianTree": "02-data-structure", "wavelet": "02-data-structure",

    # 03-graph
    "dijkstra": "03-graph", "kruskal": "03-graph", "maxflow": "03-graph",
    "mincost": "03-graph", "scc": "03-graph", "tree": "03-graph",
    "tree64": "03-graph", "bfs": "03-graph", "dag": "03-graph",
    "matching": "03-graph", "particalgraph": "03-graph", "warflo": "03-graph",
    "graph": "03-graph",

    # 04-string
    "rori": "04-string", "string": "04-string", "eertree": "04-string",
    "hensyuKyori": "04-string", "suffixarray": "04-string", "zalg": "04-string",

    # 05-math
    "adm": "05-math", "comb": "05-math", "convmod": "05-math",
    "convolve_ll": "05-math", "divhoujo": "05-math", "divisor": "05-math",
    "gyoretu": "05-math", "hakidasi": "05-math", "inv": "05-math",
    "kika": "05-math", "math": "05-math", "period": "05-math",
    "prime": "05-math", "totu": "05-math", "touhi": "05-math",
    "tousa": "05-math", "gensikon": "05-math", "convolution": "05-math",
    "radix_convert": "05-math", "kyori": "05-math", "Packer": "05-math",

    # 06-dp
    "treedp": "06-dp", "dfa": "06-dp", "nfa": "06-dp", "LIS": "06-dp",
    "slopetrick": "06-dp",

    # 07-range
    "CHT": "07-range", "mo": "07-range", "rangeaffine": "07-range",
    "imos2d": "07-range", "squaresplit": "07-range",

    # 08-misc-algo
    "bitall": "08-misc-algo", "grid": "08-misc-algo", "nibutan": "08-misc-algo",
    "tentou": "08-misc-algo", "twosat": "08-misc-algo", "way12": "08-misc-algo",
    "ragu": "08-misc-algo", "bunkatu": "08-misc-algo", "ushi": "08-misc-algo",
    "hakidasi2": "08-misc-algo",

    # 09-archive
    "graphUndirected": "09-archive", "lazysegold": "09-archive",
    "lazysegacl": "09-archive", "segment_tree_old": "09-archive",
    "tree_old": "09-archive", "primeold": "09-archive",

    # 99-template
    "Sample": "99-template",
}


def main(dry_run: bool):
    with SRC.open(encoding="utf-8") as f:
        data = json.load(f)

    # Apply rename + description fix
    new = {}
    for old_key, entry in data.items():
        if old_key in RENAME:
            new_key, new_prefix = RENAME[old_key]
            entry["prefix"] = new_prefix
        else:
            new_key = old_key
            # Force key == prefix where prefix is ASCII-only and differs only by case
            if entry.get("prefix") != old_key and entry.get("prefix", "").lower() == old_key.lower():
                entry["prefix"] = old_key

        # Lookup description override using the *new* key OR the *old* key
        # (since DESC is keyed by either, depending on whether we renamed).
        desc_key = new_key if new_key in DESC else old_key
        if desc_key in DESC:
            entry["description"] = DESC[desc_key]

        if new_key in new:
            print(f"[ERROR] duplicate key after rename: {new_key}", file=sys.stderr)
            sys.exit(1)
        new[new_key] = entry

    # Verify every key has a category
    missing = [k for k in new if k not in CAT]
    if missing:
        print(f"[ERROR] no category assigned: {missing}", file=sys.stderr)
        sys.exit(1)

    # Group by category
    buckets = {}
    for k, entry in new.items():
        buckets.setdefault(CAT[k], {})[k] = entry

    # Show plan
    print(f"Total entries: {len(new)}")
    for cat in sorted(buckets):
        print(f"  {cat}.code-snippets: {len(buckets[cat])} entries")

    # Diff: renamed keys
    print("\nRenamed (old -> new key/prefix):")
    for old, (new_k, new_p) in RENAME.items():
        print(f"  {old:<26} -> {new_k:<20} prefix={new_p}")

    if dry_run:
        print("\n[dry-run] no files written.")
        return

    # Write category files
    for cat, entries in buckets.items():
        out = VSCODE_DIR / f"{cat}.code-snippets"
        with out.open("w", encoding="utf-8", newline="\n") as f:
            json.dump(entries, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"  wrote {out.name} ({len(entries)} entries)")

    # Remove original
    SRC.unlink()
    print(f"  removed {SRC.name}")


if __name__ == "__main__":
    main(dry_run="--apply" not in sys.argv)
