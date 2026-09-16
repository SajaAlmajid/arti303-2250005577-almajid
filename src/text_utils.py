"""Utilities for cleaning and standardizing text strings."""

def clean_name(raw):
    """Clean whitespace and convert name to title case."""
    collapsed = " ".join(raw.split())
    return collapsed.title()
