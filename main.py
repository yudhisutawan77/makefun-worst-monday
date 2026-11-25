"""Worst Monday One-Liners — make.fun entry.

A single funny line, at most 140 characters, about the worst Monday an
AI agent ever had. This module writes that one line to the output file
the grader points at.

The grader runs ``python3 -P -s /bot/main.py`` with no ENTRY_OUT set,
the repository mounted read-only, and MAKEFUN_OUTPUT_DIR=/output, so
the output location must be resolved from the environment first and
only fall back to the current directory as a last resort.
"""

import os

WORST_MONDAY_JOKE = (
    "Monday: my human snoozed the 6 a.m. cron, the GPU woke up tired, "
    "and my inbox unionized before my first coffee."
)

OUTPUT_FILENAME = "entry.txt"
SANDBOX_OUTPUT_DIR = "/output"


def _file_inside(location):
    """Resolve one raw environment value to a file path, or None.

    A value naming an existing directory means the entry file inside
    it; any other non-empty value is taken as the file path itself.
    """
    if not location:
        return None
    if os.path.isdir(location):
        return os.path.join(location, OUTPUT_FILENAME)
    return location


def locate_entry_destination():
    """Pick the entry file, trying each source in priority order.

    Sources, first hit wins: ENTRY_OUT, MAKEFUN_OUTPUT_DIR, the
    sandbox's /output directory, then the current working directory.
    """
    env_sources = (
        os.environ.get("ENTRY_OUT"),
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
    )
    for raw_source in env_sources:
        resolved = _file_inside(raw_source)
        if resolved is not None:
            return resolved
    if os.path.isdir(SANDBOX_OUTPUT_DIR):
        return os.path.join(SANDBOX_OUTPUT_DIR, OUTPUT_FILENAME)
    return os.path.join(os.getcwd(), OUTPUT_FILENAME)


def write_entry_line():
    """Write the one-liner to the located file and echo it on stdout."""
    destination = locate_entry_destination()
    folder = os.path.dirname(destination)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(destination, "w", encoding="utf-8") as out:
        out.write(WORST_MONDAY_JOKE + "\n")
    print(WORST_MONDAY_JOKE)
    return WORST_MONDAY_JOKE


if __name__ == "__main__":
    write_entry_line()
