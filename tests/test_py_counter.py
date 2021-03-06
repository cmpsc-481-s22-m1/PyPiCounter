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
    expected_comments = 17
    assert test_pycount.count_comments() == expected_comments

def test_count_while_loops():
    """Test case for counting the while loops."""
    expected_while = 0
    assert test_pycount.count_while_loops() == expected_while

def test_import_statements():
    """Test case for counting import statements."""
    expected_imports = 2
    assert test_pycount.count_import_statements() == expected_imports

def test_count_for_loops():
    """Test case for counting the for loops."""
    expected_for = 1
    assert test_pycount.count_for_loops() == expected_for

def test_count_if_statements():
    """Test case for counting the if statements."""
    expected_if = 2
    assert test_pycount.count_if_statements() == expected_if

def test_count_functions_without_docstrings():
    """Test case for counting the number of functions that do not have docstrings."""
    expected_function_dst = 5
    assert test_pycount.count_functions_without_docstrings() == expected_function_dst

def test_count_functions_with_docstrings():
    """Test case for counting the number of functions that do not have docstrings."""
    expected_function_dst_2 = 4
    assert test_pycount.count_functions_with_docstrings() == expected_function_dst_2

def test_count_classes_without_docstrings():
    """Test case for counting the number of Classes that do not have docstrings."""
    expected_classes_dst = 1
    assert test_pycount.count_classes_without_docstrings() == expected_classes_dst

def test_count_classes_with_docstrings():
    """Test case for counting the number of Classes that do not have docstrings."""
    expected_classes_dst_2 = 1
    assert test_pycount.count_classes_with_docstrings() == expected_classes_dst_2

def test_function_parameters():
    """Test case for counting the parameters"""
    expected_parameters = 1
    assert test_pycount.count_function_parameters("test_saying_two") == expected_parameters

def test_count_assignment_statements(): #pylint: disable=C0116
    """Test case for counting assignment statements"""
    expected_assignment_statements = 11
    assert test_pycount.count_assignment_statements() == expected_assignment_statements

def test_count_augmented_assignment_statements():
    """Test case for counting augmented assignement statements."""
    exp_aug_assignment_statements = 1
    assert test_pycount.count_augmented_assignment_statements() == exp_aug_assignment_statements
