# Session 16 — Functions


# 1. Basic Function
def say_hello():
    print("Hello, Ramtin!")


# 2. Function with a Parameter and Return
def square(number):
    return number**2


# 3. Function with Multiple Parameters
def add(a, b):
    return a + b


# 4. Boolean Return
def is_even(number):
    return number % 2 == 0


# 5. List Processing
def get_high_accuracies(accuracies):
    return [accuracy for accuracy in accuracies if accuracy >= 0.9]


# 6. Conditional Return
def classify_model(accuracy):
    if not 0 <= accuracy <= 1:
        return "Invalid Accuracy!"
    elif accuracy >= 0.9:
        return "Good"
    elif accuracy > 0.7:
        return "Needs Improvement"
    else:
        return "Bad"


# 7. Working with Lists
def count_models(models):
    return len(models)


# 8. Set Comprehension
def get_unique_frameworks(models):
    return {model["framework"] for model in models}


# Challenge — Find the Best Models
def find_best_models(models):
    best_models = []

    for model in models:
        if len(best_models) == 0:
            best_models.append(model)
        elif model["accuracy"] > best_models[0]["accuracy"]:
            best_models.clear()
            best_models.append(model)
        elif model["accuracy"] == best_models[0]["accuracy"]:
            best_models.append(model)

    return best_models
