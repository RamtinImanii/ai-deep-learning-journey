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

ai_models = ["CNN", "ResNet", "Transformer", "ViT", "LLM"]

print(len(ai_models))


# AI Example

training_config = [
    "ResNet",
    50,
    0.001,
    True
]

print(training_config)
print(training_config[0])
print(training_config[1])