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
- CLI

## Install cookiecutter

```bash
python3 -m pip install --user cookiecutter
```

You can install it on Mac using the following command in Terminal:

```bash
brew install cookiecutter
```

## Configuration using Github

Templates can be directly cloned from Github using:

```bash
cookiecutter https://github.com/adi-central-ai/cookiecutter-python-template.git --checkout dev
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

```bash
[1/11] full_name (Central AI): Name of the developer
[2/11] email (Central.ai@analog.com): E-mail
[3/11] namespace (): Modules namespace. If not empty (default), the module will be located in the namespace/module_name folder.
[4/11] module_name (aiproject_python): Module name
[5/11] python_version (3.12): Python version. Default is set python 3.12
[6/11] project_folder : Root folder of the python module development (repository)
[7/11] short_description (Python project of the Central AI team.): Description for the repository
[8/11] version (0.1.0): Version of the cookiecutter template.
[9/11] use_jupyterlab (n): If y then a notebooks directory is created for jupyter notebooks
[10/11] ci_use_cache (n): If y then use ci cache
[11/11] create_dev_builds (y): if y then dev builds will be created and uploaded to github's repository.
```

### Post configuration

After the configuration steps a folder with the python development project will be created (project_folder), with all the configurations.
It is a ready to use poetry project...
