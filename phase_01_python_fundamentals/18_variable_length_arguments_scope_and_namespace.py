# Session 18: Variable-Length Arguments, Scope and Namespace


# 1. *args: collect positional arguments into a tuple
def calculate_sum(*args):
    return sum(args)


print("Sum:", calculate_sum(10, 20, 30))


# 2. **kwargs: collect keyword arguments into a dictionary
def show_model_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_model_info(name="Model A", accuracy=0.95)


# 3. Unpacking with * and **
def multiply(a, b, c):
    return a * b * c


numbers = [2, 3, 4]
print("Product:", multiply(*numbers))


def describe_model(name, accuracy):
    print(f"{name}: {accuracy}")


model = {"name": "Model B", "accuracy": 0.92}
describe_model(**model)


# 4. Local and global scope
value = 10


def show_scope():
    value = 20
    print("Local value:", value)


show_scope()
print("Global value:", value)


# 5. Enclosing scope and nonlocal
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()
    print("Enclosing count:", count)


outer()


# 6. Prefer explicit parameters and return values
def is_good_model(score, threshold):
    return score >= threshold


print("Model accepted:", is_good_model(0.93, 0.90))
