import json
from pathlib import Path
import click
from notesprojectcli import crud

# but how do we know exactly what does all decorator does ?? 
# the answer is ? : just browse it all in git click/core.py
#
#
@click.group()
def cli() -> None:
    """just a tiny notes cli"""
    pass

@cli.command()
@click.argument("name")
@click.option("--content", default="", type=str, help="Note content")
@click.option("--tags", default="", type=str, help="Comma-separated tags")
def create(name: str, content: str, tags: str) -> None:
    """Create a new note."""
    note = crud.create(name, content=content, tags=tags)
    click.echo(f"Created note: {note['name']}")


@cli.command(name="list")
def list_notes() -> None:
    """List all notes."""
    notes = crud.load_notes()
    if not notes:
        click.echo("No notes yet. Add one with: notesprojectcli create <name>")
        return

    for i, note in enumerate(notes, start=1):
        tags = ", ".join(note.get("tags", []))
        tags_part = f"  [{tags}]" if tags else ""
        click.echo(f"{i}. {note['name']}{tags_part}")
        if note.get("content"):
            click.echo(f"   {note['content']}")


@cli.command()
@click.argument("index", type=int)
@click.option("--name", default=None, type=str, help="New note name")
@click.option("--content", default=None, type=str, help="New content")
@click.option("--tags", default=None, type=str, help="New comma-separated tags")
def update(
    index: int,
    name: str | None,
    content: str | None,
    tags: str | None,
) -> None:
    """Update a note by its number."""
    if name is None and content is None and tags is None:
        click.echo("Nothing to update. Pass at least one of --name, --content, --tags.")
        return

    result = crud.update(index, name=name, content=content, tags=tags)
    if result is None:
        click.echo(f"No note #{index}.")
        return

    click.echo(f"Updated note #{index}: {result['name']}")


@cli.command()
@click.argument("index", type=int)
def delete(index: int) -> None:
    """Delete a note by its number."""
    removed = crud.delete(index)
    if removed is None:
        click.echo(f"No note #{index}.")
        return

    click.echo(f"Deleted: {removed['name']}")


@cli.command()
@click.argument("index", type=int)
def show(index: int) -> None:
    """Show a single note in detail."""
    note = crud.get(index)
    if note is None:
        click.echo(f"No note #{index}.")
        return

    click.echo(f"Name:    {note['name']}")
    click.echo(f"Content: {note.get('content', '')}")
    click.echo(f"Tags:    {', '.join(note.get('tags', [])) or '(none)'}")


def main() -> None:
    cli()


if __name__ == "__main__":
    main()


