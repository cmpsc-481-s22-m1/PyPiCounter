"""Python Counter for counting different parts of a program."""

import libcst.matchers as m
import libcst as cst


class PyCount:
    """Class for the python counter."""

    def __init__(self, filename):
        """Declaring the self variable."""
        with open(filename, 'r', encoding="utf8") as file:
            self.search = cst.parse_module(file.read())

    def count_class_definitions(self):
        """Counting the class definitions."""
        return len(m.findall(self.search, m.ClassDef()))


    def count_comments(self):
        """Counting the comments."""
        return len(m.findall(self.search, m.Comment()))


    def count_import_statements(self):
        """Counting the import statements."""
        return len(m.findall(self.search, m.Import()))


    def count_if_statements(self):
        """Counting the if statements."""
        return len(m.findall(self.search, m.If()))


    def count_function_definitions(self):
        """Counting the function definitions."""
        func_definitions = m.findall(self.search, m.FunctionDef())
        return len(func_definitions)


    def count_functions_without_docstring(self):  # pylint: disable=R1710
        """Counting the function definitions without docstrings."""
        functions_list = m.findall(self.search, m.FunctionDef())
        count = 0
        total_count = []
        for find in functions_list:
            if find.get_docstring() is None:
                total_count.append(count)
                count += 1
        return count


    def count_functions_with_docstring(self):  # pylint: disable=R1710
        """Counting the function definitions with docstrings."""
        function_definitions2 = m.findall(self.search, m.FunctionDef())
        count = 0
        total = []
        for finding in function_definitions2:
            if finding.get_docstring() is not None:
                count += 1
                total.append(count)
        return count

    def count_classes_without_docstring(self):  # pylint: disable=R1710
        """Counting the class definitions without docstrings."""
        class_definitions = m.findall(self.search, m.ClassDef())
        count = 0
        total_count = []
        for find in class_definitions:
            if find.get_docstring() is None:
                total_count.append(count)
                count += 1
        return count


    def count_classes_with_docstring(self):  # pylint: disable=R1710
        """Counting the class definitions without docstrings."""
        class_definitions2 = m.findall(self.search, m.ClassDef())
        count = 0
        total = []
        for find in class_definitions2:
            if find.get_docstring() is not None:
                total.append(count)
                count += 1
        return count
