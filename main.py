"""The Robot Pickup Line Championship — entry program.

Writes one robot pickup line to /output/entry.txt.

The line is a single line of at most 200 characters, in the voice of a
robot trying to charm someone. The joke grows out of being a machine:
a spam filter — the kind of thing a robot actually runs — doing the
complimenting by letting exactly one face through.
"""

import os

ENTRY_LINE = "I scanned ten thousand faces today \u2014 yours is the only one my spam filter let through."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> bool:
    """Return True only if the line passes the competition gate.

    The gate requires UTF-8 text of 1 to 200 characters that is not
    only whitespace, and a single line. The character count is taken
    over the decoded text, and the line must survive a UTF-8
    encode/decode round trip unchanged, so the file the grader reads
    is exactly the line validated here.
    """
    if not line or not line.strip():
        return False
    if len(line) > 200:
        return False
    if "\n" in line or "\r" in line:
        return False
    try:
        if line.encode("utf-8").decode("utf-8") != line:
            return False
    except UnicodeError:
        return False
    return True


def main() -> None:
    if not validate(ENTRY_LINE):
        raise ValueError("entry line fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
