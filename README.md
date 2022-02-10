# PyPi-Counter

![PyPi-Counter](picture/design.png)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![example workflow](https://github.com/cmpsc-481-s22-m1/PyPiCounter/actions/workflows/main.yml/badge.svg)
![github issues](https://img.shields.io/github/issues/cmpsc-481-s22-m1/PyPiCounter)

## Table of Contents

- [Overview](#overview)
- [Project Usage](#usefulness-of-project)
- [Getting Started](#getting-started)
  - [Importing to Another Tool](#importing-into-another-grading-tool)
  - [Stand-Alone Usage](#stand-alone-usage)
- [Help and Bug Fixes](#help-and-bug-fixes)
- [Authors](#authors)

## Overview

- This project is a tool that, on its own, will provide assistance to
computer science professors to assist in grading assignments.
This tool will count and output the number of 'common errors'
(e.g., Classes without docstrings, functions without docstrings, etc.)
as well as the number of common computing structures (e.g.,
functions, Classes, looping constructs, imports, etc.)
all as specified by the user in the command line interface.

- This project also can serve as a collaborative enhancement
to import this tool into Allegheny College's
own GatorGrader to create new GatorGrader checks.
The program utilizes LibCST, which parses Python
code as a CST (Concrete Syntax Tree)
that keeps all formatting details (comments,
white spaces, parentheses, etc.).
As a released tool on PiPy, this tool can be imported into
any other automated grading tool as well.

## Usefulness of Project

- Within LibCST, it has many nodes to "match" modules, expressions, and
statements which allowed us as programmers to complete our user stories in a
more uniform way. This project is useful because of the exploration of LibCST,
which ultimately allows end users to specify a given construct they would like
to identify in the source code (as LibCST will find all matches of this construct).

## Getting Started

### Importing into Another Grading Tool

1. Install from PyPi by running `poetry add pypi-counter` in your terminal.
2. Import the PyPiCounter package with the syntax:
`from pypi_count.py_counter import PyPiCount`.
3. Call `PyPiCount` Class on specified file with the following syntax:
`stored_path = PyPiCount("path_to_file")`
Throughout this example, `stored_path` is an instance variable that stores the
result of the parsed file. Functions must be called on a parsed file.
4. Run the functions in the package using the `stored_path.[function_name]` syntax.
For example, `stored_path.count_comments()`

For best results, we recommend adding a print statement, as the functions
will only return the number of the specified construct. For example,

```python

console.print(f"Number of comments in this file: {stored_path.count_comments()}")

```

Will produce:

```python

Number of comments in this file: 26

```

The list of functions available are:

```python

count_class_definitions(file_name)                      
# returns the number of class definitions

count_comments(file_name)                                
# returns the number of comments

count_import_statements(file_name)                     
# returns the number of import statements

count_for_loops(file_name)                           
# returns the number of for loops

count_while_loops(file_name)                           
# returns the number of while loops

count_function_definitions(file_name)            
# returns the number of function definitions  

count_functions_without_docstrings(file_name)         
# returns the number of functions without docstrings

count_functions_with_docstrings(file_name)          
# returns the number of functions with docstrings

count_classes_with_docstrings(file_name)                  
# returns the number of classes with docstrings

count_classes_without_docstrings(file_name)             
# returns the number of classes without docstrings

count_function_parameters(file_name, function_name)    
# returns the number of function parameters
# after specifying the function name

count_assignment_statements(file_name)              
# returns the number of assignment statements

count_augmented_assignment_statements(file_name)
# returns the number of assignment statements that include
an augmented assignment operator (+=, -=)

```

### Stand-Alone Usage

Users can get started with this project by following the following steps:

1. Install the package with pip, using the command `pip install pypi-counter`
or `pipx install pypi-counter`
2. To familiarize yourself with the arguments accepted for this project, run the
command ```poetry run pypicount --help```. This command displays all of the
different arguments that can be passed. The list of the different arguments
are listed below:

  ```python
 Usage: pypicount [OPTIONS] INPUT_FILE

  Main method to display the different options.

Arguments:
  INPUT_FILE  [required]

Options:
  --class-definitions             [default: False]
  --import-statements             [default: False]
  --comments                      [default: False]
  --function-definitions          [default: False]
  --if-statements                 [default: False]
  --function-without-docstrings   [default: False]
  --function-with-docstrings      [default: False]
  --class-with-docstrings         [default: False]
  --class-without-docstrings      [default: False]
  --function-parameters TEXT
  --assignment-statements         [default: False]
  --augmented-assignment-statements
                                  [default: False]
  --while-loops                   [default: False]
  --for-loops                     [default: False]
  --install-completion            Install completion for the current shell.
  --show-completion               Show completion for the current shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.

  ```

These are the different types of arguments that PyPiCount will accept in this release.

Once you find your chosen arguments, run the following:

```python
poetry run pypicount --[argument] --input-file path/to/file
```

## Example of Output

Sample run command:

```python
poetry run pypicount --class-with-docstrings --input-file tests/input/sample_file.py
```

Sample Output:

```python
# of functions with docstrings: 1
```

## Help and Bug Fixes

- Users who are having trouble with navigating the program can come to the ReadMe
for assistance.
- Users can also open an issue on our [Issue Tracker](https://github.com/cmpsc-481-s22-m1/PyCount/issues)
with the following format:
  - Describe the bug
  - Include steps to replicate the bug
  - Expected behavior
  - Screenshots
  - Desktop OS

## Authors

- The people who maintain and contribute to this project are
  - Alexis Caldwell, [@caldwella2](https://github.com/caldwella2)
  - Adriana Solis, [@solisa986](https://github.com/solisa986)
  - Rachael Harris, [@rachaelharris](https://github.com/rachaelharris)
  - Ramon Guzman, [@guzmanr04](https://github.com/guzmanr04)
  - Ryan Hilty, [@RyanHiltyAllegheny](https://github.com/RyanHiltyAllegheny)
