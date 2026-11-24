"""news-23 b50 front-page-dense: copy entry.png (1024x1024) to $MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only. Never writes next to itself: it writes only to MAKEFUN_OUTPUT_DIR,
so it also works from a read-only copy (with MAKEFUN_OUTPUT_DIR pointed elsewhere).
"""
import hashlib
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is empty", file=sys.stderr)
        return 1
    if os.path.abspath(out_dir) == HERE or os.path.abspath(out_dir).startswith(HERE + os.sep):
        print("MAKEFUN_OUTPUT_DIR must be outside the repo", file=sys.stderr)
        return 1
    if not os.path.isfile(SRC):
        print("source entry.png missing next to main.py", file=sys.stderr)
        return 1
    with open(SRC, "rb") as f:
        data = f.read()
    print("source entry.png: %d bytes" % len(data))
    if len(data) > 1024 * 1024:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("not a PNG", file=sys.stderr)
        return 1
    w, h, depth, ctype = struct.unpack(">IIBB", data[16:26])
    if (w, h) != (1024, 1024) or depth != 8 or ctype not in (2, 6):
        print("unexpected PNG header: %dx%d depth %d type %d" % (w, h, depth, ctype),
              file=sys.stderr)
        return 1
    if data[-12:] != b"\x00\x00\x00\x00IEND\xaeB`\x82":
        print("PNG IEND trailer malformed", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(dst, "wb") as f:
        f.write(data)
    with open(dst, "rb") as f:
        back = f.read()
    if back != data:
        print("output differs from source", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, %dx%d, sha256 %s)"
          % (dst, len(data), w, h, hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
