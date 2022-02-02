#!/usr/bin/env python -W ignore::DeprecationWarning

"""The command line interface for the PyCount program."""
from pathlib import Path
from rich.console import Console

import typer

from pypi_count.py_counter import PyPiCount

cli = typer.Typer()

console = Console()


@cli.command()
def main(  # pylint: disable=R0913
    input_file: Path = typer.Option(...),
    class_def: bool = typer.Option(False, "--class_def"),
    import_statements: bool = typer.Option(False, "--import_statements"),
    comment: bool = typer.Option(False, "--comment"),
    function_def: bool = typer.Option(False, "--function_def"),
    if_statements: bool = typer.Option(False, "--if_statements"),
    function_without_docstrings: bool = typer.Option(False, "--function_without_docstrings"),
    function_with_docstrings: bool = typer.Option(False, "--function_with_docstrings"),
    class_with_docstrings: bool = typer.Option(False, "--class_with_docstrings"),
    class_without_docstrings: bool = typer.Option(False, "--class_without_docstrings"),
    find_parameters: bool = typer.Option(False, "--find_parameters"),
    assignment_statements: bool = typer.Option(False, "--assignment_statements"),

):
    """Main method to display the different options."""
    pycount = PyPiCount(input_file)
    if class_def:
        console.print("\n# of class definitions: " + str(pycount.count_class_definitions()))

    if import_statements:
        console.print("\n# of import statements: " + str(pycount.count_import_statements()))

    if comment:
        console.print("\n# of comments: " + str(pycount.count_comments()))

    if function_def:
        console.print("\n# of function definitions: " + str(pycount.count_function_definitions()))

    if function_without_docstrings:
        console.print("\n# of functions w/o docstrings: " + str(pycount.count_functions_without_docstring())) # pylint: disable=C0301

    if function_with_docstrings:
        console.print("\n# of functions with docstrings: " + str(pycount.count_functions_with_docstring())) # pylint: disable=C0301

    if class_without_docstrings:
        console.print("\n# of classes w/o docstrings: " + str(pycount.count_classes_without_docstring())) # pylint: disable=C0301

    if class_with_docstrings:
        console.print("\n# of functions with docstrings: " + str(pycount.count_classes_with_docstring())) # pylint: disable=C0301

    if if_statements:
        console.print("\n# of if statements: " + str(pycount.count_if_statements())) # pylint: disable=C0301

    if find_parameters:
        console.print("\n# of parameters in functions: " + str(pycount.count_function_parameters())) # pylint: disable=C0301

    if assignment_statements:
        console.print("\n of assignment statements: " + str(pycount.count_assignment_statements())) # pylint: disable=c0301
