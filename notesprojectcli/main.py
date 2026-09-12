import json
from pathlib import Path
import click
from notesprojectcli.crud import create

# but how do we know exactly what does all decorator does ?? 
# the answer is ? : just browse it all in git click/core.py
#
#
@click.group()
def cli() -> None:
    pass

cli.add_command(create)



