"""Version test for {{ cookiecutter.namespace + '-' + cookiecutter.module_name if cookiecutter.namespace else cookiecutter.module_name }}."""
import pytest

@pytest.mark.skip(reason="No version test yet.")
def test_version() -> None:
    """Check that all the version tags are in sync."""

    raise NotImplementedError("Test not implemented yet.")
