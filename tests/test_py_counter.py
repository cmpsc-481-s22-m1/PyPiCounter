"""Test cases for py_counter method."""

from pypi_count.py_counter import PyPiCount


FILE = "tests/input/sample_file.py"
test_pycount = PyPiCount(FILE)

def test_count_class_defintions():
    """Test case for counting the class definitions."""
    expected_class = 2
    assert test_pycount.count_class_definitions() == expected_class


def test_count_comments():
    """Test case for counting the class definitions."""
    expected_comments = 14
    assert test_pycount.count_comments() == expected_comments

def test_count_while():
    """Test case for counting the while loops."""
    expected_while = 0
    assert test_pycount.count_while() == expected_while

def test_import_statements():
    """Test case for counting import statements."""
    expected_imports = 2
    assert test_pycount.count_import_statements() == expected_imports

def test_count_for():
    """Test case for counting the for loops."""
    expected_for = 0
    assert test_pycount.count_for() == expected_for

def test_count_if_statements():
    """Test case for counting the if statements."""
    expected_if = 1
    assert test_pycount.count_if_statements() == expected_if

def test_count_functions_without_docstrings():
    """Test case for counting the number of functions that do not have docstrings."""
    expected_function_dst = 3
    assert test_pycount.count_functions_without_docstring() == expected_function_dst

def test_count_functions_with_docstrings():
    """Test case for counting the number of functions that do not have docstrings."""
    expected_function_dst_2 = 3
    assert test_pycount.count_functions_with_docstring() == expected_function_dst_2

def test_count_classes_without_docstrings():
    """Test case for counting the number of Classes that do not have docstrings."""
    expected_classes_dst = 1
    assert test_pycount.count_classes_without_docstring() == expected_classes_dst

def test_count_classes_with_docstrings():
    """Test case for counting the number of Classes that do not have docstrings."""
    expected_classes_dst_2 = 1
    assert test_pycount.count_classes_with_docstring() == expected_classes_dst_2

def test_find_parameters():
    """Test case for counting the parameters"""
    expected_parameters = 0
    assert test_pycount.count_function_parameters() == expected_parameters

def test_count_assignment_statements():
    """Test case for counting assignement statements."""
    expected_assignment_statements = 2
    assert test_pycount.count_assignment_statements() == expected_assignment_statements
