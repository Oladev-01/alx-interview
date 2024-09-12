#!/usr/bin/python3
"""N queens"""
import sys


def solve_nqueens(N, board, row):
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row + 1)


def is_valid(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col or \
            board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        get_n = int(sys.argv[1])
    except (ValueError, TypeError):
        print("N must be a number")
        sys.exit(1)
    if get_n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * get_n
    solve_nqueens(get_n, board, 0)
