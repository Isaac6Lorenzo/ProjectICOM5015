import pygame
from game.piece import Piece
from game.data import *
import numpy as np


class Board:
    def __init__(self):
        self.board = []
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        self.black_kings_count = self.white_kings_count = 0
        self.black_count = self.white_count = 0
        self.createBoard()
    
    def drawBoard(self, display):
        display.fill(BLACK)
       
        for x in np.nditer(range(ROWS)):
            for y in np.nditer(range(x % 2, COLUMNS, 2)):
                pygame.draw.rect(display, WHITE, (x * SIZE, y * SIZE, SIZE, SIZE))

    def utilityValue(self, agent, color, mode):
        factor = 1
        # if color == WHITE and  agent == "Player":
        #     if mode == 1:
        #         return self.white_left - self.black_left + (self.white_kings * factor  - self.black_kings * factor )
        #     if mode == 2:
        #         return self.white_count - self.black_count + (self.white_kings_count * factor - self.black_kings_count *factor)
        # if color == WHITE and  agent == "AI":
        #     if mode == 1:
        #         return self.white_left - self.black_left + (self.white_kings * factor  - self.black_kings * factor )
        #     if mode == 2:
        #         return self.white_count - self.black_count + (self.white_kings_count * factor - self.black_kings_count *factor)
            
        # if color == BLACK and  agent == "AI":
        if mode == 1:
            return self.black_left - self.white_left + (self.black_kings * factor  - self.white_kings * factor )
        if mode == 2:
            return self.black_count - self.white_count + (self.black_kings_count * factor - self.white_kings_count *factor)

        return None
    

    def getAllPiecesByColor(self, color):
        piecelist = []

        color_string = ''
        if color == BLACK:
            color_string = "Black"
        else:
            color_string = "Red"

        for row in np.nditer(range(len(self.board)), flags=['zerosize_ok']):
            for piece in np.nditer(range(len(self.board[row])), flags=['zerosize_ok']):
                if self.board[row][piece] != 0 and self.board[row][piece].color == color:
                    piecelist.append(self.board[row][piece])

        print(len(piecelist), color_string)
        return piecelist

    def move(self, piece, row, column):
        self.board[piece.row][piece.column], self.board[row][column] = self.board[row][column], self.board[piece.row][piece.column]
        piece.move(row, column)

        if row == ROWS - 1 or row == 0:
            piece.createQueen()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.black_kings += 1

    def getPiece(self, row, col):
        return self.board[row][col]

    def createBoard(self):
       
        for row in np.nditer(range(ROWS), flags=['zerosize_ok']):
            self.board.append([])
            for column in np.nditer(range(COLUMNS), flags=['zerosize_ok']):
                if column % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, column, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, column, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        
    def draw(self, display):
        self.drawBoard(display)
        
        for row in np.nditer(range(ROWS), flags=['zerosize_ok']):
            for col in np.nditer(range(COLUMNS), flags=['zerosize_ok']):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(display)
        return 0

    def eating(self, pieces):
        
        for piece_num in np.nditer(range(len(pieces)), flags=['zerosize_ok']):
            piece = pieces[piece_num]
            self.board[piece.row][piece.column] = 0
            if piece != 0:
                if piece.color == BLACK:
                    if piece.queen == True:
                        self.black_kings_count +=1
                        self.black_kings -=1
                    else:
                        self.black_left -= 1
                        self.black_count +=1 
                elif piece.color == WHITE:
                        if piece.queen == True:
                            self.white_kings_count +=1
                            self.white_kings -=1
                        else:
                            self.white_left -= 1
                            self.white_count +=1 
        return None

    def noMoveLeft(self, listPieces):
        notMoving = False
        lenPiece = len(listPieces)
        count = 0
       
        for piece_num in np.nditer(range(len(listPieces)), flags=['zerosize_ok']):
            piece = listPieces[piece_num]
            lenght = len(self.getValidMove(piece))
            if lenght ==0:
                count = count + 1

        if count == lenPiece:
            notMoving = True

        return notMoving

    def winner(self):
        pieceBlack = self.getAllPiecesByColor(BLACK)
        pieceWhite = self.getAllPiecesByColor(WHITE)

        if self.black_left <= 0 or self.noMoveLeft(pieceBlack):
            print("THE WINNER IS RED: ")
            return WHITE
        elif self.white_left <= 0 or self.noMoveLeft(pieceWhite):
            print("THE WINNER IS BLACK: ")
            return BLACK

        elif self.black_left == 1 and self.white_left == 1:
            print("TIE")
            return TIE

        return None
    
    def getValidMove(self, piece):
        movelist = {}
        left = piece.column - 1
        right = piece.column + 1
        row = piece.row

        if piece.color == BLACK or piece.queen:
            movelist.update(self.moveLeft(row - 1, max(row - 3, -1), -1, piece.color, left))
            movelist.update(self.moveRight(row - 1, max(row - 3, -1), -1, piece.color, right))

        if piece.color == WHITE or piece.queen:
            movelist.update(self.moveLeft(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            movelist.update(self.moveRight(row + 1, min(row + 3, ROWS), 1, piece.color, right))
    
        return movelist

    def moveLeft(self, start, stop, step, color, left, skiplist=[]):
        movelist = {}
        last = []
        
        for move in np.nditer(range(start, stop, step), flags=['zerosize_ok']):
            if left < 0:
                break
        
            current = self.board[move][left]
            if current == 0:
                if skiplist and not last:
                    break
                elif skiplist:
                    movelist[(int(move), left)] = last + skiplist
                else:
                    movelist[(int(move), left)] = last
                
                if last:
                    if step == -1:
                        row = max(int(move)-3, 0)
                    else:
                        row = min(int(move)+3, ROWS)
                    movelist.update(self.moveLeft(move + step, row, step, color, left - 1, skiplist=last))
                    movelist.update(self.moveRight(move + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        # print(movelist)
        return movelist

    def moveRight(self, start, stop, step, color, right, skipped=[]):
        movelist = {}
        last = []
                
        for move in np.nditer(range(start, stop, step), flags=['zerosize_ok']):
            if right >= COLUMNS:
                break
            
            current = self.board[move][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    movelist[(int(move),right)] = last + skipped
                else:
                    movelist[(int(move), right)] = last
                
                if last:
                    if step == -1:
                        row = max(int(move)-3, 0)
                    else:
                        row = min(int(move)+3, ROWS)
                    movelist.update(self.moveLeft(move + step, row, step, color, right - 1, skiplist=last))
                    movelist.update(self.moveRight(move + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        # print(movelist)
        return movelist