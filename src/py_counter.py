import libcst.matchers as m
import libcst as cst

from rich.console import Console

import typer

cli = typer.Typer()

console = Console()


class PyCount:

    def __init__(self):
        # parses through the
        self.search = cst.parse_module(open("tests/import_test.py").read())

    def count_class_definitions(self):
        print(len(m.findall(self.search, m.ClassDef())))


    def count_import_statements(self):
        print(len(m.findall(self.search, m.Import())))


    def count_function_definitions(self):
        FuncDefinitions = m.findall(self.search, m.FunctionDef())
        print(len(FuncDefinitions))


    def count_functions_without_docstring(self):
        functions_list = m.findall(self.search, m.FunctionDef())
        for f in functions_list:
            if functions_list(f).get_docstring() == false:
                count += 1
            print(count)


    def count_classes_without_docstring(self):
        class_definitions = m.findall(self.search, m.ClassDef())
        for c in class_definitions:
            if class_definitions(c).get_docstring() == false:
                count += 1
            print(count)


@cli.command()
def main(
    class_def: str = typer.Option(...),
    import_statements: str = typer.Option(...),
    comment: str = typer.Option(...),
    function_def: str = typer.Option(...),
    function_without_docstrings: str = typer.Option(...),
    class_without_docstrings: str = typer.Option(...)
):
    """Main method to display the different options."""
    console.print("")
    if class_def:
        pycount = PyCount()
        pycount.count_class_definitions()
    if import_statements:
        pycount = PyCount()
        pycount.count_import_statements()
    if comment:
        pycount = PyCount()
        pycount.count_comments()
    if function_def:
        pycount = PyCount()
        pycount.count_function_definitions()
    if function_without_docstrings:
        pycount = PyCount()
        pycount.count_functions_without_docstring()
    if class_without_docstrings:
        pycount = PyCount()
        pycount.count_classes_without_docstring()
