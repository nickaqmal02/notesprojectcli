# notesprojectcli

A tiny command-line notes app. Add notes, list them, delete them.


```bash
poetry install



eval $(poetry env activate)

deactivate


```

## Project Structure

notesprojectcli/
├── pyproject.toml            # project config + dependencies
├── poetry.lock               # pinned dependency versions
├── README.md
├── notesprojectcli/          # the package
│   ├── __init__.py
│   └── main.py               # CLI logic
└── tests/
    └── test_main.py

# Lisense
## MIT


### 💡 Adjust These Before Committing

- **Repo URL** — replace `<your-repo-url>` with the actual GitHub link (or remove the clone line if you haven't pushed yet).
- **Python version** — check your `pyproject.toml` for the actual required version (e.g. `^3.11` vs `^3.12`) and match it.
- **Command examples** — swap `notesprojectcli` for whatever you named the CLI entry point if you change it later.
- **License** — if you didn't pick MIT during `poetry init`, either add a `LICENSE` file or remove that section.

### 📝 What Makes This README "Simple but Real"

It has the four things every project README needs:

1. **What it is** — one sentence at the top
2. **How to install** — copy-pasteable commands
3. **How to use** — real examples, not just `--help`
4. **How to develop** — for future-you or a collaborator

Short enough to actually read, complete enough to actually follow. 🚀

