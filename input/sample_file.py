"""Test case for imports."""
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


# Output: 10
print(TestClass.age)

# Output: <function Person.greet>
print(TestClass.test_greeting)
print()
print(TestClass.test_saying)

# Output: "This is a person class"
print(TestClass.__doc__)
