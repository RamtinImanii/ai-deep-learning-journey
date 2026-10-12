"""Session 19 — Lambda & Higher-Order Functions

Topics:
- Lambda expressions
- First-class functions
- Higher-order functions
- Callbacks
- Returning functions and closures
- Lambda with sorted()
- Common pitfalls and debugging
"""

# 1. Lambda expressions
double = lambda x: x * 2
print("Double:", double(7))


# 2. First-class functions
def square(x):
    return x**2


callback = square
print("Square:", callback(5))


# 3. Higher-order functions
def apply_function(func, value):
    return func(value)


print("Applied function:", apply_function(square, 4))


# 4. Lambda with sorted()
students = [
    {"name": "Ali", "score": 17},
    {"name": "Sara", "score": 20},
    {"name": "Reza", "score": 15},
]

sorted_students = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True,
)
print("Sorted students:", sorted_students)


# 5. Closure
def create_multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


double_number = create_multiplier(2)
triple_number = create_multiplier(3)

print("Double 5:", double_number(5))
print("Triple 5:", triple_number(5))


# 6. Avoiding late binding in a loop
functions = []

for i in range(3):
    functions.append(lambda i=i: i)

print("Loop values:", [func() for func in functions])
