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


