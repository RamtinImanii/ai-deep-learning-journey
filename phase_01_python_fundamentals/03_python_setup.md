# Session 03 — Installing and Setting Up the Python Environment

## Overview

Prepared a professional Python development environment on Windows for the AI & Deep Learning journey.

## Environment

- Windows
- Python 3.13.7
- pip 25.2
- Visual Studio Code
- Python Virtual Environment (`.venv`)
- Git

## What I Learned

- Python Interpreter and how Python code is executed
- Development Environment
- VS Code and Python Interpreter selection
- Terminal / PowerShell
- Python Virtual Environments
- `pip` and package management basics
- Python project structure
- `.gitignore`
- Basic Git repository initialization

## Virtual Environment

Created and activated a project-specific Virtual Environment:

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

The project uses an isolated Python environment so that dependencies can be managed independently from other projects.

## Environment Verification

Verified the active Python environment using:

    python --version
    where.exe python
    python -m pip --version

The active Python interpreter and pip were confirmed to point to the project's `.venv`.

## Project Structure

    ai-deep-learning-journey/
    ├── .gitignore
    ├── .venv/
    └── phase-01-python-fundamentals/
        └── Session-03-Python-Setup.md

The `.venv` directory is excluded from Git tracking.

## Key Takeaways

- Each Python project should have its own isolated environment.
- VS Code should use the project's `.venv` interpreter.
- `python -m pip` helps ensure pip is executed with the intended Python interpreter.
- Virtual environments help prevent dependency conflicts between projects.
- `.gitignore` prevents unnecessary or sensitive files from being tracked by Git.

## Status

Session 03 completed.