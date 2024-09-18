import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(path):
    os.rmdir(os.path.join(PROJECT_DIRECTORY, path))

if __name__ == "__main__":
    if "{{ cookiecutter.use_jupyterlab }}" != "y":
        remove_dir("notebooks")