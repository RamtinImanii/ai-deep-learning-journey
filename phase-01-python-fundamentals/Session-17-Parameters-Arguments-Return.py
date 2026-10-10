"""Session 17: Parameters, Arguments, Return, and Function Best Practices."""


# 1. Multiple Return Paths
def classify_accuracy(accuracy):
    if not 0 <= accuracy <= 1:
        return "Invalid Accuracy"

    if accuracy >= 0.9:
        return "Excellent"

    if accuracy >= 0.7:
        return "Good"

    return "Needs Improvement"


print(classify_accuracy(0.95))
print(classify_accuracy(0.75))
print(classify_accuracy(1.2))


# 2. Function Composition
def square(number):
    return number**2


def add_one(number):
    return number + 1


print(square(add_one(3)))  # 16


# 3. Testing with assert
def multiply(a, b):
    return a * b


assert multiply(3, 4) == 12
assert multiply(-2, 3) == -6
assert multiply(0, 5) == 0


# 4. Basic Type Hints
def calculate_average(scores: list[float]) -> float:
    return sum(scores) / len(scores)


print(calculate_average([0.8, 0.9, 1.0]))


# 5. Input Validation
def evaluate_threshold(threshold):
    if not isinstance(threshold, (int, float)):
        return "Invalid Input"

    if not 0 <= threshold <= 1:
        return "Threshold Out of Range"

    return "Valid Threshold"


print(evaluate_threshold(0.9))
print(evaluate_threshold(1.5))
print(evaluate_threshold("high"))


# 6. Mutable Default Argument — Avoid This Pattern
# Incorrect pattern: the same list is reused across calls.
#
# def add_item(item, items=[]):
#     items.append(item)
#     return items


# Safe pattern: use None to create a fresh list when needed.
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


print(add_item("Model A"))  # ['Model A']
print(add_item("Model B"))  # ['Model B']


# 7. Mutation of Mutable Objects
def add_model(models, model):
    models.append(model)


models = [{"name": "Model A"}]
add_model(models, {"name": "Model B"})
print(models)


# 8. Docstrings
def get_accuracy(correct: int, total: int) -> float:
    """Return the ratio of correct predictions to total predictions."""
    return correct / total


print(get_accuracy(95, 100))


# 9. Introductory Scope
def calculate_total():
    total = 10
    return total


print(calculate_total())

# 'total' is local to calculate_total().
# print(total)  # Uncommenting this line raises NameError.


# 10. Parameters and Arguments
def divide(a, b):
    return a / b


print(divide(10, 2))


# 11. Positional Arguments
def subtract(a, b):
    return a - b


print(subtract(10, 3))


# 12. Keyword Arguments
print(subtract(b=3, a=10))


# 13. Combining Positional and Keyword Arguments
def describe_model(name, accuracy, framework="PyTorch"):
    return f"{name}: {accuracy:.0%} accuracy using {framework}"


print(describe_model("Model A", 0.95))
print(describe_model("Model B", 0.92, framework="TensorFlow"))


# 14. Default Parameters
def calculate_discount(price, discount_percent=10):
    return price * (1 - discount_percent / 100)


print(calculate_discount(200))  # 180.0
print(calculate_discount(200, 20))  # 160.0


# 15. Returning Multiple Values
def analyze_scores(scores):
    if not scores:
        return None, None

    average = sum(scores) / len(scores)
    highest = max(scores)

    return average, highest


average, highest = analyze_scores([0.8, 0.9, 1.0])
print(f"Average: {average:.2f}")
print(f"Highest: {highest:.2f}")


# 16. Using the Return Value of One Function in Another
def normalize_percentage(value):
    return value / 100


def is_high_accuracy(accuracy, threshold=0.9):
    return accuracy >= threshold


accuracy = normalize_percentage(95)
print(is_high_accuracy(accuracy))


# 17. Avoiding Missing Return Values
def get_model_status(accuracy):
    if accuracy >= 0.9:
        return "Excellent"

    return "Needs Improvement"


print(get_model_status(0.95))
print(get_model_status(0.8))


# 18. Clear Parameter Names
def calculate_accuracy(correct_predictions, total_predictions):
    if total_predictions <= 0:
        return None

    return correct_predictions / total_predictions


print(calculate_accuracy(95, 100))


# 19. AI Model Evaluation Example
def evaluate_model(name, accuracy, threshold=0.9):
    if not isinstance(accuracy, (int, float)):
        return "Invalid Accuracy"

    if not 0 <= accuracy <= 1:
        return "Accuracy Out of Range"

    if accuracy >= threshold:
        status = "Pass"
    else:
        status = "Needs Improvement"

    return {
        "name": name,
        "accuracy": accuracy,
        "threshold": threshold,
        "status": status,
    }


print(evaluate_model("Model A", 0.95))
print(evaluate_model("Model B", 0.82, threshold=0.85))


# 20. Filtering Model Accuracies
def filter_accuracies(accuracies, threshold=0.9):
    if not isinstance(threshold, (int, float)):
        return []

    if not 0 <= threshold <= 1:
        return []

    return [
        score
        for score in accuracies
        if isinstance(score, (int, float)) and 0 <= score <= 1 and score >= threshold
    ]


scores = [0.72, 0.91, 0.85, 0.97, 0.90, 1.2, "unknown"]

print(filter_accuracies(scores))
print(filter_accuracies(scores, threshold=0.95))
