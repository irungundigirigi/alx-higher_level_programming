#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys

def initialize_board(size):
    """Initialize an `size`x`size` sized chessboard with empty spaces."""
    board = []
    [board.append([]) for i in range(size)]
    [row.append(' ') for i in range(size) for row in board]
    return board

def deep_copy_board(board):
    """Return a deep copy of a chessboard."""
    if isinstance(board, list):
        return list(map(deep_copy_board, board))
    return board

def find_queen_positions(board):
    """Return the list of lists representation of a solved chessboard."""
    queen_positions = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                queen_positions.append([r, c])
                break
    return queen_positions

def mark_unsafe_positions(board, row, col):
    """Mark positions on a chessboard where non-attacking queens cannot be placed."""
    # Mark all forward positions
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # Mark all backward positions
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Mark all positions below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # Mark all positions above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Mark all positions diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all positions diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # Mark all positions diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all positions diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1

def solve_nqueens_recursively(board, current_row, queens_placed, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        current_row (int): The current working row.
        queens_placed (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens_placed == len(board):
        solutions.append(find_queen_positions(board))
        return solutions

    for col in range(len(board)):
        if board[current_row][col] == " ":
            temp_board = deep_copy_board(board)
            temp_board[current_row][col] = "Q"
            mark_unsafe_positions(temp_board, current_row, col)
            solutions = solve_nqueens_recursively(temp_board, current_row + 1,
                                                  queens_placed + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    size = int(sys.argv[1])
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_board(size)
    solutions = solve_nqueens_recursively(chessboard, 0, 0, [])
    for solution in solutions:
        print(solution)
