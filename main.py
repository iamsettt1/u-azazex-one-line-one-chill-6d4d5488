"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt. The line is fixed text, composed once and stored
here as a constant, so every run produces byte-identical output.
"""

import os

LINE = "Every Sunday my mother calls from the number we disconnected the week she died."


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, exactly one sentence.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.count(".") == 1 and LINE.endswith("."), "line must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
