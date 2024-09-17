import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(path):
    os.rmdir(os.path.join(PROJECT_DIRECTORY, path))

if __name__ == "__main__":
    if "{{ cookiecutter.use_jupyterlab }}" != "y":
        remove_dir("notebooks")

    if "{{ cookiecutter.use_precommit }}" != "y":
        remove_file(".pre-commit-config.yaml")

    if "{{ cookiecutter.use_precommit }}" == "y":
        os.system('echo "Initializing Git for pre-commit... \n"')
        os.system("git init --initial-branch=main")
        os.system('echo "Installing pre-commit hooks... \n"')
        os.system("pre-commit install")
        os.system('echo "Running pre-commit hooks... \n"')
