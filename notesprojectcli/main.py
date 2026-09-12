import json
from pathlib import Path
import click
import crud

# but how do we know exactly what does all decorator does ?? 
# the answer is ? : just browse it all in git click/core.py
#
#
@click.group()
def cli() -> None:
    print("hello world")


@cli.add_command(crud.create)


