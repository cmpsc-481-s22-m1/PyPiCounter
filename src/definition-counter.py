# Given a counting tool that will be implemented, when putting the specifications set
# by the user into our user interface, then it will print out the correct number of
# class definitions that are inside a Python module or package.

from itertools import count

counter = count()

class Sample(something):
    number_of_classes = counter(0)

    def __init__(self):
        self.number_of_classes = next(self.number_of_classes)
