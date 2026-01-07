# Lab 2: Iterator, Generator, and Decorator
# -----------------------------------------

# -------------------------
# Iterator Example
# -------------------------
print("\n--- Iterator Example ---")
my_list = [1, 2, 3]
it = iter(my_list)  # Get iterator
print(next(it))     # 1
print(next(it))     # 2
print(next(it))     # 3

# -------------------------
# Generator Example
# -------------------------
print("\n--- Generator Example ---")
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# -------------------------
# Decorator Example
# -------------------------
print("\n--- Decorator Example ---")
def my_decorator(func):
    def wrapper():
        print("Before the function.")
        func()
        print("After the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# -------------------------
# For loop is not an iterator
# -------------------------
print("\n--- For Loop Info ---")
print("A for loop is not an iterator itself, but it uses an iterator internally.")

# -------------------------
# Comparison Table (Iterator vs Generator)
# -------------------------
print("\n--- Comparison Table ---")
comparison = """
Feature           | Iterator                       | Generator
-----------------|--------------------------------|----------------------------
Implementation   | Uses a class with __iter__ and __next__ | Uses a function with yield
Complexity       | More heavy code                 | Concise and easy to read
State            | You must manage the internal state manually | Python manages the state automatically
Memory           | Can be high if converting a large list | Highly memory-efficient
"""
print(comparison)

# -------------------------
# Program: Decorator + Generator Example
# -------------------------
print("\n--- Program: Passing Students ---")
def log_status(func):
    def wrapper(*args, **kwargs):
        print(f"--- Starting {func.__name__} ---")
        result = func(*args, **kwargs)
        print(f"--- Finished {func.__name__} ---")
        return result
    return wrapper

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

@log_status
def get_passing_students(students):
    for student in students:
        if student.score >= 50:
            yield student.name

classroom = [
    Student("Ram", 90),
    Student("Shyam", 40),
    Student("Hari", 75)
]

for name in get_passing_students(classroom):
    print(f"Passed: {name}")
