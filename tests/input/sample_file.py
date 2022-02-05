"""Sample file to be analyzed for the test cases."""
import csv  # pylint: disable=W0611
import pytest  # pylint: disable=W0611


class TestClass:
    "This is a test class for the py counter."
    real_age = 10
    x = 2
    x +=4

    def __init__(self, name, age):
        "Init function that defines the parameters."
        self.name = name
        self.age = age

    def test_greeting(self):  # pylint: disable=R0201
        """Test greeting for the test class."""
        print("Hello")

    def test_saying(self):  # pylint: disable=R0201
        """Test saying for the test class."""
        print("This is a test case.")

    def sample_function(self): # pylint: disable=C0116,R0201
        print("Where did my docstring go?")

# Output: 10
print(TestClass.real_age)

# Output: <function Person.greet>
print(TestClass.test_greeting)
print()
print(TestClass.test_saying)
print()
print(TestClass.sample_function)
testing = TestClass(10, "Lily")
print()
print(f"A sample age: {testing.age}")
print(f"A sample name: {testing.name}")

# Output: "This is a person class"
print(TestClass.__doc__)


class AnotherClass: # pylint: disable=C0115
    def __init__(self, name, age, bio):
        self.name = name
        self.age = age
        self.bio = bio

    def test_greeting_two(self): # pylint: disable=C0116,R0201
        print("Hello, how are you?")

    def test_saying_two(self): # pylint: disable=C0116,R0201
        age_again = 10
        if age_again == 10:
            print("What's the big idea?")
        else:
            print("What's up?")

    def test_sample_function(self): # pylint: disable=C0116,R0201
        """Test sample function."""
        print("Found my docstring!")

    def test_sample_for(self): # pylint: disable=C0116,R0201
        fruits = ["apple", "banana", "cherry"] # Sample for loop
        for x in fruits:    # pylint: disable=R0201,C0103
            if x == "banana":
                break
            print(x)

# Output: <function Person.greet>
print(AnotherClass.test_greeting_two)
print()
print(AnotherClass.test_saying_two)
print()
print(AnotherClass.test_sample_function)
test_two = AnotherClass("PyPiCounter v0.2.0", 1, \
                        "I am a counting tool for Python packages or modules.")
print()
print(f"I am {test_two.name}.")
print(f"I am currently in the {test_two.age}st phase of my software development.")
print(f"{test_two.bio}")

# Output: "This is a person class"
print(AnotherClass.__doc__)
