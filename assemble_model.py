#!/usr/bin/env python3
"""Verify and join the ordered assets from this project's GitHub Release."""

import argparse
import hashlib
import json
from pathlib import Path

CHUNK = 8 * 1024 * 1024


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parts-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    manifest = json.loads((Path(__file__).parent / "SHA256SUMS.json").read_text(encoding="utf-8"))
    output = args.output.resolve()
    if output.exists():
        parser.error(f"Output already exists: {output}")
    parts_dir = args.parts_dir.resolve()
    parts = manifest["parts"]
    for part in parts:
        path = (parts_dir / part["name"]).resolve()
        if path.parent != parts_dir or not path.is_file():
            parser.error(f"Missing or invalid part: {part['name']}")
        if path.stat().st_size != part["bytes"]:
            parser.error(f"Wrong size: {part['name']}")

    output.parent.mkdir(parents=True, exist_ok=True)
    final_hash = hashlib.sha256()
    total = 0
    try:
        with output.open("xb") as dst:
            for part in parts:
                path = parts_dir / part["name"]
                part_hash = hashlib.sha256()
                with path.open("rb") as src:
                    while data := src.read(CHUNK):
                        part_hash.update(data)
                        final_hash.update(data)
                        dst.write(data)
                        total += len(data)
                if part_hash.hexdigest() != part["sha256"]:
                    raise ValueError(f"SHA-256 mismatch: {part['name']}")
                print(f"Verified {part['name']}")
        if total != manifest["model"]["bytes"]:
            raise ValueError("Reconstructed file size mismatch")
        if final_hash.hexdigest() != manifest["model"]["sha256"]:
            raise ValueError("Reconstructed model SHA-256 mismatch")
    except Exception:
        output.unlink(missing_ok=True)
        raise
    print(f"Verified model: {output}")
    print(f"SHA-256: {final_hash.hexdigest()}")


if __name__ == "__main__":
    main()
