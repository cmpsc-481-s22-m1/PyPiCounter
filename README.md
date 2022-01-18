# project-template

Simple Python project template with basic CI (Continuous Integration) and
developer support infrastructure. The GitHub Actions workflow executes
[pytest](https://pytest.org/) (with
[coverage](https://pypi.org/project/pytest-cov/)) and
[pylint](https://pylint.org/) using the Poetry configuration, and checks
markdown with [markdownlint](https://github.com/DavidAnson/markdownlint) and
spelling with [cspell](https://cspell.org/).

## Requirements

- [Python](https://realpython.com/installing-python/)
- [Pipx](https://pypa.github.io/pipx/installation/)
- [Poetry](https://python-poetry.org/docs/#installing-with-pipx)

## Usage

### Installing Python dependencies

After cloning this project, you will likely want to instruct Poetry to create a
virtual environment and install the Python packages (like pytest and pylint)
listed in `pyproject.toml`. You also likely want to configure Poetry to create
that virtual environment in your local project folder, so that text editors like
Visual Studio Code can find the environment and provide code completion.

To configure Poetry to create a virtual environment in your local project folder
(only needed once per system):

```bash
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true
```

To install Python dependencies:

```bash
poetry install
```

### Running tasks

This project uses the [taskipy](https://github.com/illBeRoy/taskipy) task runner
to simplify testing and linting. You can see the actual commands run when tasks
are executed under the `[tool.taskipy.tasks]` header in `pyproject.toml`.

- **Test** your code with `poetry run task test`
- **Lint** your code with `poetry run task lint`

### Writing code

This project provides a basic "hello world" example package named `hello`. When
using this template, you should replace or rename this package (and mentions of
it in `pyproject.toml`) with your own package.
