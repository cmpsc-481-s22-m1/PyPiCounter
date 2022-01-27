"""Sample file to be analyzed for the test cases."""
import csv  # pylint: disable=W0611
import pytest  # pylint: disable=W0611


class TestClass:
    "This is a test class for the py counter."
    age = 10

    def test_greeting(self):  # pylint: disable=R0201
        """Test greeting for the test class."""
        print("Hello")

    def test_saying(self):  # pylint: disable=R0201
        """Test saying for the test class."""
        print("This is a test case.")

    def sample_function(self):
        print("Where did my docstring go?")


# Output: 10
print(TestClass.age)

# Output: <function Person.greet>
print(TestClass.test_greeting)
print()
print(TestClass.test_saying)
print()
print(TestClass.sample_function)

# Output: "This is a person class"
print(TestClass.__doc__)

class AnotherClass:
    age_again = 10
    def test_greeting_two(self):
        print("Hello, how are you?")

    def test_saying_two(self):
        if age_again == 10:
            print("What's the big idea?")
        else:
            print("What's up?")

    def test_sample_function(self):
        """Test sample function."""
        print("Found my docstring!")

# Output: <function Person.greet>
print(AnotherClass.test_greeting_two)
print()
print(AnotherClass.test_saying_two)
print()
print(AnotherClass.sample_function_two)

# Output: "This is a person class"
print(AnotherClass.__doc__)
