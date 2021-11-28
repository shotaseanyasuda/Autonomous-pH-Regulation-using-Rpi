# GardenManagerV2.py
import tkinter as tk
from AnalogProbe import *
from Pump import *
from MCP3008 import MCP3008
from tkinter import *
import time
import threading
from DHTSensor import *

upperLimit = 10.50 #Starting pH for upper limit
lowerLimit = 8.50 #Starting pH for lower limit

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()
    
# Page1 pH Control Panel
class Page1(Page):
    
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # Creates label Auto pH Regulator
        header = Label(self, text = "pH Dashboard",font=("Arial Bold",50),bg='NavajoWhite2' )
        header.place(x=70,y=30)
        # Starts thread to displaypH
        threading.Thread(target=self.displaypH).start()
        
        
        # Dispenses 5ml of base solution
        def dispenseBase():
            # Creates object p1 of class Pump
            p1 = Pump('/dev/ttyAMA1')
            # D is for dispense, number is for volume in ml
            p1.send_cmd("D,2")
            print("dispensing base")
            
        # Dispenses 5ml of acid solution
        def dispenseAcid():
            # Creates object p2 of class Pump
            p2 = Pump('/dev/ttyAMA0')
            # D is for dispense, number is for volume in ml
            p2.send_cmd("D,2")
            print("dispensing acid")
        
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
                    
        # Starts thread to displaypH
        threading.Thread(target=regulatepH).start()
        
        # Displays upper and lower limit before any changes are made via buttons
        upperLimitDisplay = Label (self, text=upperLimit, font=("Arial Bold",40),bg='NavajoWhite2') #creates labels for upper limits
        upperLimitDisplay.place(x=520,y=125)
        lowerLimitDisplay = Label (self, text=lowerLimit, font=("Arial Bold",40),bg='NavajoWhite2')
        lowerLimitDisplay.place(x=520,y=275)
        
        # Pre-set pH settings for plants that the user can select
        def pHPlantSettings(plant):
            global upperLimit
            global lowerLimit
            # Lettuce Settings
            if (plant == 'lettuce'):
                upperLimit = 6.50
                lowerLimit = 6.00
                upperLimitDisplay = Label (self, text="{:.1f}".format(upperLimit) + "  ", font=("Arial Bold",40),bg='NavajoWhite2') #creates abels for upper limits
                upperLimitDisplay.place(x=520,y=125)
                lowerLimitDisplay = Label (self, text="{:.1f}".format(lowerLimit), font=("Arial Bold",40),bg='NavajoWhite2')
                lowerLimitDisplay.place(x=520,y=275)
            # Strawberry Settings
            if (plant == 'strawberry'):
                upperLimit = 6.50
                lowerLimit = 5.50
                upperLimitDisplay = Label (self, text="{:.1f}".format(upperLimit) + "  ", font=("Arial Bold",40),bg='NavajoWhite2') #creates abels for upper limits
                upperLimitDisplay.place(x=520,y=125)
                lowerLimitDisplay = Label (self, text="{:.1f}".format(lowerLimit), font=("Arial Bold",40),bg='NavajoWhite2')
                lowerLimitDisplay.place(x=520,y=275)
            if (plant == 'basil'):
                upperLimit = 6.20
                lowerLimit = 5.80
                upperLimitDisplay = Label (self, text="{:.1f}".format(upperLimit) + "  ", font=("Arial Bold",40),bg='NavajoWhite2') #creates abels for upper limits
                upperLimitDisplay.place(x=520,y=125)
                lowerLimitDisplay = Label (self, text="{:.1f}".format(lowerLimit), font=("Arial Bold",40),bg='NavajoWhite2')
                lowerLimitDisplay.place(x=520,y=275)
            if (plant == 'spinach'):
                upperLimit = 6.50
                lowerLimit = 5.50
                upperLimitDisplay = Label (self, text="{:.1f}".format(upperLimit) + "  ", font=("Arial Bold",40),bg='NavajoWhite2') #creates abels for upper limits
                upperLimitDisplay.place(x=520,y=125)
                lowerLimitDisplay = Label (self, text="{:.1f}".format(lowerLimit), font=("Arial Bold",40),bg='NavajoWhite2')
                lowerLimitDisplay.place(x=520,y=275)
            else:
                pass
        
        # Lettuce Button
        button11 = Button(self, text = "Lettuce", command = lambda: pHPlantSettings('lettuce'),font=("Arial Bold",20))
        button11.place(x=70,y=350)
        
        # Strawberry Button
        button12 = Button(self, text = "Strawberry", command = lambda: pHPlantSettings('strawberry'),font=("Arial Bold",20))
        button12.place(x=200,y=350)
        
        # Basil Button
        button13 = Button(self, text = "Basil", command = lambda: pHPlantSettings('basil'),font=("Arial Bold",20))
        button13.place(x=380,y=350)
        
        # Spinach Button
        button13 = Button(self, text = "Spinach", command = lambda: pHPlantSettings('spinach'),font=("Arial Bold",20))
        button13.place(x=480,y=350)
    # Displays current ph on a label and updates every 2 seconds
    def displaypH(self):
        while True:
            # gets current pH and stores in variable currentph
            currentph = "{:.2f}".format(AnalogProbe.getpH())
            currentphlabel = Label (self, text="pH: " + currentph,font=("Arial Bold",60),bg='NavajoWhite2')
            currentphlabel.place(x=80,y=170)
            time.sleep(2)
    def addToUpperLimit(self):
        print("pressed")
        #global upperLimit
        global upperLimit
        if(upperLimit < 13.9):
            upperLimit = upperLimit + 0.1
            upperLimitDisplay = Label (self, text="{:.1f}".format(upperLimit), font=("Arial Bold",40),bg='NavajoWhite2') #creates abels for upper limits
            upperLimitDisplay.place(x=520,y=125)
            print("Upper Limit is now",upperLimit)
        else:
            pass
    def subFromUpperLimit(self):
        global upperLimit
        if(upperLimit > lowerLimit + 0.6):
            upperLimit = upperLimit - 0.1
            upperLimitDisplay = Label (self, text="{:.1f}".format(upperLimit), font=("Arial Bold",40),bg='NavajoWhite2')
            upperLimitDisplay.place(x=520,y=125)
            print("Upper Limit is now",upperLimit)
        else:
            pass
    def addToLowerLimit(self):
        global lowerLimit
        if(lowerLimit < upperLimit - 0.6):
            lowerLimit = lowerLimit + 0.1
            lowerLimitDisplay = Label (self, text="{:.1f}".format(lowerLimit), font=("Arial Bold",40),bg='NavajoWhite2')
            lowerLimitDisplay.place(x=520,y=275)
            print("Lower Limit is now",lowerLimit)
        else:
            pass
    def subFromLowerLimit(self):
        global lowerLimit
        if(lowerLimit > 0.1):
            lowerLimit = lowerLimit - 0.1
            lowerLimitDisplay = Label (self, text="{:.1f}".format(lowerLimit), font=("Arial Bold",40),bg='NavajoWhite2')
            lowerLimitDisplay.place(x=520,y=275)
            print("Lower Limit is now",lowerLimit)
        else:
            pass
        
# Page2 Temperature Control Panel
class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # Starts thread to displayTemperature
        threading.Thread(target=self.displayTemperature).start()
        temperatureLabel = Label(self, text = "Temperature Dashboard",font=("Arial Bold",40),bg='NavajoWhite2' )
        temperatureLabel.place(x=50,y=30)
    
    # Displays Temp Label and Live Temp
    def displayTemperature(self):
        while True:
            try:
                temp = DHTSensor.getTemperature()
                celcius = "{:.1f}".format(temp)
                fahrenheit = "{:.1f}".format(temp * (9 / 5) + 32)
                fahrenheitLabel = Label (self, text="Temperature: " + fahrenheit + " F°",font=("Arial Bold",40),bg='NavajoWhite2')
                fahrenheitLabel.place(x=150,y=160)
                celciusLabel = Label (self, text="Temperature: " + celcius + " C°",font=("Arial Bold",40),bg='NavajoWhite2')
                celciusLabel.place(x=150,y=250)
                print(celcius, fahrenheit)
                
                #DHTSensor.getTemperature()
                print("successfully read temp:" + str(temp))
                
            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                time.sleep(2.0)
                continue    
            time.sleep(8)

# Page3 Humidity Control Panel
class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        # Starts thread to displayHumidity
        threading.Thread(target=self.displayHumidity).start()
        
        humidityLabel = Label(self, text = "Humidity Dashboard",font=("Arial Bold",40),bg='NavajoWhite2' )
        humidityLabel.place(x=50,y=30)

    # Displays Humidity Label and Live Humidity
    def displayHumidity(self):
        while True:
            try:
                humidity = "{:.1f}".format(DHTSensor.getHumidity())
                humidityLabel = Label (self, text="Humidity:       " + humidity + " %",font=("Arial Bold",40),bg='NavajoWhite2')
                humidityLabel.place(x=150,y=160)

                #DHTSensor.getTemperature()
                print("successfully read humidity" + humidity)
                
            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                time.sleep(2.0)
                continue
            time.sleep(8)
     
# Page4 Maintenance Panel            
class Page4(Page):
    # instanciate variable running for dispensing while button held
    running = False
    reverserunning = False
    
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        maintenanceInstructions = Label(self, text = "Hold for Continuous Dispensing",font=("Arial Bold",30),bg='NavajoWhite2' )
        maintenanceInstructions.place(x=80,y=30)
        
        precisionInstructions = Label(self, text = "Precision Dispensing",font=("Arial Bold",30),bg='NavajoWhite2' )
        precisionInstructions.place(x=80,y=270)
            # Dispenses 1ml of base solution
        def dispense1mlBase():
            # Creates object p1 of class Pump
            p1 = Pump('/dev/ttyAMA1')
            # D is for dispense, number is for volume in ml
            p1.send_cmd("D,1")
            print("dispensing 1ml base")
            
        # Dispenses 1ml of acid solution
        def dispense1mlAcid():
            # Creates object p2 of class Pump
            p2 = Pump('/dev/ttyAMA0')
            # D is for dispense, number is for volume in ml
            p2.send_cmd("D,1")
            print("dispensing 1ml acid")
            
        # Dispenses 2ml of base solution
        def dispense2mlBase():
            # Creates object p1 of class Pump
            p1 = Pump('/dev/ttyAMA1')
            # D is for dispense, number is for volume in ml
            p1.send_cmd("D,2")
            print("dispensing 2ml base")
            
        # Dispenses 2ml of acid solution
        def dispense2mlAcid():
            # Creates object p2 of class Pump
            p2 = Pump('/dev/ttyAMA0')
            # D is for dispense, number is for volume in ml
            p2.send_cmd("D,2")
            print("dispensing 2ml acid")
        
        # Continuously Dispense Acid while button is held
        def startAcid(event):
            global running
            running = True
            # Starts thread to displaypH
            threading.Thread(target=continuousDispenseAcid).start()
        
        # Continuously Dispense Base while button is held
        def startBase(event):
            global running
            running = True
            # Starts thread to displaypH
            threading.Thread(target=continuousDispenseBase).start()       
        
        # Stops Continuous dispense by setting running variable to false   
        def stopDispense(event):
            global running
            running = False
            print("stopping dispense")
        
        # Dispenses 0.5ml at a time until running is set to False
        def continuousDispenseAcid():
            p2 = Pump('/dev/ttyAMA0')
            while(running == True):
                p2.send_cmd("D,0.5")
        # Dispenses 0.5ml at a time until running is set to False
        def continuousDispenseBase():
            p1 = Pump('/dev/ttyAMA1')
            while(running == True):
                p1.send_cmd("D,0.5")
        
        # Continuously Dispense Acid while button is held
        def startAcidReverse(event):
            global reverseRunning
            reverseRunning = True
            # Starts thread to displaypH
            threading.Thread(target=continuousReverseAcid).start()
        
        # Continuously Dispense Base while button is held
        def startBaseReverse(event):
            global reverseRunning
            reverseRunning = True
            # Starts thread to displaypH
            threading.Thread(target=continuousReverseBase).start()
        
        # Stops Continuous dispense by setting reverseRunning variable to false   
        def stopReverse(event):
            global reverseRunning
            reverseRunning = False
            print("stopping Reverse Dispensing")
        
        # Reverses 0.5ml at a time until reverseRunning is set to False
        def continuousReverseAcid():
            p2 = Pump('/dev/ttyAMA0')
            while(reverseRunning == True):
                p2.send_cmd("D,-0.5")
        # Reverses 0.5ml at a time until reverseRunning is set to False
        def continuousReverseBase():
            p1 = Pump('/dev/ttyAMA1')
            while(reverseRunning == True):
                p1.send_cmd("D,-0.5")
                
            
        # Dispense 2ml Acid Button
        button5 = Button(self, text='Dispense 2ml Acid ', command = dispense2mlAcid,bg='NavajoWhite2', font=("Arial Bold",20))
        button5.place(x=420,y=330)

        # Dispense 2ml Base Button
        button6 = Button(self, text='Dispense 2ml Base', command = dispense2mlBase,bg='NavajoWhite2', font=("Arial Bold",20))
        button6.place(x=420,y=380)
        
        # Dispense 1ml Acid Button
        button14 = Button(self, text='Dispense 1ml Acid ', command = dispense1mlAcid,bg='NavajoWhite2', font=("Arial Bold",20))
        button14.place(x=80,y=330)
        
        # Dispense 1ml Base Button
        button15 = Button(self, text='Dispense 1ml Base ', command = dispense1mlBase,bg='NavajoWhite2', font=("Arial Bold",20))
        button15.place(x=80,y=380)
        
        # Continuously Dispense Acid while button is held
        button7 = Button(self, text = "Hold: Dispense Acid ",bg='NavajoWhite2',font=("Arial Bold",20))
        button7.place(x=80,y=135)
        button7.bind('<ButtonPress-1>',startAcid)
        button7.bind('<ButtonRelease-1>',stopDispense)
        
        # Continuously Dispense Base while button is held
        button8 = Button(self, text = "Hold: Dispense Base",bg='NavajoWhite2',font=("Arial Bold",20))
        button8.place(x=480,y=135)
        button8.bind('<ButtonPress-1>',startBase)
        button8.bind('<ButtonRelease-1>',stopDispense)
        
        # Continuously Reverse Acid pump while button is held
        button9 = Button(self, text = "Hold: Reverse Acid  ",bg='NavajoWhite2',font=("Arial Bold",20))
        button9.place(x=80,y=185)
        button9.bind('<ButtonPress-1>',startAcidReverse)
        button9.bind('<ButtonRelease-1>',stopReverse)
        
        # Continuously Reverse Base pump while button is held
        button10 = Button(self, text = "Hold: Reverse Base  ",bg='NavajoWhite2',font=("Arial Bold",20))
        button10.place(x=480,y=185)
        button10.bind('<ButtonPress-1>',startBaseReverse)
        button10.bind('<ButtonRelease-1>',stopReverse)
    
        
class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
                
        
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    
        
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)
        
        # Page 1 Background Color
        p1.configure(bg='NavajoWhite3')
        # Page 2 Background Color
        p2.configure(bg='NavajoWhite3')
        # Page 3 Background Color
        p3.configure(bg='NavajoWhite3')
        # Page 4 Background Color
        p4.configure(bg='NavajoWhite3')
        # Page 5 Background Color
        p5.configure(bg='NavajoWhite3')
        
        #Buttons for controlling pH Limits
        button1 = Button(p1, text='  Up   ', command = p1.addToUpperLimit,bg='NavajoWhite2' )
        button1.place(x=650,y=120)
        button2 = Button(p1, text='Down', command = p1.subFromUpperLimit,bg='NavajoWhite2')
        button2.place(x=650,y=160)
        button3 = Button(p1, text='  Up   ', command = p1.addToLowerLimit,bg='NavajoWhite2')
        button3.place(x=650,y=270)
        button4 = Button(p1, text='Down', command = p1.subFromLowerLimit,bg='NavajoWhite2')
        button4.place(x=650,y=310)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        
        
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)


        b1 = tk.Button(buttonframe, text="    pH    ", command=p1.show)
        b2 = tk.Button(buttonframe, text="Temperature", command=p2.show)
        b3 = tk.Button(buttonframe, text="Humidity", command=p3.show)
        b4 = tk.Button(buttonframe, text="Maintenance", command=p4.show)
        b5 = tk.Button(buttonframe, text="Stats", command=p5.show)


        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")

        

        p1.show()

    
if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    #root.wm_geometry("800x480")
    # Title
    root.title("Garden Manager Alpha Test")
    root.minsize(width=800,height=480) #matched to Elemnent14 7" touchscreen display screen resolution

    root.mainloop()