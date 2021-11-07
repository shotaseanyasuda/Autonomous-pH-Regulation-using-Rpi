#GardenManager.py
from AnalogProbe import *
from Pump import *
from MCP3008 import MCP3008
from tkinter import *
import time
import threading

    
upperLimit = 10.50 #Starting pH for upper limit
lowerLimit = 8.50 #Starting pH for lower limit

def addToUpperLimit():
    global upperLimit
    if(upperLimit < 13.9):
        upperLimit = upperLimit + 0.1
        upperLimitDisplay = Label (win, text="{:.1f}".format(upperLimit), font=("Arial Bold",40),bg='NavajoWhite2') #creates abels for upper limits
        upperLimitDisplay.place(x=520,y=125)
        #print("Upper Limit is now",upperLimit)
    else:
        pass
def subFromUpperLimit():
    global upperLimit
    if(upperLimit > lowerLimit + 0.6):
        upperLimit = upperLimit - 0.1
        upperLimitDisplay = Label (win, text="{:.1f}".format(upperLimit), font=("Arial Bold",40),bg='NavajoWhite2')
        upperLimitDisplay.place(x=520,y=125)
        #print("Upper Limit is now",upperLimit)
    else:
        pass
def addToLowerLimit():
    global lowerLimit
    if(lowerLimit < upperLimit - 0.6):
        lowerLimit = lowerLimit + 0.1
        lowerLimitDisplay = Label (win, text="{:.1f}".format(lowerLimit), font=("Arial Bold",40),bg='NavajoWhite2')
        lowerLimitDisplay.place(x=520,y=275)
        #print("Lower Limit is now",lowerLimit)
    else:
        pass
def subFromLowerLimit():
    global lowerLimit
    if(lowerLimit > 0.1):
        lowerLimit = lowerLimit - 0.1
        lowerLimitDisplay = Label (win, text="{:.1f}".format(lowerLimit), font=("Arial Bold",40),bg='NavajoWhite2')
        lowerLimitDisplay.place(x=520,y=275)
        #print("Lower Limit is now",lowerLimit)
    else:
        pass
        
# Dispenses 5ml of base solution
def dispenseBase():
    # Creates object p1 of class Pump
    p1 = Pump('/dev/ttyAMA1')
    # D is for dispense, number is for volume in ml
    p1.send_cmd("D,2")
    
# Dispenses 5ml of acid solution
def dispenseAcid():
    # Creates object p2 of class Pump
    p2 = Pump('/dev/ttyAMA0')
    # D is for dispense, number is for volume in ml
    p2.send_cmd("D,2")
    

#TODO: add conditionals so that lower limit will never exceed upper limit
#Upper limit must not exceed 14, lower limit must not go below 0.
    
win = Tk()
f = Frame(win)

# Title
win.title("pH Dashboard")
win.minsize(width=800,height=480) #matched to Elemnent14 7" touchscreen display screen resolution
win.configure(bg='NavajoWhite3')


# Displays current ph on a label and updates every 2 seconds
def displaypH():
    while True:
        # gets current pH and stores in variable currentph
        currentph = "{:.2f}".format(AnalogProbe.getpH())
        currentphlabel = Label (win, text=currentph,font=("Arial Bold",60),bg='NavajoWhite2')
        currentphlabel.place(x=240,y=170)
        time.sleep(2)
# Tests if pH is within range and dispenses Acid or Base accordingly
def regulatepH():
    while True:
        if(AnalogProbe.getpH() > upperLimit):
            print("too basic. dispensing acid")
            dispenseAcid()
            time.sleep(5)
        if(AnalogProbe.getpH() < lowerLimit):
            print("too acidic. dispensing base")
            dispenseBase()
            time.sleep(5)
        else:
            print("ph is within range. testing again in 5 seconds")
            time.sleep(5)
        
# Displays upper and lower limit before any changes are made via buttons
upperLimitDisplay = Label (win, text=upperLimit, font=("Arial Bold",40),bg='NavajoWhite2') #creates labels for upper limits
upperLimitDisplay.place(x=520,y=125)
lowerLimitDisplay = Label (win, text=lowerLimit, font=("Arial Bold",40),bg='NavajoWhite2')
lowerLimitDisplay.place(x=520,y=275)
    
# Displays Up and Down buttons to control the upper and lower thresholds
button1 = Button(win, text='  Up   ', command = addToUpperLimit,bg='NavajoWhite2' )
button1.place(x=650,y=120)
button2 = Button(win, text='Down', command = subFromUpperLimit,bg='NavajoWhite2')
button2.place(x=650,y=160)
button3 = Button(win, text='  Up   ', command = addToLowerLimit,bg='NavajoWhite2')
button3.place(x=650,y=270)
button4 = Button(win, text='Down', command = subFromLowerLimit,bg='NavajoWhite2')
button4.place(x=650,y=310)

# Dispense Acid Button
button5 = Button(win, text='Dispense Acid', command = dispenseAcid,bg='NavajoWhite2', font=("Arial Bold",20))
button5.place(x=80,y=370)

# Dispense Base Button
button6 = Button(win, text='Dispense Base', command = dispenseBase,bg='NavajoWhite2', font=("Arial Bold",20))
button6.place(x=330,y=370)
    
# Creates label "The current pH is:"
lbl = Label (win, text="pH: ", font=("Arial Bold",60),bg='NavajoWhite2')
lbl.place(x=80,y=170)

header = Label(win, text = " Auto pH Regulator  ",font=("Arial Bold",50),bg='NavajoWhite2' )
header.place(x=70,y=30)
        
x = threading.Thread(target = displaypH) #starts a new thread displaypH so that the program doesnt freeze
x.start() 

y = threading.Thread(target = regulatepH)
y.start()

win.mainloop()

    
    
    