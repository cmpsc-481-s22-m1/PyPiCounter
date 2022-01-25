"""The command line interface for the PyCount program."""

from rich.console import Console

import typer

from src.py_counter import PyCount

cli = typer.Typer()

console = Console()

pycount = PyCount()


@cli.command()
def main(  # pylint: disable=R0913
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

    if class_def:
        pycount.count_class_definitions()
    if import_statements:
        pycount.count_import_statements()
    if comment:
        pycount.count_comments()
    if function_def:
        pycount.count_function_definitions()
    if function_without_docstrings:
        pycount.count_functions_without_docstring()
    if class_without_docstrings:
        pycount.count_classes_without_docstring()
