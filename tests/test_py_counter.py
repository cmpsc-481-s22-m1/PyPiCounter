"""Test cases for py_counter method."""

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


def test_import_statements():
    """Test case for counting the import statements."""
    expected_imports = 2
    assert test_pycount.count_import_statements() == expected_imports


def test_count_if_statements():
    """Test case for counting the if statements."""
    expected_if = 0
    assert test_pycount.count_if_statements() == expected_if

def test_count_functions_without_docstrings():
    """Test case for counting the number of functions that do not have docstrings."""
    expected_function_without_docstring_count = 0
    assert test_pycount.count_functions_without_docstring() == expected_function_without_docstring_count
