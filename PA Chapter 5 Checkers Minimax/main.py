import pygame
from game.game import Game 
from minimax import minimax
from game.data import *
# from windowTk import *
import windowTk as tk
import numpy as np
import sys, time



pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
frames = 60
start = 0
end = 0
exectime = 0
check = False

def main():
    run = True
    check = False

    # tk = windowTk()
    # tk.runTK()

    tk
    check = tk.kill
    print("check kill", check)
    agent, nivel = tk.retValue()
    print("mode is: ",tk.retMode())
    mode = tk.mode
    
    if mode != 1 and mode != 2:
        mode = 1
    
    print("mode select: ", mode)
    checker(agent, nivel, mode)

    if check != True:
        check = False

    print("check kill if", check)
   
    
    # for debugging
    # checker("AI", 2, 2)
    # checker("Player", 2, 2)
    return 0


def checker(agent, depth, mode):
    gameOn = True
    game = Game(display)
    global start
    global end
    global exectime

    # start = 0
    # end = 0
    # exectime = 0

    if agent == "AI":
        pygame.display.set_caption('AI vs IA')
        print("AI vs IA")
        start = time.time()
        while gameOn:
            # pygame.time.delay(500)
            # pygame.time.delay(2000)
            clock.tick(frames)

            if game.turn == BLACK:
                value, new_board = minimax(game.getBoard(), depth, True, game, agent, game.turn, mode)
                game.moveFromIA(new_board)
                game.update()

            if game.turn == WHITE:
                value, new_board = minimax(game.getBoard(), depth,  False, game, agent, game.turn, mode)
                game.moveFromIA(new_board)
                game.update()

            if game.winner() != None:
                print(game.winner())
                gameOn = False
                color = game.winner()
                end = time.time()
                exectime = end - start
                game_over(agent, color)

            
            events = pygame.event.get()
            for event_num in np.nditer(range(len(events)), flags=['zerosize_ok']):
                event = events[event_num]
                if event.type == pygame.QUIT:
                    gameOn = False
                    break
                   
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, column = get_pos(pos)
                    game.select(row, column)


            game.update()
       
    
    if agent == "Player":
        print("Player vs AI")
        pygame.display.set_caption('Player vs IA')
        start = time.time()

        while gameOn:
            # pygame.time.delay(2000)
            clock.tick(frames)

            if game.turn == WHITE:
                value, new_board = minimax(game.getBoard(), depth, True, game, agent, game.turn, mode)
                game.moveFromIA(new_board)
                game.update()

            if game.winner() != None:
                print(game.winner())
                gameOn = False
                color = game.winner()
                end = time.time()
                exectime = end - start
                game_over(agent, color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOn = False
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, column = get_pos(pos)
                    game.select(row, column)


            game.update()

    print("Time Execution in ns: ", exectime)
    pygame.quit()
   
    return 0


def game_over(agent, color):
    # display.blit(background, [0, 0])
    display.fill(BLACK)
    textDraw("GAME OVER", 50, True, False, WIDTH//2, HEIGHT//8)
    textDraw("Checkers: " + agent + "vs AI", 35, True, False, WIDTH//2, HEIGHT//4)
    if color == WHITE and agent == "AI":
        textDraw(agent + ": Red Pieces Win the Round", 30, False, False, WIDTH//2, HEIGHT//2)
    if color == BLACK and agent == "AI":
        textDraw(agent + ": Black Pieces Win the Round", 30, False, False, WIDTH//2, HEIGHT//2)
    if color == BLACK and agent == "Player":
        textDraw(agent + ": Black Pieces Win the Round", 30, True, True, WIDTH//2, HEIGHT//2)
    if color == WHITE and agent == "Player":
        textDraw("AI: Red Pieces Win the Round", 30, True, True, WIDTH//2, HEIGHT//2)
    if color == TIE:
        textDraw("TIE", 30, True, True, WIDTH//2, HEIGHT//2)

    textDraw("Time of execution in ns: " + str(exectime), 30, True, False, WIDTH//2, HEIGHT *3/4)
    textDraw("To Continue, click the Mouse", 30, True, False, WIDTH//2, HEIGHT *0.85)
    textDraw("Close this Window, hit X button", 30, True, False, WIDTH//2, HEIGHT *0.95)
    pygame.display.flip()
        
    wait = True
    global check
    # check = False
    while wait:
        clock.tick(frames)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                wait = False
                break
                # pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                wait = False
                check = True
                # pygame.quit()
                break

       
    pygame.display.flip()
    return 0

def textDraw(text, size, bold, italic, xpoint, ypoint):
    font = pygame.font.SysFont("Time New Roman", size, bold, italic)
    render_font = font.render(text, True, WHITE)
    text_fig = render_font.get_rect()
    text_fig.midtop = (xpoint, ypoint)
    display.blit(render_font, text_fig)
    return 0

def get_pos(pos):
    x, y = pos
    posy = y // SIZE
    posx = x // SIZE
    return posy, posx

def setCheck(value):
    global check
    check = value

# for debugging
if __name__ == "__main__":
    main()
