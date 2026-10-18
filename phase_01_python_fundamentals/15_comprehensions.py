# Session 15 — Comprehensions

# List Comprehension
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]
print(squares)

# List Comprehension with Condition
even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]
print(even_numbers)

# AI Example: Filtering Accuracies
accuracies = [0.72, 0.91, 0.84, 0.95, 0.68]

high_accuracies = [
    accuracy
    for accuracy in accuracies
    if accuracy > 0.90
]
print(high_accuracies)

# List Comprehension with if/else
performance = [
    "Good" if accuracy >= 0.90 else "Needs Improvement"
    for accuracy in accuracies
]
print(performance)

# Set Comprehension
models = [
    "CNN",
    "ResNet",
    "CNN",
    "Transformer",
    "ResNet"
]

unique_models = {model for model in models}
print(unique_models)

# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]

number_squares = {
    number: number ** 2
    for number in numbers
}
print(number_squares)

# Dictionary Comprehension with Condition
models = {
    "CNN": 0.91,
    "ResNet": 0.95,
    "ViT": 0.97,
    "RNN": 0.84
}

high_accuracy_models = {
    model: accuracy
    for model, accuracy in models.items()
    if accuracy >= 0.90
}
print(high_accuracy_models)

# AI Example: Model Accuracies
model_names = ["CNN", "ResNet", "ViT"]
model_accuracies = [0.91, 0.95, 0.97]

model_results = {
    model: accuracy
    for model, accuracy in zip(model_names, model_accuracies)
}
print(model_results)

# Nested Comprehension
matrix = [
    [1, 2],
    [3, 4]
]

flattened = [
    number
    for row in matrix
    for number in row
]
print(flattened)