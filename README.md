# notesprojectcli

A tiny command-line notes app. Create, list, update, and delete notes — all from your terminal.

## Requirements

- Python 3.14+
- [Poetry](https://python-poetry.org/)

## Install

```bash
git clone <your-repo-url>
cd notesprojectcli
poetry install
```

## usage

```bash
# Create a note
poetry run notesprojectcli create shopping --content "milk, eggs" --tags "home,urgent"

# List all notes
poetry run notesprojectcli list

# Show a single note in detail
poetry run notesprojectcli show 1

# Update a note
poetry run notesprojectcli update 1 --content "milk, eggs, bread"

# Delete a note
poetry run notesprojectcli delete 2

```

## where all notes will be saved ??

```bash
~/.notesprojectcli/notes.json
```

## development section

```bash

# Enter the virtual environment
eval $(poetry env activate)

# Run type checks
poetry run mypy notesprojectcli/

# Run tests
poetry run pytest

# Leave the environment
deactivate

```

## project structure

```bash
notesprojectcli/
├── pyproject.toml            # project config + dependencies
├── poetry.lock               # pinned dependency versions
├── README.md
├── notesprojectcli/          # the package
│   ├── __init__.py
│   ├── main.py               # CLI layer (Click commands)
│   └── crud.py               # data layer (load/save/update/delete)
└── tests/
    └── test_crud.py
```

## design
```txt
The code is split into two layers:

main.py — the CLI. Handles user input, output, and Click decorators.

crud.py — the logic. Handles reading/writing notes and business rules.

main.py never touches JSON or file paths. crud.py never imports click. This separation makes the logic testable without invoking the CLI.


```

*this project was fully-type annotated and checked with mypy*

```bash
poetry run mypy notesprojectcli/

# expected
Succes: no issues found in 3 source files

```
