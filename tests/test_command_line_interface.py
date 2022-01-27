"""Test cases for the command line interface."""
from typer.testing import CliRunner

from command_line_interface import cli


cli_runner = CliRunner()


def test_main_class():
    """Test case to see if class argument is correct."""
    class_result = cli_runner.invoke(cli, ["--input-file", "tests/input/sample_file.py", "--class_def"]) # pylint: disable=C0301
    assert class_result.exit_code == 0
    assert "2" in class_result.stdout


def test_main_imports():
    """Test case to see if import argument is correct."""
    import_result = cli_runner.invoke(cli, ["--input-file", "tests/input/sample_file.py", "--import_statements"]) # pylint: disable=C0301
    assert import_result.exit_code == 0
    assert "2" in import_result.stdout


def test_main_comment():
    """Test case to see if comment argument is correct."""
    comment_result = cli_runner.invoke(cli, ["--input-file", "tests/input/sample_file.py", "--comment"]) # pylint: disable=C0301
    assert comment_result.exit_code == 0
    assert "14" in comment_result.stdout


def test_main_function_def():
    """Test case to see if function definition argument is correct."""
    function_def_result = cli_runner.invoke(cli, ["--input-file", "tests/input/sample_file.py", "--function_def"]) # pylint: disable=C0301
    assert function_def_result.exit_code == 0
    assert "6" in function_def_result.stdout


def test_main_function_without_docstrings():
    """Test case to see if function without docstrings argument is correct."""
    func_wo_docstr_result = cli_runner.invoke(cli, ["--input-file", "tests/input/sample_file.py", "--function_without_docstrings"]) # pylint: disable=C0301
    assert func_wo_docstr_result.exit_code == 0
    assert "None" in func_wo_docstr_result.stdout


def test_main_class_without_docstrings():
    """Test case to see if class without docstrings argument is correct."""
    class_wo_docstr_result = cli_runner.invoke(cli, ["--input-file", "tests/input/sample_file.py", "--class_without_docstrings"]) # pylint: disable=C0301
    assert class_wo_docstr_result.exit_code == 0
    assert "None" in class_wo_docstr_result.stdout

def test_if_statements():
    """Test case to see if 'if statements' argument is correct."""
    if_state = cli_runner.invoke(cli, ["--input-file", "tests/input/sample_file.py", "--if_statements"]) # pylint: disable=C0301
    assert if_state.exit_code == 0
    assert "1" in if_state.stdout
