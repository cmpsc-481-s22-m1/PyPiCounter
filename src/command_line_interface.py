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
        console.print()
        class1 = pycount.count_class_definitions()
        console.print(f"The number of class definitions found in the file: {class1}")
    if import_statements:
        console.print()
        import1 = pycount.count_import_statements()
        console.print(f"The number of import statements found in the file: {import1}")
    if comment:
        console.print()
        comment1 = pycount.count_comments()
        console.print(f"The number of comments found in the file: {comment1}")
    if function_def:
        console.print()
        function1 = pycount.count_function_definitions()
        console.print(f"The number of function definitions found in the file: {function1}")
    if function_without_docstrings:
        console.print()
        without1 = pycount.count_functions_without_docstring()
        console.print(f"The number of functions without docstrings found in the file: {without1}")
    if class_without_docstrings:
        console.print()
        without2 = pycount.count_classes_without_docstring()
        console.print(f"The number of classes without docstrings found in the file: {without2}")
