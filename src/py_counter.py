import libcst.matchers as m
import libcst as cst

def PyCount():
    # parses through the given test file
    search = cst.parse_module(open("tests/import_test.py").read())

    def count_class_definitions():
        definitions = m.findall(search, m.ClassDef())
        print(len(definitions))
        
    def count_import_statements():
        print(len(m.findall(search, m.Import())))
    

    def count_function_definitions():
        FuncDefinitions = m.findall(search, m.FunctionDef())
        print(len(FuncDefinitions))
        
    def count_functions_without_docstring():
        functions_list = m.findall(search, m.functionDef())
        for f in functions_list:
            if functions_list(f).getdocstring() == false:
                count++
         print(count)
