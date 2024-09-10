#!/usr/bin/python3

text = "PythonProgramming"

# indexing
print("Example 1: Indexing")
# indexing starts at 0 in Python.
print(f"First character (text[0]): {text[0]}")
print(f"Sixth Character (text[6]): {text[6]}")

# slicing
print("\nExample 2: Slicing")
# slicing sysntax: text[start:end] (end not included)
print(f"slice first four characters (text[:4]): {text[:4]}")
# 3. Slicing with step
print("\nExample 3: Slicing with step")
# Adding a step allows skipping characters
print(f"Slice with step of 2 (text[::2]): {text[::2]}")
print(f"Slice with step of 3 (text[::3]): {text[::3]}")

# 4. Negative Slicing
print("\nExample 4: Negative Slicing")
# Slicing in reverse
print(f"Slice last 5 characters (text[-5:]): {text[-5:]}")
print(f"Reverse the string (text[::-1]): {text[::-1]}")
