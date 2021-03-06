"""Test cases for the command line interface."""
from typer.testing import CliRunner

from pypi_count.command_line_interface import cli

cli_runner = CliRunner()


def test_main_class():
    """Test case to see if class argument is correct."""
    class_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", "--class-definitions"])
    assert class_result.exit_code == 0
    assert "class definitions" in class_result.stdout

def test_while_loops():
    """Test case to see if class argument is correct."""
    while_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", "--while-loops"])
    assert while_result.exit_code == 0
    assert "while loop" in while_result.stdout

def test_for_loops():
    """Test case to see if class argument is correct."""
    for_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", "--for-loops"])
    assert for_result.exit_code == 0
    assert "for loop" in for_result.stdout

def test_main_imports():
    """Test case to see if import argument is correct."""
    import_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", "--import-statements"])
    assert import_result.exit_code == 0
    assert "import statements" in import_result.stdout


def test_main_comment():
    """Test case to see if comment argument is correct."""
    comment_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", "--comments"])
    assert comment_result.exit_code == 0
    assert "comments" in comment_result.stdout


def test_main_function_def():
    """Test case to see if function definition argument is correct."""
    function_def_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                                  "--function-definitions"])
    assert function_def_result.exit_code == 0
    assert "function definitions" in function_def_result.stdout


def test_main_function_without_docstrings():
    """Test case to see if function without docstrings argument is correct."""
    func_wo_docstr_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                                    "--function-without-docstrings"])
    assert func_wo_docstr_result.exit_code == 0
    assert "functions w/o docstrings" in func_wo_docstr_result.stdout


def test_main_function_with_docstrings():
    """Test case to see if function without docstrings argument is correct."""
    func_w_docstr_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                                   "--function-with-docstrings"])
    assert func_w_docstr_result.exit_code == 0
    assert "functions with docstrings" in func_w_docstr_result.stdout


def test_main_class_without_docstrings():
    """Test case to see if class without docstrings argument is correct."""
    class_wo_docstr_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                                     "--class-without-docstrings"])
    assert class_wo_docstr_result.exit_code == 0
    assert "classes w/o docstrings" in class_wo_docstr_result.stdout

def test_main_class_with_docstrings():
    """Test case to see if class with docstrings argument is correct."""
    class_w_docstr_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                                    "--class-with-docstrings"])
    assert class_w_docstr_result.exit_code == 0
    assert "classes with docstrings" in class_w_docstr_result.stdout

def test_if_statements():
    """Test case to see if 'if statements' argument is correct."""
    if_state = cli_runner.invoke(cli, ["tests/input/sample_file.py", "--if-statements"])
    assert if_state.exit_code == 0
    assert "if statements" in if_state.stdout

def test_function_parameters():
    """Test case to see if function finds the parameters."""
    function_parameter_result = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                                    "--function-parameters", "test_saying_two"])
    assert function_parameter_result.exit_code == 0
    assert "parameters in functions" in function_parameter_result.stdout

def test_count_assignment_statements():
    """Test case to see if 'assignment statements' argument is correct."""
    assign_state = cli_runner.invoke(cli, ["tests/input/sample_file.py", \
                                       "--assignment-statements"])
    assert assign_state.exit_code == 0
    assert "assignment statements" in assign_state.stdout

def testing_valid_file():
    """Test case for a non-valid file exception."""
    nonvalid_file = cli_runner.invoke(cli, ["test/input/text.txt", \
                                            "--class-definitions"])
    assert nonvalid_file.exit_code == 0
    assert "Please input a valid file!" in nonvalid_file.stdout
