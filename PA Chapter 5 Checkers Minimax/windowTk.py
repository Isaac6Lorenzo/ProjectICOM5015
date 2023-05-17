import tkinter.messagebox as m
from tkinter import *
from tkinter import ttk as t
from pygame import mixer
from game.data import *
# from main import *

import os

path = os.getcwd()

mode = 1
kill = False
result = ""
numValue = 1
AI = False
Player = False
root = Tk()
root.geometry('400x720')
root.title("Checkers")


def enter():
    global AI
    global Player
    check = True
    # result = []

    if Player == False and AI == False:
        check = False
        m.showerror('Error Selection not made', 'Try again. Only choose one option between AI vs AI or Player vs Ai. Select the degree of difficult. Then press the enter button')


    if Player == True and AI == True:
        AI = False
        Player = False
        check = False
        print("both boolean are true")
        print("reset the boolean")
        # result.append("0")
        # print(result)
        save("0")
        m.showerror('Error push both button', 'You press both button, try again. Only choose one option between AI vs AI or Player vs Ai')
        # return TIE

    if AI == True and (Player and AI) == False:
        # method call
        print("call ai game")
        AI = False
        Player = False
        save("AI")
        # result.append("AI")
        # print(result)
        m.showinfo('Choose AI vs AI', 'Press the OK button to continue. Now you can select an other configuration to simulate.')
        
        # return WHITE

    if Player == True and (Player and AI) == False:
        # method call
        print("call player game")
        AI = False
        Player = False
        save("Player")        
        # result.append("Player")
        # print(result)
        m.showinfo('Choose Player vs AI', 'Press the OK button to continue. Now you can select an other configuration to simulate.')
        # return  BLACK

    # print("last res: ", result)
    # return result
    if check == True:
        root.destroy()
        # root.quit()

    return 0
    

def ai_vs_ai():
    global AI
    AI =True
    print("ai method: ", AI)
    
    return 0
def playerVs():
    global Player
    Player = True
    print("player method: ", Player)
    return 0

def save(str):
    global result
    result = str
    print(result)
    # return result

def set_nivel(value):
    global numValue
    v = int(value)
    print("num. diff.: ", v)
    numValue = v
    # return v

def retValue():
    global result
    global numValue

    return result, numValue

def kill():
    global kill
    kill = True
    root.destroy()

def mode(value):
    global mode
    m = int(value)
    print("mode: ", m)
    mode = m

def retMode():
    global mode
    return mode

text = Label(root, text='Chose Player vs AI')
text.pack()

# playerPhoto = PhotoImage(file='resources\\player.png')
playerPhoto = PhotoImage(file=path+'/resources/player.png')
playerBtn = Button(root, image=playerPhoto, command=playerVs)
playerBtn.pack(side='top', padx=10)

text = Label(root, text='Choose AI vs AI')
text.pack()

# aiPhoto = PhotoImage(file = 'resources\\android.png')
aiPhoto = PhotoImage(file = path+'/resources/android.png')
aiBtn = Button(root, image=aiPhoto, command=ai_vs_ai)
aiBtn.pack(side='top', padx=10)

text = Label(root, text='\nSet the degree of difficult use in Minimax')
text.pack()

scale = Scale(root, from_=1, to=6, orient=HORIZONTAL, command=set_nivel)
scale.pack()

text = Label(root, text='\nSet the degree of Mode use in Minimax\nTo select the Mode Survive = 1 or to select the Mode Attack = 2')
text.pack()

scale2 = Scale(root, from_=1, to=2, orient=HORIZONTAL, command=mode)
scale2.pack()

text = Label(root, text='\nPress the button below to Enter the configuration')
text.pack()

# enterPhoto = PhotoImage(file = 'resources\\enter.png')
enterPhoto = PhotoImage(file = path+'/resources/enter.png')
enterBtn = Button(root, image=enterPhoto, command=enter)
enterBtn.pack()

text = Label(root, text='\nPress the button below to destroy the tkinter')
text.pack()

# killPhoto = PhotoImage(file = 'resources\\kill.png')
killPhoto = PhotoImage(file = path+'/resources/kill.png')
killBtn = Button(root, image=killPhoto, command=kill)
killBtn.pack()

print("kill: ", kill)
root.mainloop()    
    
