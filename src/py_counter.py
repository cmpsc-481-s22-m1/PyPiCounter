import libcst.matchers as m
import libcst as cst

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
                count++
         print(count)
        
        
    def count_classes_without_docstring(self):
        class_definitions = m.findall(self.search, m.ClassDef())
        for c in class_definitions:
            if class_definitions(c).get_docstring() == false:
                count++
         print(count)


pycount = PyCount()
pycount.count_class_definitions()
pycount.count_import_statements()
pycount.count_comments()
