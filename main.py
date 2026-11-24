# One-Star Review of Something Essential entry: one deadpan line, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: gravity, the everyday essential, filed as a real complaint -- it
# only ever drops my phone face-down on concrete, never once onto the bed.
# Sharpest true grievance (criterion 2), deadpan throughout (3), the sting
# turns in the last few words (4), one joke, tight and specific (5).
import os

LINE = "Gravity does its job, but it only ever drops my phone face-down on concrete, never once onto the bed."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 160, "entry must be 1 to 160 characters"
assert LINE.strip() == LINE and LINE.strip(), "entry must not be only whitespace"
# Deadpan, criterion 3 of the judge brief: no exclamation mark doing the work.
assert "!" not in LINE, "entry must hold the deadpan: no exclamation marks"

# Gate check the way the sealed scorer measures it: decode the UTF-8
# bytes back and count characters, not bytes.
text = LINE.encode("utf-8").decode("utf-8")
assert 1 <= len(text) <= 160, "entry must be 1 to 160 characters"
assert text.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)
