
# AI Model Performance Analyzer

## Overview

AI Model Performance Analyzer is a command-line Python application for storing, managing, and analyzing basic information about AI models.

This project was built as part of my AI & Deep Learning learning journey to practice Python fundamentals through a practical, menu-driven application.

## Features

- **Add a Model:** Store a model's name, type, accuracy, and framework.
- **Show All Models:** Display all models currently stored in the application.
- **Find the Best Model:** Identify the model or models with the highest accuracy, including ties.
- **Filter Models by Accuracy:** Find models whose accuracy meets a specified minimum threshold.
- **Classify Model Performance:** Categorize models based on their accuracy:
  - **Good:** Accuracy >= 0.90
  - **Needs Improvement:** 0.70 < Accuracy < 0.90
  - **Bad:** Accuracy <= 0.70
- **Show Unique Frameworks:** Display the distinct frameworks used by the stored models.
- **Generate a Model Summary:** Display the total number of models, the best-performing model or models, high-performance models, and available frameworks.
- **Interactive Menu:** Navigate between features through a command-line interface.

## Technologies

- Python
- Python Standard Library

## Python Concepts Practiced

- Variables and data types
- Operators and conditional statements
- Loops
- User input and output
- Strings and formatted strings
- Lists, sets, and dictionaries
- List comprehensions and set comprehensions
- Filtering and comparing data
- Basic problem-solving and program design

## How to Run

### Prerequisites

Make sure Python is installed on your system.

### Run the Application

1. Open a terminal in the project directory.
2. Run the following command:

```bash
python main.py
```

3. Follow the interactive menu to use the application.

## Data Storage

Model information is stored in an in-memory Python list of dictionaries while the application is running.

**Note:** Data is not saved permanently. All stored model information is lost when the application exits.

## Limitations

- Input validation is limited.
- Model data is not persisted between runs.
- The application uses a command-line interface rather than a graphical interface.
- The project focuses on Python fundamentals rather than production-level software engineering.

## Future Improvements

- Add persistent data storage.
- Improve input validation and error handling.
- Refactor repeated logic into reusable functions.
- Improve the project's structure and maintainability.

## Author

Ramtin Imani

Part of the [AI & Deep Learning Journey](https://github.com/RamtinImanii/ai-deep-learning-journey).
