#!/usr/bin/env python3
"""Upload heavy Print PDF and .originals.pdf camera scan assets to GitHub Releases."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess


def resolve_pipeline_root(cli_root: str | None = None) -> Path:
    lib_root = Path(__file__).resolve().parents[1]
    if cli_root:
        return Path(cli_root).expanduser().resolve()
    env_root = os.environ.get("AKSHARA_PIPELINE_ROOT") or os.environ.get("AKSHARA_NEW_ROOT")
    if env_root:
        return Path(env_root).expanduser().resolve()
    return (lib_root.parent / "akshara_new").resolve()


def main() -> None:
    parser = argparse.ArgumentParser(description="Upload Print & Originals PDFs to GitHub Releases")
    parser.add_argument("--book", help="Single book_id to upload")
    parser.add_argument("--pipeline-root", help="Path to akshara_new repository")
    parser.add_argument("--repo", default="bebhuvan/akshara-library", help="Target GitHub repo")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without executing")
    args = parser.parse_args()

    lib_root = Path(__file__).resolve().parents[1]
    pipeline_root = resolve_pipeline_root(args.pipeline_root)
    catalog = json.loads((lib_root / "catalog.json").read_text(encoding="utf-8"))
    books = [b for b in catalog["books"] if not args.book or b["book_id"] == args.book]

    for b in books:
        bid = b["book_id"]
        col = b["collection"]
        ed_dir = pipeline_root / "library" / col / bid
        print_pdf = ed_dir / "print" / f"{bid}.pdf"
        orig_pdf = pipeline_root / "sources" / f"{bid}.originals.pdf"
        assets = [str(p) for p in (print_pdf, orig_pdf) if p.is_file()]
        if not assets:
            print(f"SKIP {bid}: no heavy PDF assets found under {pipeline_root}")
            continue
        tag = f"edition-{bid}"
        title = f"{b['title']} ({b.get('publication_year') or 'PD'})"
        notes = (
            f"Compiled PDF and de-blotted Archive.org camera scan backup for `{bid}`.\n\n"
            f"- Tier: `{b['edition_tier']}` ({b['rubric_score']:.1f}/100)\n"
            f"- Online Reader: https://akshara.ink/books/{bid}/"
        )
        exists = subprocess.run(
            ["gh", "release", "view", tag, "--repo", args.repo],
            capture_output=True,
        ).returncode == 0
        cmd = (
            ["gh", "release", "upload", tag, "--repo", args.repo, "--clobber", *assets]
            if exists
            else ["gh", "release", "create", tag, "--repo", args.repo, "--title", title, "--notes", notes, *assets]
        )
        print(f"[{'UPLOAD' if exists else 'CREATE'}] {tag}: {len(assets)} file(s)")
        if not args.dry_run:
            subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
