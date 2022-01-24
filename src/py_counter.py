import libcst.matchers as m
import libcst as cst


class PyCount:


    def __init__(self):
        self.message = "Welcome to PyCount!"
        self.search = cst.parse_module(open("tests/import_test.py").read())


    def count_class_definitions(self):
        """Counting the class definitions."""
        print(len(m.findall(self.search, m.ClassDef())))


    def count_comments(self):
        """Counting the comments."""
        print(len(m.findall(self.search, m.Comment())))


    def count_import_statements(self):
        """Counting the import statements."""
        print(len(m.findall(self.search, m.Import())))


    def count_function_definitions(self):
        """Counting the function definitions."""
        FuncDefinitions = m.findall(self.search, m.FunctionDef())
        print(len(FuncDefinitions))


    def count_functions_without_docstring(self):
        """Counting the function definitions without docstrings."""
        functions_list = m.findall(self.search, m.FunctionDef())
        for f in functions_list:
            if f.get_docstring() == False:
                count += 1
                print(count)


    def count_classes_without_docstring(self):
        """Counting the class definitions without docstrings."""
        class_definitions = m.findall(self.search, m.ClassDef())
        for c in class_definitions:
            if c.get_docstring() == False:
                count += 1
                print(count)
