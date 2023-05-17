from copy import deepcopy as copy
from time import sleep
from game.data import *
import pygame
import numpy as np


def minimax(board, depth, player, game, agent, color, mode):
    if depth == 0 or board.winner() != None:
        return board.utilityValue(agent, color, mode), board

    if player:
        alpha = float('-inf')
        bestMove = None

        all_moves = getAllPossibleMove(board, WHITE, game)
        for move_num in np.nditer(range(len(all_moves)), flags=['zerosize_ok']):
            result = minimax(all_moves[move_num], depth-1, False, game, agent, color, mode)[0]
            alpha = max(alpha, result)
            if alpha == result:
                bestMove = all_moves[move_num]

        return alpha, bestMove

    else:
        beta = float('inf')
        bestMove = None

        all_moves = getAllPossibleMove(board, BLACK, game)
        for move_num in np.nditer(range(len(all_moves)), flags=['zerosize_ok']):
            move = all_moves[move_num]
            result = minimax(move, depth-1, True, game, agent, color, mode)[0]
            beta = min(beta, result)
            if beta == result:
                bestMove = move

        return beta, bestMove


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.eating(skip)
    return board


def getAllPossibleMove(board, color, game):
    movelist = []
    listOfPieces = board.getAllPiecesByColor(color)
    
    for piece_num in np.nditer(range(len(listOfPieces)), flags=['zerosize_ok']):
        # listOfMoving = board.getValidMove(listOfPieces[piece_num])
        # getValidMovesList = listOfMoving
        piece = listOfPieces[piece_num]
        getValidMovesList =  board.getValidMove(piece)
        for key_num in np.nditer(range(len(getValidMovesList)), flags=['zerosize_ok']):
            move = list(getValidMovesList)[key_num]
            skip = getValidMovesList[move]
            # print(move, skip)
            copyBoard = copy(board)
            copyPiece = copyBoard.getPiece(piece.row, piece.column)
            simulate_board = simulate_move(copyPiece, move, copyBoard, game, skip)
            movelist.append(simulate_board)

    return movelist