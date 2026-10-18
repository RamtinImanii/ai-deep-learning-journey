# Session 08 — Conditional Statements


# Basic if statement

age = 20

if age >= 18:
    print("Adult")


# if else

score = 75

if score >= 50:
    print("Passed")
else:
    print("Failed")


# if elif else

accuracy = 0.87

if accuracy >= 0.9:
    print("Excellent model")

elif accuracy >= 0.8:
    print("Acceptable model")

else:
    print("Need improvement")


# Logical operators

gpu_available = True
cloud_available = False

if gpu_available or cloud_available:
    print("Training is possible")


# AI Model Deployment Checker

model_name = "ResNet"
accuracy = 0.93
gpu_available = True


if accuracy >= 0.9 and gpu_available:
    print(f"{model_name} is ready for deployment on GPU")

elif accuracy >= 0.9 and not gpu_available:
    print(f"{model_name} is accurate but needs CPU deployment")

else:
    print(f"{model_name} needs improvement")