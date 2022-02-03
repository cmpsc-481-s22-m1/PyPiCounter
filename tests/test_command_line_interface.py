"""Test cases for the command line interface."""
from typer.testing import CliRunner

from pypi_count.command_line_interface import cli

cli_runner = CliRunner()


def test_main_class():
    """Test case to see if class argument is correct."""
    class_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", "--class-definitions"])
    assert class_result.exit_code == 0
    assert "2" in class_result.stdout


def test_main_imports():
    """Test case to see if import argument is correct."""
    import_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", "--import-statements"])
    assert import_result.exit_code == 0
    assert "2" in import_result.stdout


def test_main_comment():
    """Test case to see if comment argument is correct."""
    comment_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", "--comments"])
    assert comment_result.exit_code == 0
    assert "14" in comment_result.stdout


def test_main_function_def():
    """Test case to see if function definition argument is correct."""
    function_def_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                                  "--function-definitions"])
    assert function_def_result.exit_code == 0
    assert "8" in function_def_result.stdout


def test_main_function_without_docstrings():
    """Test case to see if function without docstrings argument is correct."""
    func_wo_docstr_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                                    "--function-without-docstrings"])
    assert func_wo_docstr_result.exit_code == 0
    assert "4" in func_wo_docstr_result.stdout


def test_main_function_with_docstrings():
    """Test case to see if function without docstrings argument is correct."""
    func_w_docstr_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                                   "--function-with-docstrings"])
    assert func_w_docstr_result.exit_code == 0
    assert "4" in func_w_docstr_result.stdout


def test_main_class_without_docstrings():
    """Test case to see if class without docstrings argument is correct."""
    class_wo_docstr_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                                     "--class-without-docstrings"])
    assert class_wo_docstr_result.exit_code == 0
    assert "1" in class_wo_docstr_result.stdout

def test_main_class_with_docstrings():
    """Test case to see if class with docstrings argument is correct."""
    class_w_docstr_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                                    "--class-with-docstrings"])
    assert class_w_docstr_result.exit_code == 0
    assert "1" in class_w_docstr_result.stdout

def test_if_statements():
    """Test case to see if 'if statements' argument is correct."""
    if_state = cli_runner.invoke(cli, ["tests/input/sample_file.py", "--if-statements"])
    assert if_state.exit_code == 0
    assert "1" in if_state.stdout

def test_main_parameters():
    """Test case to see if function finds the parameters."""
    find_parameter_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                                    "--find-parameters"])
    assert find_parameter_result.exit_code == 0
    assert "0" in find_parameter_result.stdout

def test_count_assignment_statements():
    """Test case to see if 'assignment statements' argument is correct."""
    if_state = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                       "--assignment-statements"])
    assert if_state.exit_code == 0
    assert "9" in if_state.stdout
