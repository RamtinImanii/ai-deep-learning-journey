"""Session 21: Modules & Packages in Python.

Demonstrates importing modules and functions, organizing packages,
using standard library modules, inspecting module paths, and
understanding module execution and caching.
"""

# ============================================================
# 1. Modules: organize reusable code
# ============================================================

# A module is usually a Python (.py) file containing reusable
# functions, classes, or variables.
#
# Example project:
#
# my_project/
# |-- main.py
# |-- helpers.py
#
# helpers.py:
# def greet(name):
#     return f"Hello, {name}!"
#
# main.py:
# import helpers
# print(helpers.greet("Ramtin"))


# ============================================================
# 2. Different ways to import
# ============================================================

import math
import math as m
from math import sqrt

print("Square root using math:", math.sqrt(25))
print("Square root using from-import:", sqrt(36))
print("Pi using alias:", m.pi)

# import module_name:
# import math
# math.sqrt(25)
#
# from module_name import function_name:
# from math import sqrt
# sqrt(25)
#
# import module_name as alias:
# import math as m
# m.sqrt(25)
#
# Importing a specific function makes it directly accessible.
# Importing the module keeps its namespace explicit.
# Avoid "from module import *" in most project code because
# it can make the origin of names unclear.


# ============================================================
# 3. Packages: organize related modules
# ============================================================

# Example project structure:
#
# my_project/
# |-- main.py
# |-- utilities/
#     |-- __init__.py
#     |-- greetings.py
#     |-- calculations.py
#
# Import a function from a module inside a package:
#
# from utilities.greetings import greet
# from utilities.calculations import square
#
# __init__.py is commonly used to define a regular package.
# Some namespace packages can work without __init__.py.
#
# In this example, utilities is a package and greetings.py
# and calculations.py are modules inside that package.
#
# These imports work when the package is discoverable by Python.


# ============================================================
# 4. Absolute and relative imports
# ============================================================

# Absolute import:
# from utilities.greetings import greet
#
# Relative import, when used inside a package:
# from .greetings import greet
#
# A single dot refers to the current package.
# Relative imports depend on package context and can fail when
# a package file is run directly as a standalone script.
#
# Absolute imports are often easier to follow in beginner projects.


# ============================================================
# 5. Standard library: math
# ============================================================


def math_examples():
    """Demonstrate useful mathematical functions."""

    print("Square root:", math.sqrt(81))
    print("Pi:", math.pi)
    print("Ceiling:", math.ceil(4.2))
    print("Floor:", math.floor(4.8))
    print("Factorial:", math.factorial(5))


# math provides mathematical functions and constants.
# It is part of Python's standard library and needs no pip install.


# ============================================================
# 6. Standard library: random
# ============================================================

import random


def random_examples():
    """Demonstrate random number generation and selection."""

    print("Random integer:", random.randint(1, 10))
    print(
        "Random choice:",
        random.choice(["Python", "AI", "Data"]),
    )

    languages = ["Python", "SQL", "PyTorch"]
    random.shuffle(languages)
    print("Shuffled languages:", languages)


# random is useful for simulations, random selection, and examples.
# Its output can change between runs.
# Do not use random for security-sensitive tokens; use secrets.


# ============================================================
# 7. Standard library: statistics
# ============================================================

import statistics


def statistics_examples():
    """Calculate basic descriptive statistics."""

    scores = [60, 75, 90, 75, 100]

    print("Scores:", scores)
    print("Mean:", statistics.mean(scores))
    print("Median:", statistics.median(scores))
    print("Population standard deviation:", round(statistics.pstdev(scores), 2))


# statistics provides basic descriptive statistics.
# More advanced data analysis will use additional tools later.


# ============================================================
# 8. Standard library: datetime and pathlib
# ============================================================

from datetime import datetime
from pathlib import Path


def datetime_and_pathlib_examples():
    """Demonstrate date/time and filesystem path operations."""

    now = datetime.now()
    print("Current date and time:", now)

    file_path = Path("data") / "records.txt"

    print("Path:", file_path)
    print("File name:", file_path.name)
    print("File extension:", file_path.suffix)
    print("Parent directory:", file_path.parent)


# datetime handles dates and times.
# pathlib represents filesystem paths in a readable,
# cross-platform way.
# Creating a Path object does not create the file itself.


# ============================================================
# 9. The __name__ variable and direct execution
# ============================================================


def greet(name):
    return f"Hello, {name}!"


def square(number):
    return number**2


def demonstrate_main_guard():
    """Demonstrate reusable functions and the main guard."""

    print(greet("Ramtin"))
    print("Square of 6:", square(6))


# When a Python file is executed directly, __name__ is "__main__".
# When imported, its __name__ is normally the module's name.
#
# Put demonstration code inside this guard so it does not run
# merely because another module imports the file.


# ============================================================
# 10. Top-level execution and module caching
# ============================================================

# Consider helpers.py:
#
# print("Module loaded")
#
# def greet():
#     print("Hello")
#
# And main.py:
#
# import helpers
# import helpers
# helpers.greet()
#
# Under normal circumstances, "Module loaded" prints only once
# in that Python process. Python caches imported modules in
# sys.modules and reuses the cached module on later imports.
#
# importlib.reload() can explicitly reload a module.
#
# The examples above are illustrative; they do not create
# or import a separate helpers.py file.


# ============================================================
# 11. Finding and inspecting modules
# ============================================================

import sys
import importlib.util


def inspect_modules():
    """Inspect module search paths and module information."""

    print("Python module search paths:")
    for search_path in sys.path:
        print(search_path)

    print("math module name:", math.__name__)
    print("math module file:", getattr(math, "__file__", None))
    print("Names available in math:", dir(math))

    spec = importlib.util.find_spec("random")
    if spec is not None:
        print("random module origin:", spec.origin)


# sys.path contains locations Python searches when importing.
# It is not the path to one particular module.
#
# __file__ often identifies a module's file path, but some
# built-in modules do not have a __file__ attribute.
#
# dir(module) lists names available in a module.
# help(module.function) displays documentation for a function.
# Uncomment this line when needed:
# help(math.sqrt)
#
# To inspect an installed package in the terminal:
# python -m pip show numpy


# ============================================================
# 12. Naming conventions and common import errors
# ============================================================

# Prefer lowercase module names and snake_case.
# Avoid spaces, hyphens, and names starting with a digit.
#
# Avoid naming project files after standard library modules:
# math.py, random.py, json.py, statistics.py, typing.py
#
# Such filenames can shadow the intended module and cause
# confusing import errors.
#
# If an import fails, check:
# 1. The module or package name.
# 2. The project directory and package structure.
# 3. The current working directory and sys.path.
# 4. Whether a local file shadows a standard library module.
#
# For an external package, installation may be necessary:
# python -m pip install package_name
#
# The standard library modules shown in this session do not
# require installation with pip.


# ============================================================
# 13. Module, package, and library
# ============================================================

# Module:
# Usually one Python file containing reusable code.
#
# Package:
# A structure used to organize related modules.
#
# Library:
# A collection of reusable code that may include modules
# and packages.
#
# These terms can overlap in everyday technical usage.


# ============================================================
# 14. Main entry point
# ============================================================


def main():
    """Run the executable examples in this session."""

    print("\n--- Session 21: Modules & Packages ---")

    print("\n--- Reusable Functions ---")
    demonstrate_main_guard()

    print("\n--- math ---")
    math_examples()

    print("\n--- random ---")
    random_examples()

    print("\n--- statistics ---")
    statistics_examples()

    print("\n--- datetime and pathlib ---")
    datetime_and_pathlib_examples()

    print("\n--- Module Inspection ---")
    inspect_modules()


if __name__ == "__main__":
    main()
