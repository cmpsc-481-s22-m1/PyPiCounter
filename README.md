# Py-Count ReadMe

## What does the project do?

- This project is a collaborative enhancement to import this tool into GatorGrader
to create new GatorGrader checks. The program utilizes LibCST, which parses Python
code as a CST (Concrete Syntax Tree) that keeps all formatting details (comments,
white spaces, parentheses, etc.)

## Why is the project useful?

- Within LibCST, it has many nodes to "match" modules, expressions, and
statements which allowed us as programmers to complete our user stories in a
more uniform way. This project is useful because of the exploration of LibCST.

## How users can get started with the project?

Users can get started with this project by following the following steps:

1. Clone this repository and `cd` into the project folder
2. Run the command ```poetry install``` to install the dependencies for this project
3. To familiarize yourself with the arguments accepted for this project, run the
command ```poetry run pypicount --help```. Output from running this command:
```
C:\Users\exampleuser\PyPiCount>poetry run pypicount --help
Usage: pypicount [OPTIONS]

  Main method to display the different options.

Options:
  --class_def                    [default: False]
  --import_statements            [default: False]
  --comment                      [default: False]
  --function_def                 [default: False]
  --function_without_docstrings  [default: False]
  --class_without_docstrings     [default: False]
  --install-completion           Install completion for the current shell.
  --show-completion              Show completion for the current shell, to
                                 copy it or customize the installation.

  --help                         Show this message and exit.
```

4. Once you find your chosen arguments, run ```poetry run pypicount --*argument*```. For example,
running the command ```poetry run pypicount --comment``` generates the following:
```
C:\Users\exampleuser\PyPiCount>poetry run pypicount --comment

The number of comments found in the file: 7

```

## Where can users get help with the project?

- Users who are having trouble with navigating the program can come to the ReadMe
for assistance.

## Who maintains and contributes to the project?

- The people who maintain and contribute to this project are Alexis Caldwell,
Adriana Solis, Rachael Harris, Ramon Guzman,
and Ryan Hilty
