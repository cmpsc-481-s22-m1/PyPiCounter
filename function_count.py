import libcst.FunctionDef as m
import libcst as cst

def PyCount():
    # parses through the given test file
    search = cst.parse_module(open("test.py").read())

    def count_function_definitions():
        f_definitions = m.findall(search, m.FunctionDef())
        print(len(f_definitions))
