from sudoku import Sudoku
from windowTK import *
import time
from game import *

def main():

    runTK()
    agent, diff = retValue()
    print("agent: ", agent)
    print("nivel diff: ", diff)
    
    puzzle = create_boardSudoku(diff)
    board = create_boardTerminal(puzzle)
    puzzle.show_full()

    if agent == "Terminal":
        print("Use the library py-sudoku")
        start = time.time()
        solution = puzzle.solve()
        solution.show_full()
        end = time.time()

        print("time execution: ", end - start)

        print("\n\n")
        print("Use the Backtraking Method")
        start = time.time()
        backtracking(board)
        print_board(board)
        end = time.time()
        print("time execution in seconds: ", end - start)
    

    if agent == "Player":
        check, b = gamePlayer(board)
        print_board(b)
        print("Player - Time Execution in seconds: ", check)

    return 0

def getpos(board, row, col):
    return board[row][col]


def create_boardSudoku(diff):
    board = Sudoku(3).difficulty(diff/100)
    return board

def create_boardTerminal(puzzle):
    board = puzzle._copy_board(puzzle.board)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if getpos(board, i, j) == None:
                board[i][j] = 0
    return board

def print_terminal(board):
    b = Sudoku(3, board=board)
    b.show()

if __name__ == "__main__":
    main()