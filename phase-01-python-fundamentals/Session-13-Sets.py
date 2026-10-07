# Session 13 — Sets


# Creating a Set
models = {"CNN", "ResNet", "Transformer"}
print(models)


# Unique Values
models = {"CNN", "CNN", "ResNet", "Transformer", "ResNet"}
print(models)


# Empty Set
empty_set = set()
print(empty_set)


# Set Does Not Support Indexing
# models[0]  # TypeError


# Adding Elements
models = {"CNN", "ResNet"}
models.add("Transformer")
print(models)


# Adding Multiple Elements
models.update(["ViT", "LLM"])
print(models)


# Removing Elements
models.remove("LLM")
print(models)


# Safe Removal
models.discard("UnknownModel")
print(models)


# Membership Testing
print("CNN" in models)
print("GAN" in models)


# Clearing a Set
temporary_models = {"CNN", "ResNet"}
temporary_models.clear()
print(temporary_models)


# Removing Duplicates from a List
model_list = [
    "CNN",
    "ResNet",
    "CNN",
    "Transformer",
    "ResNet"
]

unique_models = set(model_list)
print(unique_models)


# Set Operations
computer_vision = {"CNN", "YOLO", "ResNet", "ViT"}
generative_ai = {"GAN", "Diffusion", "Transformer", "ViT"}


# Union
all_models = computer_vision | generative_ai
print(all_models)


# Intersection
common_models = computer_vision & generative_ai
print(common_models)


# Difference
cv_only = computer_vision - generative_ai
print(cv_only)


# Symmetric Difference
different_models = computer_vision ^ generative_ai
print(different_models)


# Subset
models = {"CNN", "ResNet"}
all_models = {"CNN", "ResNet", "Transformer", "ViT"}

print(models.issubset(all_models))


# Superset
print(all_models.issuperset(models))


# Disjoint Sets
set_a = {"CNN", "ResNet"}
set_b = {"LLM", "RAG"}

print(set_a.isdisjoint(set_b))


# AI / Data Example
dataset_a_labels = {"cat", "dog", "bird"}
dataset_b_labels = {"dog", "horse", "bird"}

common_labels = dataset_a_labels & dataset_b_labels
all_labels = dataset_a_labels | dataset_b_labels

print(common_labels)
print(all_labels)