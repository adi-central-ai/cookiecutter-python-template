"""
Python project of the Central AI.
"""

from importlib.metadata import version
from pkgutil import extend_path
from typing import Any

__author__ = "{{ cookiecutter.full_name }} <{{ cookiecutter.email }}>"

try:
    # This works only, if the package is installed.
    __version__ = version("{{cookiecutter.project_folder}}")
except BaseException:
    # Version set to default, if the repository is used as a non-installed package.
    __version__ = "0.1.0"


__path__ = extend_path(__path__, __name__)

__all__: list[Any] = []
