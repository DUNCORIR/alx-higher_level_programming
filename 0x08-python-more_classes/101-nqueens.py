#!/usr/bin/python3
"""
N Queens Puzzle Solver
"""
import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i] == col or \
            abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(N):
    """Solve the N queens problem using backtracking.
    Returns a list of all possible solutions.
    Each solution is a list that represents the queen's position.
    on each row.
    """
    def backtrack(board, row):
        """Backtracking helper to place queens."""
        if row == N:
            solutions.append(board[:])  # Store the solution
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1  # Reset the row after backtracking

        solutions = []  # This will hold all the solutions
        board = [-1] * N  # Initialize board with -1 (no queens placed yet)
        backtrack(board, 0)
        return solutions

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate if N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Validate if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem and print each solution
    solutions = solve_nqueens(N)
    if solutions:  # Ensure solutions exist
        for solution in solutions:
            print([[i, solution[i]] for i in range(N)])
