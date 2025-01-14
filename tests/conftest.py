import pytest

def pytest_configure(config: pytest.Config):
    """Set pytest configuration values at runtime."""
    config.addinivalue_line(
        "markers", "term: tests of symbolic terms"
    )
    config.addinivalue_line(
        "markers", "expression: tests of symbolic expressions"
    )

