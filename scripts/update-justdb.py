"""Update the cask from the latest published stable JustDB release."""
import hashlib
import json
import os
from pathlib import Path
import re
import urllib.request


def main():
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "justdb-homebrew-tap"}
    if token := os.environ.get("GH_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request("https://api.github.com/repos/codellyson/justdb/releases/latest", headers=headers)
    with urllib.request.urlopen(request, timeout=60) as response:
        release = json.load(response)
    if release["draft"] or release["prerelease"]:
        raise ValueError("Only stable published releases can update the cask")
    tag = release["tag_name"]
    if not re.fullmatch(r"v\d+\.\d+\.\d+", tag):
        raise ValueError(f"Unexpected release tag: {tag}")
    version = tag[1:]
    name = f"JustDB_{version}_universal.dmg"
    asset = next(a for a in release["assets"] if a["name"] == name and a["state"] == "uploaded")
    url = f"https://github.com/codellyson/justdb/releases/download/{tag}/{name}"
    if asset["browser_download_url"] != url:
        raise ValueError("Unexpected installer URL")
    path = Path(__file__).resolve().parents[1] / "Casks/justdb.rb"
    current = path.read_text()
    expected = asset.get("digest", "")
    old_version = re.search(r'^  version "([^"]+)"$', current, re.M).group(1)
    old_hash = re.search(r'^  sha256 "([a-f0-9]{64})"$', current, re.M).group(1)
    if tuple(map(int, version.split('.'))) < tuple(map(int, old_version.split('.'))):
        raise ValueError("Refusing to downgrade the cask")
    if old_version == version and expected == f"sha256:{old_hash}":
        print(f"JustDB {version} is current")
        return
    digest = hashlib.sha256()
    with urllib.request.urlopen(url, timeout=120) as response:
        while chunk := response.read(1024 * 1024):
            digest.update(chunk)
    checksum = digest.hexdigest()
    if expected and expected != f"sha256:{checksum}":
        raise ValueError("Installer checksum differs from GitHub asset digest")
    updated = re.sub(r'^  version "[^"]+"$', f'  version "{version}"', current, flags=re.M)
    updated = re.sub(r'^  sha256 "[a-f0-9]{64}"$', f'  sha256 "{checksum}"', updated, flags=re.M)
    path.write_text(updated)
    print(f"Verified JustDB {version}: {checksum}")


if __name__ == "__main__":
    main()
