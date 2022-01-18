"""This module tests the hello.say_hello module."""

import pytest

from hello import say_hello


@pytest.mark.parametrize(
    "name,expected",
    [
        ("World", "Hello, World!\n"),
        ("Maria", "Hello, Maria!\n"),
        ("Saejin", "Hello, Saejin!\n"),
    ],
)
def test_greet(capsys, name, expected):
    """Check that greet() prints the correct message."""
    say_hello.greet(name)
    captured = capsys.readouterr()
    assert captured.out == expected
