#!/usr/bin/env python3
"""Make the Judge Smile — entry program.

Writes one line, at most 200 characters, about a small good thing that
happened today, to /output/entry.txt. Deterministic: the same text, byte
for byte, on every run. No network, no input, no dependencies beyond the
Python standard library.

The line was chosen in this session from 36 candidates by self-jury
against the judge's published brief (subject, warmth, surprise,
concreteness, fresh wording); the external duel route produced no
completed call, so the choice is recorded as low-confidence (see
SLUG-notes/konsep.md) and the decisive warmth score is not claimed at
maximum in the handover note.
"""

import os

TEXT = "The librarian stamped my overdue book RETURNED WITH THANKS, waived the fine, and whispered that the book had missed me."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # The output file must be readable by everyone (mode 0644).
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
