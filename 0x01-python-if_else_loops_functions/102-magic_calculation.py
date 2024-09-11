#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c


print(magic_calculation(1, 2, 3))
print(magic_calculation(5, 4, 3))
print(magic_calculation(5, 4, 6))
print(magic_calculation(1, 2, 0))
print(magic_calculation(2, 3, 4))
