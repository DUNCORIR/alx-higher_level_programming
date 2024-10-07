#!/usr/bin/python3
"""
N Queens Puzzle Solver
"""


import sys


def print_usage_and_exit():
    """Prints usage message and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid(board, row, col):
    """Checks if placing a queen at board[row][col] is valid."""
    for i in range(row):
        # Check the same column
        if board[i] == col:
            return False
        # Check the diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(n, board, row, solutions):
    """Uses backtracking to find all solutions for placing N queens."""
    if row == n:
        solutions.append(board[:])  # Found a valid solution
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col  # Place queen
            solve_nqueens(n, board, row + 1, solutions)  # Move to next row
            # No need to remove the queen; the board[row] will be overwritten


def main():
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print_usage_and_exit()

    # Validate the input
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [-1] * n  # Using -1 to indicate no queen placed
    solutions = []  # To store all valid solutions

    # Start solving the N queens problem
    solve_nqueens(n, board, 0, solutions)

    # Print all solutions
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])  # Format: [row, col]

    if __name__ == "__main__":
        main()
