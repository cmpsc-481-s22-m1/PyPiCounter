#!/usr/bin/env python -W ignore::DeprecationWarning

"""The command line interface for the PyCount program."""
from pathlib import Path
from rich.console import Console

import typer

from pypi_count.py_counter import PyPiCount

cli = typer.Typer()

console = Console()


@cli.command()
def main(  # pylint: disable=R0913,R0912
    input_file: Path,
    class_def: bool = typer.Option(False, "--class-definitions"),
    import_statements: bool = typer.Option(False, "--import-statements"),
    comment: bool = typer.Option(False, "--comments"),
    function_def: bool = typer.Option(False, "--function-definitions"),
    if_statements: bool = typer.Option(False, "--if-statements"),
    function_without_docstrings: bool = typer.Option(False, "--function-without-docstrings"),
    function_with_docstrings: bool = typer.Option(False, "--function-with-docstrings"),
    class_with_docstrings: bool = typer.Option(False, "--class-with-docstrings"),
    class_without_docstrings: bool = typer.Option(False, "--class-without-docstrings"),
    find_parameters: bool = typer.Option(False, "--find-parameters"),
    assignment_statements: bool = typer.Option(False, "--assignment-statements"),
    while_loops: bool = typer.Option(False, "--while-loops"),
    for_loops: bool = typer.Option(False, "--for-loops"),

):
    """Main method to display the different options."""
    if input_file.is_file():
        pycount = PyPiCount(input_file)

        if class_def:
            console.print("\n# of class definitions: " + str(pycount.count_class_definitions()))

        if import_statements:
            console.print("\n# of import statements: " + str(pycount.count_import_statements()))

        if comment:
            console.print("\n# of comments: " + str(pycount.count_comments()))

        if function_def:
            console.print("\n# of function definitions: " + \
            str(pycount.count_function_definitions()))

        if function_without_docstrings:
            console.print("\n# of functions w/o docstrings: " + \
            str(pycount.count_functions_without_docstring()))

        if function_with_docstrings:
            console.print("\n# of functions with docstrings: " + \
            str(pycount.count_functions_with_docstring()))

        if class_without_docstrings:
            console.print("\n# of classes w/o docstrings: " + \
            str(pycount.count_classes_without_docstring()))

        if class_with_docstrings:
            console.print("\n# of functions with docstrings: " + \
            str(pycount.count_classes_with_docstring()))

        if if_statements:
            console.print("\n# of if statements: " + \
            str(pycount.count_if_statements()))

        if find_parameters:
            console.print("\n# of parameters in functions: " + \
            str(pycount.count_function_parameters()))

        if assignment_statements:
            console.print("\n of assignment statements: " + \
            str(pycount.count_assignment_statements()))

        if while_loops:
            console.print("\n of assignment statements: " + \
            str(pycount.count_while()))

        if for_loops:
            console.print("\n of assignment statements: " + \
            str(pycount.count_for()))
    else:
        console.print("Please input a valid file!")
