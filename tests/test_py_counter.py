"""Test cases for py_counter method."""

import libcst.matchers as m
import libcst as cst

from src.py_counter import PyCount

test_pycount = PyCount()


def test_count_class_defintions():
    """Test case for counting the class definitions."""
    expected_class = 1
    assert test_pycount.count_class_definitions() == expected_class

def test_count_comments():
    """Test case for counting the class definitions."""
    expected_comments = 7
    assert test_pycount.count_comments() == expected_comments
