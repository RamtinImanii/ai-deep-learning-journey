# Session 07 — Input and Output


# Basic Output
print("Hello, AI!")


# Variables and Print
name = "Ramtin"
age = 26

print(name, age)


# sep parameter
print("AI", "Deep Learning", "Python", sep=" | ")


# end parameter
print("Learning", end=" ")
print("Python")


# Basic Input
user_name = input("Enter your name: ")

print(f"Hello, {user_name}")


# Type Conversion
user_age = int(input("Enter your age: "))

print(f"After 5 years you will be {user_age + 5}")


# AI Training Configuration Example

model_name = input("Model name: ")
dataset = input("Dataset: ")
epochs = int(input("Epochs: "))
learning_rate = float(input("Learning rate: "))
gpu_available = input("GPU available: ")

print("\n===== Training Configuration =====")
print(f"Model: {model_name}")
print(f"Dataset: {dataset}")
print(f"Epochs: {epochs}")
print(f"Learning Rate: {learning_rate}")
print(f"GPU Available: {gpu_available}")
print("=================================")