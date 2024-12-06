import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(path):
    os.rmdir(os.path.join(PROJECT_DIRECTORY, path))


def make_dir(path):
    os.mkdir(os.path.join(PROJECT_DIRECTORY, path))


def create_github_workflows():
    github_dir = os.path.join(PROJECT_DIRECTORY, ".github")
    workflows_dir = os.path.join(github_dir, "workflows")

    # Create .github directory if it doesn't exist
    if not os.path.exists(github_dir):
        os.makedirs(github_dir)

    # Create workflows directory if it doesn't exist
    if not os.path.exists(workflows_dir):
        os.makedirs(workflows_dir)

    # Create python-test.yml file
    python_test_yml = os.path.join(workflows_dir, "python-test.yml")
    with open(python_test_yml, "w") as f:
        f.write(
            """
name: Python test

on:
  push:
    branches: "**"
  pull_request:
    branches: "**"

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version:
        - 3.11
        - 3.12

    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install --upgrade poetry setuptools anybadge wheel
          poetry install
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      - name: Lint
        run: poetry run invoke lint
      - name: Test
        run: poetry run invoke test

      - name: Upload coverage report
        if: github.ref == 'refs/heads/dev' || github.ref == 'refs/heads/main'
        uses: actions/upload-artifact@v4
        with:
          name: coverage-report-${{ github.run_number }}-${{ matrix.python-version }}
          path: coverage.html

      - name: Upload test report
        if: github.ref == 'refs/heads/dev' || github.ref == 'refs/heads/main'
        uses: actions/upload-artifact@v4
        with:
          name: test-report-${{ github.run_number }}-${{ matrix.python-version }}
          path: unit-test-report.html"""
        )


if __name__ == "__main__":
    create_github_workflows()

if __name__ == "__main__":
    create_github_workflows()
    if "{{ cookiecutter.use_jupyterlab }}" != "y":
        remove_dir("notebooks")

    if "{{ cookiecutter.use_jupyterlab }}" != "n":
        make_dir("notebooks")

    if len("{{ cookiecutter.namespace }}") != 0:
        make_dir("{{cookiecutter.namespace}}")
        shutil.move(
            "{{cookiecutter.module_name}}",
            "{{cookiecutter.namespace}}/{{cookiecutter.module_name}}",
        )
