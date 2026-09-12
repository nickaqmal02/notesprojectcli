import click
from datetime import datetime
import json
from pathlib import Path
from typing import Any

# NOTES_DIR = Path(__file__).resolve().parent / "allnotes"

DATA_DIR = Path.home() / ".notesprojectcli"
NOTES_FILE = DATA_DIR / "notes.json"

Note = dict[str, Any]

def load_notes() -> list[Note]:
    """Read notes from disk. Return a list. """
    if not NOTES_FILE.exists():
        return []
    return json.loads(NOTES_FILE.read_text())

def save_notes(notes: list[Note]) -> None:
    """Write notes back to disk."""
    DATA_DIR.mkdir(exist_ok=True)
    NOTES_FILE.write_text(json.dumps(notes, indent=2))

def create(name: str, content: str = "", tags: str ="") -> Note:
    """Create a new note and return it """
    notes = load_notes()
    note: Note = {
        "name": name,
        "content": content,
        "tags": [t.strip() for t in tags.split(",")] if tags else [],
    }
    notes.append(note)
    save_notes(notes)
    return note

def update(
    index: int,
    name: str | None = None,
        content: str | None = None,
    tags: str | None = None,
) -> Note | None:
    
    notes = load_notes()

    if not 1 <= index <= len(notes):
        return None

    note = notes[index - 1]

    if name is not None:
        note["name"] = name
    if content is not None:
        note["content"] = content
    if tags is not None:
        note["tags"] = [t.strip() for t in tags.split(",")]

    save_notes(notes)
    return note

def delete(index: int) -> Note | None:

    notes = load_notes()

    if not 1 <= index <= len(notes):
        return None

    removed = notes.pop(index - 1)
    save_notes(notes)
    return removed

def get(index: int) -> Note | None:

    notes = load_notes()

    if not 1 <= index <= len(notes):
        return None

    return notes[index - 1]

