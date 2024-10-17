#!/usr/bin/python3
"""
The module script reads stdin line by line and computes metrics.
"""


import sys

#  Variables initialized to track total file size and status code

total_file_size = 0
status_code_count = {
        "200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
        "404": 0, "405": 0, "500": 0
}
line_count = 0


def print_stats():
    """
    Prints Current statistics including total file size
    and status codes"""
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


try:
    #  Read from stdin lin by line
    for line in sys.stdin:
        line_count += 1

        #  Splits line by spaces to extract neccesary parts.
        parts = line.split()
        # check if line has expected no of parts to extract status code.
        if len(parts) >= 7:
            try:
                #  The status code is second last part
                status_code = parts[-2]
                file_size = int(parts[-1])  # Last part of file size.
                total_file_size += file_size

                if status_code in status_code_count:
                    status_code_count[status_code] += 1
            except (ValueError, IndexError):
                pass  # Skip lines that dont match expected format.

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

print_stats()  # Prints final stats if script ends normally
