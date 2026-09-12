## code snippets

```python

pipx install poetry

# then we need to setup the 
# wait before that confirm that we have installed our poetry successfully by "poetry --version"


```
```bash

mkdir -p ~/.zfunc

poetry completions zsh > ~/.zfunc/_poetry

echo 'fpath+=~/.zfunc' >> ~/.zshrc

echo 'autoload -Uz compinit && compinit' >> ~/.zshrc

source ~/.zshrc






poetry install

# to activate the project environment 
eval $(poetry env activate)


```

## learning about Path from pathlib

```python
from pathlib import Path

# this is very crucial lesson to learn
# 3 basics path that we need to actually know 

Path("~/.notes").expanduser() # /Users/apple/.notes
Path(__file__).resolve().parent / "notes"
# / "notes" here means that we will create dir to store our data
# without .parent() we will return file not the parent dir




```

## storing something in json using json approach 


