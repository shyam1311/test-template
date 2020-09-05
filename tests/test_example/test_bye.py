import pytest

from test_template.example import bye


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Jeanette", "Goodbye Jeanette!"),
        ("Raven", "Goodbye Raven!"),
        ("Maxine", "Goodbye Maxine!"),
        ("Matteo", "Goodbye Matteo!"),
        ("Destinee", "Goodbye Destinee!"),
        ("Alden", "Goodbye Alden!"),
        ("Mariah", "Goodbye Mariah!"),
        ("Anika", "Goodbye Anika!"),
        ("Isabella", "Goodbye Isabella!"),
    ],
)
def test_bye(name, expected):
    """Example test with parametrization."""
    assert bye(name) == expected
