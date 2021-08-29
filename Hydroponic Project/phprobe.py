#phprobe.py
from MCP3008 import MCP3008
import time

# Outputs Applied voltage and pH readings
def getph():
    adc = MCP3008()
    value = adc.read( channel = 0 ) # You can of course adapt the channel to be read out

    #prints voltage to two sig figs
    print("Applied voltage: %.2f" % (value / 1023.0 * 3.3) )

    voltage = value / 1023.0 * 3.3
        
    #Equation to convert voltage to pH
    pH = (-5.6548*voltage)+15.509

    #print pH to two sig figs
    print("pH is: %.2f" % (pH))
        
    return pH
    
getph()
