#GUI
from phprobe import *
from tkinter import *

win = Tk()
f = Frame(win)

upperLimit = 7.2 #Starting pH for upper limit
lowerLimit = 6.8 #Starting pH for lower limit

#Title
win.title("pH Dashboard")
win.minsize(width=700,height=500)


#TODO: add conditionals so that lower limit will never exceed upper limit
#Upper limit must not exceed 14, lower limit must not go below 0.

def addToUpperLimit():
    global upperLimit
    upperLimit = upperLimit + 0.1
    upperLimitDisplay = Label (win, text=upperLimit) #creates abels for upper limits
    upperLimitDisplay.place(x=400,y=100)
    print("Upper Limit is now",upperLimit)
    return upperLimit
def subFromUpperLimit():
    global upperLimit
    upperLimit = upperLimit - 0.1
    upperLimitDisplay = Label (win, text=upperLimit)
    upperLimitDisplay.place(x=400,y=100)
    print("Upper Limit is now",upperLimit)
def addToLowerLimit():
    global lowerLimit
    lowerLimit = lowerLimit + 0.1
    upperLimitDisplay = Label (win, text=lowerLimit)
    upperLimitDisplay.place(x=400,y=200)
    print("Lower Limit is now",lowerLimit)
def subFromLowerLimit():
    global lowerLimit
    lowerLimit = lowerLimit - 0.1
    upperLimitDisplay = Label (win, text=lowerLimit)
    upperLimitDisplay.place(x=400,y=200)
    print("Lower Limit is now",lowerLimit)

button1 = Button(win, text='Up', command = addToUpperLimit)
button1.place(x=600,y=100)
button2 = Button(win, text='Down', command = subFromUpperLimit)
button2.place(x=600,y=150)
button3 = Button(win, text='Up', command = addToLowerLimit)
button3.place(x=600,y=200)
button4 = Button(win, text='Down', command = subFromLowerLimit)
button4.place(x=600,y=250)

#creates label "The current pH is:"
lbl = Label (win, text="The current pH is: ")
lbl.place(x=50,y=150)


#Displays current ph on a label
currentph = getph() #assigns ph value to variable x
currentphlabel = Label (win, text=currentph)
currentphlabel.place(x=50,y=200)
win.mainloop()

