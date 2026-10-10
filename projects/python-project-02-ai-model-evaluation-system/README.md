# AI Model Evaluation System

## Overview

A Python mini-project for validating AI model evaluation data, calculating average accuracy, identifying the best-performing model, and filtering models based on an accuracy threshold.

## Features

- Validate model data and metric types.
- Reject invalid accuracy and precision values.
- Calculate the average accuracy of valid models.
- Identify the model or models with the highest accuracy.
- Filter models using a configurable accuracy threshold.
- Generate a readable evaluation report.

## Concepts Practiced

- Python functions
- Lists and dictionaries
- List comprehensions
- Type checking and validation
- Exception handling
- Type hints and docstrings
- Assertions
- String formatting

## Technologies

- Python

## How to Run

Run `main.py` using Python 3:

```bash
python main.py
```

## Expected Results

- Total models: 7
- Valid models: 4
- Invalid models: 3
- Average accuracy: 0.88
- Best model: Model A (0.95)
- Models meeting the 0.90 accuracy threshold: Model A and Model C

## Note

This project is an educational example. Accuracy is used as the primary selection metric; real-world model evaluation should consider the problem requirements and other relevant metrics.