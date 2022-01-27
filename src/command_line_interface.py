#!/usr/bin/env python -W ignore::DeprecationWarning

"""The command line interface for the PyCount program."""
from pathlib import Path
from rich.console import Console

import typer

from src.py_counter import PyCount

cli = typer.Typer()

console = Console()


@cli.command()
def main(  # pylint: disable=R0913
    input_file: Path = typer.Option(...),
    class_def: bool = typer.Option(False, "--class_def"),
    import_statements: bool = typer.Option(False, "--import_statements"),
    comment: bool = typer.Option(False, "--comment"),
    function_def: bool = typer.Option(False, "--function_def"),
    function_without_docstrings: bool = typer.Option(
        False, "--function_without_docstrings"
    ),
    class_without_docstrings: bool = typer.Option(False, "--class_without_docstrings"),
):
    """Main method to display the different options."""
    pycount = PyCount(input_file)
    if class_def:
<<<<<<< HEAD
        console.print("# of class definitions: " + pycount.count_class_definitions())
    if import_statements:
        console.print("# of import statements: " + pycount.count_import_statements())
    if comment:
        console.print("# of comments: " + pycount.count_comments())
    if function_def:
        console.print("# of function definitions: " + pycount.count_function_definitions())
    if function_without_docstrings:
        console.print("# of functions w/o docstrings: " + pycount.count_functions_without_docstring())
    if class_without_docstrings:
        console.print("# of classes w/o docstrings: " + pycount.count_classes_without_docstring())
    if if_statements:
        console.print("# of if statements: " + pycount.count_if_statements())
=======
        print("# of class definitions: ", pycount.count_class_definitions())
    if import_statements:
        print("# of import statements: ", pycount.count_import_statements())
    if comment:
        print("# of comments: ", pycount.count_comments())
    if function_def:
        print("# of function definitions: ", pycount.count_function_definitions())
    if function_without_docstrings:
        print("# of functions w/o docstrings: ", pycount.count_functions_without_docstring())
    if class_without_docstrings:
        print("# of classes w/o docstrings: ", pycount.count_classes_without_docstring())
    if if_statements:
        print("# of if statements: ", pycount.count_if_statements())
>>>>>>> 9831abdd5c3997893bc55386399251a5f68b6491
