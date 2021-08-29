#GUI

#TODO: add conditionals so that lower limit will never exceed upper limit
#Upper limit must not exceed 14, lower limit must not go below 0.

from phprobe import *
from tkinter import *
from MCP3008 import MCP3008
import time
import threading

win = Tk()
f = Frame(win)

upperLimit = 7.2 #Starting pH for upper limit
lowerLimit = 6.8 #Starting pH for lower limit

#Title
win.title("pH Dashboard")
win.minsize(width=800,height=480) #matched to Elemnent14 7" touchscreen display screen resolution
win.configure(bg='NavajoWhite3')

#ISClub Logo
#logo = PhotoImage(file="isclublogo.png")
#screenlogo = Label(win, image=logo)
#screenlogo.place(x=50,y=400)

#Displays upper and lower limit before any changes are made via buttons
upperLimitDisplay = Label (win, text=upperLimit, font=("Arial Bold",40),bg='NavajoWhite2') #creates abels for upper limits
upperLimitDisplay.place(x=550,y=125)
lowerLimitDisplay = Label (win, text=lowerLimit, font=("Arial Bold",40),bg='NavajoWhite2')
lowerLimitDisplay.place(x=550,y=275)


def addToUpperLimit():
    global upperLimit
    upperLimit = upperLimit + 0.1
    upperLimitDisplay = Label (win, text="{:.1f}".format(upperLimit), font=("Arial Bold",40),bg='NavajoWhite2') #creates abels for upper limits
    upperLimitDisplay.place(x=550,y=125)
    print("Upper Limit is now",upperLimit)
    return upperLimit
def subFromUpperLimit():
    global upperLimit
    upperLimit = upperLimit - 0.1
    upperLimitDisplay = Label (win, text="{:.1f}".format(upperLimit), font=("Arial Bold",40),bg='NavajoWhite2')
    upperLimitDisplay.place(x=550,y=125)
    print("Upper Limit is now",upperLimit)
def addToLowerLimit():
    global lowerLimit
    lowerLimit = lowerLimit + 0.1
    lowerLimitDisplay = Label (win, text="{:.1f}".format(lowerLimit), font=("Arial Bold",40),bg='NavajoWhite2')
    lowerLimitDisplay.place(x=550,y=275)
    print("Lower Limit is now",lowerLimit)
def subFromLowerLimit():
    global lowerLimit
    lowerLimit = lowerLimit - 0.1
    lowerLimitDisplay = Label (win, text="{:.1f}".format(lowerLimit), font=("Arial Bold",40),bg='NavajoWhite2')
    lowerLimitDisplay.place(x=550,y=275)
    print("Lower Limit is now",lowerLimit)

button1 = Button(win, text='Up', command = addToUpperLimit,bg='NavajoWhite2' )
button1.place(x=650,y=120)
button2 = Button(win, text='Down', command = subFromUpperLimit,bg='NavajoWhite2')
button2.place(x=650,y=160)
button3 = Button(win, text='Up', command = addToLowerLimit,bg='NavajoWhite2')
button3.place(x=650,y=270)
button4 = Button(win, text='Down', command = subFromLowerLimit,bg='NavajoWhite2')
button4.place(x=650,y=310)

#creates label "The current pH is:"
lbl = Label (win, text="pH: ", font=("Arial Bold",40),bg='NavajoWhite2')
lbl.place(x=80,y=200)

#Displays current ph on a label and updates every 2 seconds
def displayph():
    while True:
        currentph = "{:.2f}".format(getph())
        currentphlabel = Label (win, text=currentph,font=("Arial Bold",40),bg='NavajoWhite2')
        currentphlabel.place(x=180,y=200)
        time.sleep(2)
        
x = threading.Thread(target = displayph) #starts a new thread displayph so that the program doesnt freeze
x.start()
    
win.mainloop()

