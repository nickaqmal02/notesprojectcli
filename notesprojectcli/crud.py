import click
from datetime import datetime
import json
from pathlib import Path

NOTES_DIR = Path(__file__).resolve().parent / "allnotes"

@click.command()
@click.argument("title")
@click.option("--version", type=int, default=1)
@click.option("--content", prompt=True, help='Content of the note')
@click.option("--tags", help="comma seperated list of tag")
def create(title: str, content: str, tags:str, version: int) -> None:
    """ function: create a new note"""
    NOTES_DIR.mkdir(parents=True, exist_ok=True)

    note_path = NOTES_DIR / f"{title}.txt"

    if note_path.exists():
        raise click.ClickException(f"Note with tile '{title}' already exists")

    note_data = {
        "content": content,
        "tags": tags.split(",") if tags else [],
        "created_at": datetime.now().isoformat(),
        "version": version,
    }

    with open(note_path, "w") as f:
        json.dump(note_data, f, indent=2)

    click.echo(f"Note '{title}' created.")

    # but what does click.echo does ??
    # it just like logger.info or print(f"") same but just optimizing the click framework
    # and also how do we attach all of these commands into our main.py ?? the solution is 
    # to attach it as group
    #

