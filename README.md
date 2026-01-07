# Advance_python_lab_2
This is lab 2

# Lab 2: Iterator, Generator, and Decorator

## Objective
To understand and implement Python Iterators, Generators, and Decorators, and see how they work in programs.

## Theory

### 1. Iterator
An **iterator** is an object that allows traversing through all elements of a collection (like a list) one by one.  
It implements two methods:
- `__iter__()` → returns the iterator object itself
- `__next__()` → returns the next element

Python’s `for` loop internally uses iterators to traverse collections.

### 2. Generator
A **generator** is a simple way to create iterators using a function and the `yield` keyword instead of `return`.  
Generators **pause their state** between calls, producing items on the fly, which is memory-efficient for large datasets.

### 3. Decorator
A **decorator** is a function that **wraps another function** to extend its behavior without modifying it.  
It allows adding functionality **before and after** the original function executes.

## Summary
- **Iterator vs Generator:** Generators are simpler, concise, and memory-efficient.  
- **Decorator:** Helps in adding extra functionality to functions dynamically.  

This lab demonstrates practical use of all three concepts with Python code.


## Output

--- Iterator Example ---
1
2
3

--- Generator Example ---
1
2
3

--- Decorator Example ---
Before the function.
Hello!
After the function.

--- Program: Passing Students ---
--- Starting get_passing_students ---
--- Finished get_passing_students ---
Passed: Ram
Passed: Hari

