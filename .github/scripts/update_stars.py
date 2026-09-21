#!/usr/bin/env python3
"""Refresh star counts embedded in the profile README files.

Each count lives between markers like:
    (<!--stars:alphaloop-->20<!--/stars--> stars)

The script finds every such marker, looks up the repo's current star count via
the GitHub API, and formats it the way GitHub displays it on a repo page:
compact "k" notation with one decimal above 1,000, and the exact number below.
Everything else in the file is left untouched.
"""

import json
import math
import os
import re
import sys
import urllib.request

OWNER = "realnaka"
FILES = ["README.md", "README.zh-CN.md"]
MARKER = re.compile(r"(<!--stars:([\w.\-]+)-->)(.*?)(<!--/stars-->)")
TOKEN = os.environ.get("GITHUB_TOKEN")


def format_count(n: int) -> str:
    # Match GitHub's own display: exact below 1,000, otherwise compact "k"
    # notation with one decimal, half-up rounding, trailing ".0" dropped.
    if n < 1000:
        return str(n)
    thousands = math.floor(n / 100 + 0.5) / 10
    label = f"{thousands:.1f}".rstrip("0").rstrip(".")
    return f"{label}k"


def fetch_stars(repo: str) -> int:
    url = f"https://api.github.com/repos/{OWNER}/{repo}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)["stargazers_count"]


def main() -> None:
    cache: dict[str, str] = {}
    changed = False

    for path in FILES:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()

        def replace(match: "re.Match[str]") -> str:
            slug = match.group(2)
            if slug not in cache:
                cache[slug] = format_count(fetch_stars(slug))
                print(f"{slug}: {cache[slug]}")
            return match.group(1) + cache[slug] + match.group(4)

        updated = MARKER.sub(replace, text)
        if updated != text:
            changed = True
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(updated)
            print(f"updated {path}")
        else:
            print(f"unchanged {path}")

    if not changed:
        print("no star-count changes")


if __name__ == "__main__":
    sys.exit(main())

