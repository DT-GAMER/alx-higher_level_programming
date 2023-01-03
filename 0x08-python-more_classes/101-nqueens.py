#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):

    # check if there is a queen in the same column

    for i in range(row):

        if board[i][col] == 1:

            return False

    # check if there is a queen in the same diagonal

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):

        if board[i][j] == 1:

            return False

    for i, j in zip(range(row, -1, -1), range(col, N, 1)):

        if board[i][j] == 1:

            return False

    return True

def solve_n_queens(board, row, N):

    if row == N:

        return True

    for col in range(N):

        if is_safe(board, row, col, N):

            board[row][col] = 1

            if solve_n_queens(board, row + 1, N):

                return True

            board[row][col] = 0

    return False

def print_board(board, N):

    for i in range(N):

        for j in range(N):

            if board[i][j] == 1:

                print("Q", end=" ")

            else:

                print(".", end=" ")

        print()

def nqueens(N):

    if not isinstance(N, int):

        print("N must be a number")

        sys.exit(1)

    if N < 4:

        print("N must be at least 4")

        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]

    if solve_n_queens(board, 0, N):

        print_board(board, N)

    else:

        print("No solution")

if __name__ == "__main__":

    if len(sys.argv) != 2:

        print("Usage: nqueens N")

        sys.exit(1)

    try:

        N = int(sys.argv[1])

    except ValueError:

        print("N must be a number")

        sys.exit(1)

    nqueens(N)

