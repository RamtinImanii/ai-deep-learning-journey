# Session 06 — Strings

# Basic Strings
name = "Ramtin"
language = "Python"
message = "Hello, AI!"

# Indexing
print(language[0])
print(language[-1])

# Length
print(len(language))

# Slicing
print(language[0:3])
print(language[::2])

# String Methods
text = "  deep learning  "

print(text.strip())
print(text.upper())
print(text.lower())
print(text.replace("deep", "machine"))

# Split and Join
words = "Python AI Deep Learning".split()
print(words)

text = " ".join(words)
print(text)

# Membership
print("AI" in text)

# f-string
model_name = "ResNet"
accuracy = 0.94

report = f"Model: {model_name}, Accuracy: {accuracy}"
print(report)

# String Immutability
original = "Python"
new_text = "J" + original[1:]

print(original)
print(new_text)