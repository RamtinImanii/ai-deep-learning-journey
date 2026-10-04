# Session 09 — Loops


# For Loop

for i in range(5):
    print(i)


# Loop through list

models = ["CNN", "RNN", "Transformer"]

for model in models:
    print(model)


# While Loop

count = 1

while count <= 5:
    print(count)
    count += 1


# Break example

for number in range(10):
    if number == 5:
        break

    print(number)


# Continue example

for number in range(5):
    if number == 2:
        continue

    print(number)


# AI Example

accuracies = [0.72, 0.91, 0.84, 0.95]

for accuracy in accuracies:

    if accuracy >= 0.90:
        print("Excellent")
    else:
        print("Needs improvement")