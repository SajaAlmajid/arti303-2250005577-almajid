<<<<<<< HEAD
"""Utilities for cleaning and standardizing text strings."""

def clean_name(raw):
    """Clean whitespace and convert name to title case."""
=======
"""Helpers for cleaning up messy text fields."""


def clean_name(raw):
    """Strip, collapse inner whitespace, and title-case a name."""
>>>>>>> upstream/main
    collapsed = " ".join(raw.split())
    return collapsed.title()
