# Session 14 — Dictionaries

# Creating a Dictionary
model = {
    "name": "ResNet",
    "version": 50,
    "framework": "PyTorch"
}
print(model)

# Accessing Values
print(model["name"])
print(model["framework"])

# Changing a Value
model["version"] = 101
print(model)

# Adding a New Key
model["accuracy"] = 0.95
print(model)

# Checking if a Key Exists
print("name" in model)
print("optimizer" in model)

# Using get()
print(model.get("framework"))
print(model.get("optimizer"))
print(model.get("optimizer", "Not specified"))

# Removing an Item with del
del model["version"]
print(model)

# Removing an Item with pop()
accuracy = model.pop("accuracy")
print(accuracy)
print(model)

# Dictionary Methods
model = {
    "name": "ResNet",
    "framework": "PyTorch",
    "accuracy": 0.95
}

print(model.keys())
print(model.values())
print(model.items())

# Looping Through a Dictionary
for key, value in model.items():
    print(f"{key}: {value}")

# Nested Dictionary
training_config = {
    "model": {
        "name": "ResNet",
        "version": 50
    },
    "training": {
        "epochs": 50,
        "batch_size": 32,
        "learning_rate": 0.001
    },
    "hardware": {
        "gpu": True
    }
}

print(training_config["model"]["name"])
print(training_config["training"]["learning_rate"])
print(training_config["hardware"]["gpu"])

# List of Dictionaries
models = [
    {
        "name": "ResNet",
        "accuracy": 0.95
    },
    {
        "name": "ViT",
        "accuracy": 0.97
    },
    {
        "name": "CNN",
        "accuracy": 0.91
    }
]

print(models[0]["name"])
print(models[1]["accuracy"])