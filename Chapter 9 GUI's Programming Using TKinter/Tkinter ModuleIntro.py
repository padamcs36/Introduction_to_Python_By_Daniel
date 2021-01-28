'''
The tkinter module contains the classes for creating GUIs.
The Tk class creates a window for holding GUI widgets (i.e., visual components).
'''
from tkinter import *
tk = Tk() #create a window
label = Label(tk, text = "Welcome to Python") #creat a label
button = Button(tk, text = "Click Me!") #create a button

btShoworHide = Button(tk, text='Show',bg="white", font='courier 15 bold underline')
btShoworHide['text'] = 'Hide'
btShoworHide['bg'] = 'black'
btShoworHide['fg'] = 'white'
btShoworHide['font'] = 'times 10 bold italic'

label.pack() #place the label in the window
button.pack() #place the button in the window
btShoworHide.pack()
tk.mainloop() #create an event loop