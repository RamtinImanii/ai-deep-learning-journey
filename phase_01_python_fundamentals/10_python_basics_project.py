print("Please Answer These Questions About Your Model")


model = input("Model: ")
epochs = int(input("Epochs: "))
learning_rate = float(input("Learning Rate: "))

gpu_input = input("GPU Available (True/False): ")

if gpu_input.lower() == "true":
    gpu_available = True
else:
    gpu_available = False

result = ""

is_ready = True

if epochs > 10 and gpu_available and learning_rate <= 0.1:
    result += "\nTraining setup is ready!"

if epochs >= 100:
    result += "\nLong training expected."

if epochs <= 10:
    result += "\nIncrease epochs for better training."
    is_ready = False

if not gpu_available:
    result += "\nTraining can run but may be slower."
    is_ready = False

if learning_rate > 0.1:
    result += "\nWarning: Learning rate may be too high."
    is_ready = False

print("===== Training Configuration =====")

print(f"""
Model: {model}
Epochs: {epochs}
Learning Rate: {learning_rate}
GPU Available: {gpu_available}

{result}
""")

print("==================================")