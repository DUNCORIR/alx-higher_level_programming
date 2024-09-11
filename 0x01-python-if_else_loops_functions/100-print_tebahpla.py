#!/usr/bin/python3
def print_alphabet():
    print(''.join(
        chr(i) if (122 - i) % 2 == 0
        else chr(i - 32)
        for i in range(122, 96, -1)
    ), end='')


print_alphabet()
