# PyPiCount

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

## Usefullness of Project

- Within LibCST, it has many nodes to "match" modules, expressions, and
statements which allowed us as programmers to complete our user stories in a
more uniform way. This project is useful because of the exploration of LibCST,
which ultimately allows end users to specify a given construct they would like
to identify in the source code (as LibCST will find all matches of this construct).

## Getting Started

Users can get started with this project by following the following steps:

1. Clone this repository and `cd` into the project folder
2. Run the command ```poetry install``` to install the dependencies for this project.
3. To familiarize yourself with the arguments accepted for this project, run the
command ```poetry run pypicount --help```. This command displays all of the
different arguments that can be passed. The list of the different arguments
are listed below:

```
Options:
  --input-file PATH              [required]
  --class_def                    [default: False]
  --import_statements            [default: False]
  --comment                      [default: False]
  --function_def                 [default: False]
  --if_statements                [default: False]
  --function_without_docstrings  [default: False]
  --function_with_docstrings     [default: False]
  --class_with_docstrings        [default: False]
  --class_without_docstrings     [default: False]
  --install-completion           Install completion for the current shell.
  --show-completion              Show completion for the current shell, to
                                 copy it or customize the installation.

  --help                         Show this message and exit.

```
These are the different types of arguments that PyPiCount will accept in this release.

4. Once you find your chosen arguments, run ```poetry run pypicount --[argument] --input-file [path/to/file]```

## Example of Output

Sample run command:

```
poetry run pypicount --class_with_docstrings --input-file tests/input/sample_file.py
```

Sample Output:

```
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
