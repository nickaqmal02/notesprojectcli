import click
from datetime import datetime
import json

# this click command decorator use
@click.command()
# this argument can be past to our created method
@click.argument("title")
@click.option("--version", type=int, default=1)
@click.option("--content", prompt=True, help='Content of the note')
@click.option("--tags", help="comma seperated list of tag")
# now we can pass all of that created argument into our method
def create(title: str, content: str, tags:str) -> None:
    """ function: create a new note"""
    notes_directory = "~/.notes"
    note_name = f"{title}.txt"
    if (notes_directory / note_name).exists():
        click.echo(f"Note with title '{title}' already exists")
        exit(1)

    note_data = {
        "content": content,
        "tags": tags.split(",") if tags else [],
        "created_at": datetime.now().isoformat(),
    }
    with open(notes_directory / note_name, "a+") as file:
        json.dump(note_data, file)

    click.echo(f"Note '{title}' created.")

    # but what does click.echo does ??
    # it just like logger.info or print(f"") same but just optimizing the click framework
    # and also how do we attach all of these commands into our main.py ?? the solution is 
    # to attach it as group
    #

