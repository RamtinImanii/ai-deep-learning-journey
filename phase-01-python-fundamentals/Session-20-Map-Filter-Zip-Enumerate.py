"""Session 20: map, filter, zip, and enumerate.

Demonstrates transformations, filtering, pairing related data,
iteration, unpacking, and common iterator behaviors.
"""

# ============================================================
# 1. map(): transform every element
# ============================================================

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

# map() can also use a named function.
def normalize_score(score):
    return score / 100


scores = [60, 75, 90]
normalized_scores = list(map(normalize_score, scores))
print("Normalized scores:", normalized_scores)

# map() can process multiple iterables.
first_numbers = [1, 2, 3]
second_numbers = [10, 20, 30]

sums = list(map(lambda x, y: x + y, first_numbers, second_numbers))
print("Pairwise sums:", sums)


# ============================================================
# 2. filter(): keep elements that satisfy a condition
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

passing_scores = list(filter(lambda score: score >= 60, scores))
print("Passing scores:", passing_scores)

# filter(None, iterable) keeps truthy values.
# Be careful: 0, False, None, and empty strings are removed.
values = [0, 1, "", "Python", None, False]

truthy_values = list(filter(None, values))
print("Truthy values:", truthy_values)


# ============================================================
# 3. List comprehensions as an alternative
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

# Equivalent to a map() transformation.
doubled = [number * 2 for number in numbers]
print("Doubled numbers:", doubled)

# Equivalent to a filter() operation.
evens = [number for number in numbers if number % 2 == 0]
print("Even numbers with comprehension:", evens)

# Generator expressions produce values lazily.
squares = (number**2 for number in range(5))
print("Squares from generator:", list(squares))


# ============================================================
# 4. zip(): combine corresponding elements
# ============================================================

names = ["Ali", "Sara", "Reza", "Mina"]
student_scores = [12, 18, 9, 20]

student_records = list(zip(names, student_scores))
print("Student records:", student_records)

# zip() stops at the shortest iterable by default.
short_names = ["Ali", "Sara", "Reza"]
short_scores = [18, 20]

print("Unequal lengths:", list(zip(short_names, short_scores)))

# Python 3.10+: strict=True detects unequal lengths
# when the zip iterator is consumed.
try:
    list(zip(short_names, short_scores, strict=True))
except ValueError:
    print("Error: the iterables have different lengths.")

# Unpacking: turn pairs back into separate sequences.
pairs = [("Ali", 18), ("Sara", 20), ("Reza", 15)]

unpacked_names, unpacked_scores = zip(*pairs)
print("Unpacked names:", unpacked_names)
print("Unpacked scores:", unpacked_scores)


# ============================================================
# 5. Preserve relationships while filtering data
# ============================================================

names = ["Ali", "Sara", "Reza", "Mina", "Omid"]
scores = [12, 18, 9, 20, 15]

qualified_students = [
    (name, score)
    for name, score in zip(names, scores)
    if score >= 15
]

print("Qualified students:", qualified_students)

# Normalize the scores while keeping each name attached.
normalized_students = [
    (name, score, normalized)
    for name, score in qualified_students
    for normalized in [score / 20]
]

print("Normalized students:", normalized_students)


# ============================================================
# 6. enumerate(): iterate with a counter
# ============================================================

languages = ["Python", "SQL", "PyTorch"]

for index, language in enumerate(languages):
    print(index, language)

# start=1 changes the counter, not the list's actual indexes.
for number, language in enumerate(languages, start=1):
    print(f"{number}. {language}")


# ============================================================
# 7. Combine zip(), filter(), map(), and enumerate()
# ============================================================

names = ["Ali", "Sara", "Reza", "Mina", "Omid"]
scores = [12, 18, 9, 20, 15]

# Pair names with scores, then keep passing students.
qualified = filter(
    lambda student: student[1] >= 15,
    zip(names, scores),
)

# Normalize each qualified score while preserving the name
# and original score.
normalized = map(
    lambda student: (
        student[0],
        student[1],
        student[1] / 20,
    ),
    qualified,
)

# enumerate() numbers the resulting records.
for index, (name, original, normalized_score) in enumerate(
    normalized, start=1
):
    print(
        f"{index}. {name} | Original: {original} | "
        f"Normalized: {normalized_score}"
    )


# ============================================================
# 8. Iterator consumption
# ============================================================

result = map(lambda x: x * 2, [1, 2, 3])

print("First iteration:", list(result))
print("Second iteration:", list(result))  # Empty: already consumed.

# Materialize the result if it must be reused.
result = list(map(lambda x: x * 2, [1, 2, 3]))

print("Reusable result, first:", result)
print("Reusable result, second:", result)


# ============================================================
# 9. Data alignment in machine learning
# ============================================================

features = ["image_01", "image_02", "image_03"]
labels = ["cat", "dog", "cat"]

# Correct pairing depends on the two sequences having
# the same length and corresponding order.
dataset = list(zip(features, labels))
print("Dataset:", dataset)

# zip() does not verify that the order or meaning is correct.
# Data alignment must be ensured by the data-processing pipeline.
