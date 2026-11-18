"""Copy the bundled entry.png to the output directory.

The entry image lives next to this script. This program copies it byte for
byte to <output_dir>/entry.png, where <output_dir> comes from the
MAKEFUN_OUTPUT_DIR environment variable, or defaults to an "output"
directory under the current working directory. The source file is first
checked to be a real PNG (its 8 magic bytes must match the PNG signature);
anything else is rejected with a clear error instead of being copied. The
destination is written to a temporary file in the same directory first and
then renamed into place, so the result is byte-identical on every run.
"""

import os
import sys

SOURCE_NAME = "entry.png"

# The 8-byte signature every valid PNG file starts with.
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, SOURCE_NAME)

    with open(source_path, "rb") as source_file:
        data = source_file.read()

    if data[: len(PNG_SIGNATURE)] != PNG_SIGNATURE:
        print(
            "error: {} is not a valid PNG file "
            "(missing PNG magic bytes)".format(source_path),
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.getcwd(), "output"
    )
    os.makedirs(output_dir, exist_ok=True)
    destination_path = os.path.join(output_dir, SOURCE_NAME)

    temp_path = destination_path + ".tmp"
    with open(temp_path, "wb") as temp_file:
        temp_file.write(data)
        temp_file.flush()
        os.fsync(temp_file.fileno())
    os.replace(temp_path, destination_path)

    return 0


if __name__ == "__main__":
    sys.exit(main())
