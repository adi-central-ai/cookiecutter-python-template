# cookiecutter-python-template

Cookiecutter template configured with the following:

- poetry
- pytest
- ruff
- pydantic
- fastapi
- mypy
- bandit
- pre-commit
- jupyterlab (optional)
- CLI (optional)

## Install cookiecutter

```bash
python3 -m pip install --user cookiecutter
```

Templates can be directly cloned from Github using:

```bash
cookiecutter https://github.com/adi-central-ai/cookiecutter-python-template.git
```

The templates will be stored in the folder:

```bash
~/.cookiecutters/cookiecutter-python-template
```

After that, the template will be available locally and a project can be created:

```bash
cookiecutter cookiecutter-python-template/
```

### Configuration

After the cookiecutter command and template, the cli will ask several question for setting up the project.

### Post configuration

After the configuration steps a folder with the python development project will be created (project_folder), with all the configurations.
It is a ready to use poetry project...
