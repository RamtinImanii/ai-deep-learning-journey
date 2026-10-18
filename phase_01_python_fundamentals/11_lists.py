# Session 11 — Lists


# Creating a List

models = ["CNN", "ResNet", "Transformer"]

print(models)


# Accessing List Elements

print(models[0])
print(models[-1])


# Changing a List Element

datasets = ["MNIST", "CIFAR-10", "ImageNet"]

datasets[1] = "CIFAR-100"

print(datasets)


# List Length

print(len(models))


# Adding Elements

models.append("ViT")
models.insert(1, "LLM")

print(models)


# Removing Elements

models.remove("LLM")
models.pop()

print(models)


# List Slicing

models = ["CNN", "ResNet", "Transformer", "ViT"]

print(models[1:3])


# Nested Lists

model_groups = [
    ["CNN", "ResNet"],
    ["Transformer", "ViT"]
]

print(model_groups[1][0])


# Sorting a List

models = ["Transformer", "CNN", "ViT", "ResNet"]

models.sort()

print(models)


# Reversing a List

models.reverse()

print(models)


# AI Example

accuracies = [0.72, 0.91, 0.84, 0.95]

accuracies.sort()

print(accuracies)