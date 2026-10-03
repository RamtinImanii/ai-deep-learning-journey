# Session 05 — Operators

# Arithmetic Operators
x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

# Comparison Operators
age = 26

print(age == 26)
print(age > 18)
print(age < 18)
print(age != 30)

# Logical Operators
gpu_available = True
cpu_available = True

print(age > 18 and gpu_available)
print(gpu_available or cpu_available)
print(not gpu_available)

# Assignment Operators
value = 10
value += 5
value *= 2
value -= 4

print(value)

# Operator Precedence
result_1 = 2 + 3 * 4
result_2 = (2 + 3) * 4

print(result_1)
print(result_2)

# AI Training Configuration
epochs = 20
current_epoch = 12
learning_rate = 0.001
gpu_available = True

remaining_epochs = epochs - current_epoch
can_continue_training = gpu_available and remaining_epochs > 0

print(remaining_epochs)
print(can_continue_training)