# Model Database
models = [
    {"name": "Model A", "accuracy": 0.95, "precision": 0.92},
    {"name": "Model B", "accuracy": 0.87, "precision": 0.85},
    {"name": "Model C", "accuracy": 0.92, "precision": 0.90},
    {"name": "Model D", "accuracy": 0.78, "precision": 0.80},
    {"name": "Model E", "accuracy": 1.20, "precision": 0.91},
    {"name": "Model F", "accuracy": 0.78, "precision": True},
    {"name": "Model G", "accuracy": "0.98", "precision": 0.80},
]


# Validation
def select_valid_models(models: list) -> list:
    valid_models = [
        model
        for model in models
        if isinstance(model, dict)
        and isinstance(model.get("name"), str)
        and bool(model["name"].strip())
        and isinstance(model.get("accuracy"), (int, float))
        and not isinstance(model.get("accuracy"), bool)
        and isinstance(model.get("precision"), (int, float))
        and not isinstance(model.get("precision"), bool)
        and 0 <= model["accuracy"] <= 1
        and 0 <= model["precision"] <= 1
    ]

    return valid_models


# Best Model and Average Accuracy
def calculate_average_accuracy(valid_models: list) -> float:
    """Calculate the average accuracy of valid models."""
    if not valid_models:
        raise ValueError("Cannot calculate accuracy for an empty list.")

    accuracies = [model["accuracy"] for model in valid_models]
    average_accuracy = sum(accuracies) / len(accuracies)

    return average_accuracy


assert (
    round(calculate_average_accuracy(select_valid_models(models)), 2) == 0.88
), "Incorrect average accuracy calculation."


def choose_best_model(valid_models: list) -> list:
    """Return the model(s) with the highest accuracy."""
    if not valid_models:
        raise ValueError("Cannot choose a model from an empty list.")

    highest_accuracy = max(model["accuracy"] for model in valid_models)

    return [
        (model["name"], model["accuracy"])
        for model in valid_models
        if model["accuracy"] == highest_accuracy
    ]


# Filtering
def filter_models_by_accuracy(valid_models: list, threshold: float = 0.90) -> list:
    """Return models whose accuracy meets the threshold."""
    if not isinstance(threshold, (int, float)) or isinstance(threshold, bool):
        raise TypeError("Threshold must be a number.")

    if not 0 <= threshold <= 1:
        raise ValueError("Threshold must be between 0 and 1.")

    return [model for model in valid_models if model["accuracy"] >= threshold]


# Report
print("AI MODEL EVALUATION REPORT")
print("--------------------------")

valid_models = select_valid_models(models)
print(f"""Total models: {len(models)}
Valid models: {len(valid_models)}
Invalid models: {len(models) - len(valid_models)}\n""")

average_accuracy = calculate_average_accuracy(valid_models)
best_models = choose_best_model(valid_models)
print(f"Average accuracy: {average_accuracy:.2f}")
print("Best model(s): ", end="")

for i, (name, accuracy) in enumerate(best_models):
    if i > 0:
        print(", ", end="")

    print(f"{name} ({accuracy:.2f})", end="")


filtering_results = filter_models_by_accuracy(valid_models)
print("\n\nSelected models (threshold=0.90):")
for model in filtering_results:
    print(f"""- {model["name"]}: {model["accuracy"]}""")
