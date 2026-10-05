# Session 12 — Tuples


# Creating a Tuple
models = ("CNN", "ResNet", "Transformer")
print(models)


# Accessing Tuple Elements
print(models[0])
print(models[-1])


# Tuple Length
print(len(models))


# Mixed Data Types
training_config = ("ResNet", 50, 0.001, True)
print(training_config)


# Single-Element Tuple
single_model = ("CNN",)
print(single_model)


# Parentheses Do Not Always Mean Tuple
not_a_tuple = ("CNN")
print(type(not_a_tuple))


# AI Example: Image Size
image_size = (224, 224)
print(f"Width: {image_size[0]}")
print(f"Height: {image_size[1]}")


# AI Example: RGB Channels
rgb_channels = ("Red", "Green", "Blue")
print(rgb_channels)


# Tuple Immutability
models = ("CNN", "ResNet", "Transformer")

# The following line would raise a TypeError:
# models[1] = "LLM"


# Tuple Methods
models = ("CNN", "ResNet", "CNN", "Transformer")

print(models.count("CNN"))
print(models.index("ResNet"))


# Tuple Unpacking
model, version, framework = ("ResNet", 50, "PyTorch")

print(model)
print(version)
print(framework)


# Practical Unpacking Example
width, height = (224, 224)

print(f"Width: {width}")
print(f"Height: {height}")