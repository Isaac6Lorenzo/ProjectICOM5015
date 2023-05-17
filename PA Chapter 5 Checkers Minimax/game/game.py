import pygame
from game.board import Board
from game.data import *


class Game:
    def __init__(self, display):
        self.init()
        self.display = display
    
    def update(self):
        # print(self.board)
        self.board.draw(self.display)
        # print(self.board)
        self.drawValidMove(self.valid_moves)
        pygame.display.update()

    def init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def select(self, row, column):
        if self.selected:
            result = self.move(row, column)
            if not result:
                self.selected = None
                self.select(row, column)
        
        piece = self.board.getPiece(row, column)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.getValidMove(piece)
            return True
            
        return False

    def move(self, row, col):
        piece = self.board.getPiece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.eating(skipped)
            self.changeTurn()
        else:
            return False

        return True

    def drawValidMove(self, moves):
        for move in moves:
            row, column = move
            pygame.draw.circle(self.display, YELLOW, (column * SIZE + SIZE // 2, row * SIZE + SIZE // 2), 10)

    def changeTurn(self):
        pygame.time.delay(2000)
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def getBoard(self):
        return self.board

    def moveFromIA(self, board):
        self.board = board
        self.changeTurn()