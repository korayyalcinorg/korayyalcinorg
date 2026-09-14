#!/usr/bin/env python3
"""Update the Latest from KorayYalcin.org section in README.md.

The script first tries common RSS endpoints and falls back to parsing the
Research & Publications landing page. It uses only Python's standard library.
"""

from __future__ import annotations

import html
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

README = Path("README.md")
START = "<!-- LATEST:START -->"
END = "<!-- LATEST:END -->"
FEEDS = [
    "https://www.korayyalcin.org/yayinlar-arastirmalar/feed/",
    "https://www.korayyalcin.org/feed/",
]
LANDING = "https://www.korayyalcin.org/yayinlar-arastirmalar/"
MAX_ITEMS = 6
USER_AGENT = "korayyalcinorg-github-profile-updater/1.0"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=25) as response:
        return response.read()


def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def from_rss(data: bytes):
    root = ET.fromstring(data)
    items = []

    # RSS 2.0
    for item in root.findall(".//item"):
        title = clean_text(item.findtext("title") or "")
        link = (item.findtext("link") or "").strip()
        if title and link:
            items.append((title, link))

    # Atom fallback
    if not items:
        ns = {"a": "http://www.w3.org/2005/Atom"}
        for entry in root.findall(".//a:entry", ns):
            title = clean_text(entry.findtext("a:title", default="", namespaces=ns))
            link_el = entry.find("a:link", ns)
            link = link_el.get("href", "").strip() if link_el is not None else ""
            if title and link:
                items.append((title, link))

    return items


def from_landing(data: bytes):
    text = data.decode("utf-8", errors="ignore")
    pattern = re.compile(
        r'<a[^>]+href=["\'](https?://(?:www\.)?korayyalcin\.org/yayinlar-arastirmalar/[^"\'#?]+/)["\'][^>]*>(.*?)</a>',
        re.I | re.S,
    )
    items = []
    seen = set()
    for link, body in pattern.findall(text):
        title = clean_text(body)
        if len(title) < 24:
            continue
        if any(part in link for part in ("/kategori/", "/tur/")):
            continue
        key = (title.lower(), link.rstrip("/"))
        if key in seen:
            continue
        seen.add(key)
        items.append((title, link))
    return items


def get_items():
    for feed in FEEDS:
        try:
            items = from_rss(fetch(feed))
            if items:
                return items[:MAX_ITEMS]
        except Exception as exc:
            print(f"Feed failed: {feed}: {exc}", file=sys.stderr)

    try:
        items = from_landing(fetch(LANDING))
        if items:
            return items[:MAX_ITEMS]
    except Exception as exc:
        print(f"Landing fallback failed: {exc}", file=sys.stderr)

    return []


def main():
    readme = README.read_text(encoding="utf-8")
    if START not in readme or END not in readme:
        raise SystemExit("Latest content markers are missing from README.md")

    items = get_items()
    if not items:
        print("No items found; README left unchanged.")
        return

    lines = [START, ""]
    for title, link in items:
        safe_title = title.replace("[", "\\[").replace("]", "\\]")
        lines.append(f"- [{safe_title}]({link})")
    lines.extend(["", END])
    block = "\n".join(lines)

    updated = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        block,
        readme,
        flags=re.S,
    )
    if updated != readme:
        README.write_text(updated, encoding="utf-8")
        print(f"Updated README with {len(items)} latest items.")
    else:
        print("README already up to date.")


if __name__ == "__main__":
    main()
