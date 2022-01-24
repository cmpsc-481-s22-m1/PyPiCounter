import libcst.matchers as m
import libcst as cst

class PyCount:

    def __init__(self):
        # parses through the
        self.search = cst.parse_module(open("tests/import_test.py").read())


    def count_class_definitions(self):
        definitions = m.findall(self.search, m.ClassDef())
        print(len(definitions))

    def count_import_statements(self):
        print(len(m.findall(self.search, m.Import())))

    def count_comments(self):
        print(len(m.findall(self.search, m.Comment())))


pycount = PyCount()
pycount.count_class_definitions()
pycount.count_import_statements()
pycount.count_comments()
