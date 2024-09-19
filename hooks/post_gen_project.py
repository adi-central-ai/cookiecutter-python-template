import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(path):
    os.rmdir(os.path.join(PROJECT_DIRECTORY, path))

def make_dir(path):
    os.mkdir(os.path.join(PROJECT_DIRECTORY, path))

if __name__ == "__main__":
    if "{{ cookiecutter.use_jupyterlab }}" != "y":
        remove_dir("notebooks")

    if "{{ cookiecutter.use_jupyterlab }}" != "n":
        make_dir("notebooks")

    if len("{{ cookiecutter.namespace }}") !=0:
        make_dir("{{cookiecutter.namespace}}")

    if "{{ cookiecutter.module_name }}" != 0:
        if len("{{ cookiecutter.namespace }}") != 0:
            make_dir("{{cookiecutter.namespace}}/{{cookiecutter.module_name}}")
        else:
            make_dir("{{cookiecutter.module_name}}")
