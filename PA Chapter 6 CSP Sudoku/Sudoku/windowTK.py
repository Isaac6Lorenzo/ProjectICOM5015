import tkinter.messagebox as m
from tkinter import *
from tkinter import ttk as t

import os

path = os.getcwd()

numValue = 35
AI = False
Player = False
Terminal = False

root = Tk()
root.geometry('400x520')
root.title("Sudoku Game")

def runTK():
    global root
    global result
    global numValue
    global kill

    text = Label(root, text='Choose Terminal')
    text.pack()

    tPhoto = PhotoImage(file= 'resources\\terminal.png')
    tBtn = Button(root, image=tPhoto, command=terminal)
    tBtn.pack(side='top', padx=10)

    text = Label(root, text='Choose Player')
    text.pack()

    playerPhoto = PhotoImage(file= 'resources\\player.png')
    playerBtn = Button(root, image=playerPhoto, command=playerVs)
    playerBtn.pack(side='top', padx=10)

    text = Label(root, text='\nSet the degree of difficult.\nSelect Easy = 1, Medium = 2, Hard = 3.')
    text.pack()
    scale = Scale(root, from_=1, to=3, orient=HORIZONTAL, command=set_nivel)
    scale.pack()


    text = Label(root, text='\nPress the button below to Enter the configuration')
    text.pack()
    enterPhoto = PhotoImage(file = 'resources\\enter.png')
    enterBtn = Button(root, image=enterPhoto, command=enter)
    enterBtn.pack()

    text = Label(root, text='\nPress the button X, to destroy the tkinter')
    
    root.mainloop()    
    return 0


def enter():
    global AI
    global Player
    global Terminal
    check = True

    if Player == False and AI == False and Terminal == False:
        check = False
        m.showerror('Error Selection not made', 'Try again. Only choose one option between AI vs AI or Player vs Ai. Select the degree of difficult. Then press the enter button')


    if (Player == True and AI == True and Terminal == True) or (Player == True and AI == True and Terminal == False) or (Player == True and AI == False and Terminal == True) or (Player == False and AI == True and Terminal == True):
        AI = False
        Player = False
        Terminal = False
        check = False
        print("two or more boolean are true")
        print("reset the boolean")
        save("0")
        m.showerror('Error push two or more button at same time', 'You press two or more buttons, try again. Only choose one option between AI or Player')

    if Terminal == True and (Player and AI and AI) == False:
        # method call
        print("call Terminal game")
        AI = False
        Player = False
        Terminal = False

        save("Terminal")
        m.showinfo('Choose AI', 'Press the OK button to continue. Now you can select an other configuration to simulate.')
        
    
    if AI == True and (Player and AI and Terminal) == False:
        # method call
        print("call ai game")
        AI = False
        Player = False
        Terminal = False

        save("AI")
        m.showinfo('Choose AI', 'Press the OK button to continue. Now you can select an other configuration to simulate.')
        
    if Player == True and (Player and AI and Terminal) == False:
        # method call
        print("call player game")
        AI = False
        Player = False
        Terminal = False

        save("Player")        
        m.showinfo('Choose Player', 'Press the OK button to continue. Now you can select an other configuration to simulate.')

    if check == True:
        root.destroy()
        # root.quit()

    return 0
    
def terminal():
    global Terminal
    Terminal = True
    print("Terminal Method: ", Terminal)

def ai_vs_ai():
    global AI
    AI =True
    print("ai method: ", AI)

def playerVs():
    global Player
    Player = True
    print("player method: ", Player)

def save(str):
    global result
    result = str
    print(result)

def set_nivel(value):
    global numValue
    v = int(value)
    print("num. diff.: ", v)
    if v == 1:
        numValue = 35
    if v == 2:
        numValue = 65
    if v == 3:
        numValue = 85
    # return v

def retValue():
    global result
    global numValue

    return result, numValue
