"""Python Counter for counting different parts of a program."""

import libcst.matchers as m
import libcst as cst


class PyCount:
    """Class for the python counter."""

    def __init__(self):
        """Declaring the self variable."""
        self.search = cst.parse_module(
            open("tests/import_test.py").read()  # pylint: disable=R1732,W1514
        )

    def count_class_definitions(self):
        """Counting the class definitions."""
        return len(m.findall(self.search, m.ClassDef()))

    def count_comments(self):
        """Counting the comments."""
        return len(m.findall(self.search, m.Comment()))

    def count_import_statements(self):
        """Counting the import statements."""
        return len(m.findall(self.search, m.Import()))

    def count_function_definitions(self):
        """Counting the function definitions."""
        func_definitions = m.findall(self.search, m.FunctionDef())
        return len(func_definitions)

    def count_functions_without_docstring(self):
        """Counting the function definitions without docstrings."""
        functions_list = m.findall(self.search, m.FunctionDef())
        for find in functions_list:
            if find.get_docstring() is False:
                count += 1
                return count

    def count_classes_without_docstring(self):
        """Counting the class definitions without docstrings."""
        class_definitions = m.findall(self.search, m.ClassDef())
        for finding in class_definitions:
            if finding.get_docstring() is False:
                count += 1
                return count
