# Pump.py
import serial
import sys
import time
import string 
from serial import SerialException

class Pump():
    
    # Constructor
    def __init__(self, usbport):
        
        self.usbport = usbport
    
    # Displays usbport
    def show(self):
        
        print("port is" + str(self.usbport))
    
    # send_cmd function
    def send_cmd(self, cmd):
        
        self.cmd = cmd
        
        ser = serial.Serial(self.usbport, 9600, timeout=0)
    
        # add carriage return
        buf = self.cmd + "\r" 
        try:
            ser.write(buf.encode('utf-8'))
            return True
        except SerialException as e:
            print ("Error, ", e)
            return None
    
    # read_line function
    def read_line():
	
        lsl = len(b'\r')
        line_buffer = []
        while True:
            next_char = ser.read(1)
            if next_char == b'':
                break
            line_buffer.append(next_char)
            if (len(line_buffer) >= lsl and
                    line_buffer[-lsl:] == [b'\r']):
                break
        return b''.join(line_buffer)
	
	# read_lines function
    def read_lines():
        """
        also taken from ftdi lib to work with modified readline function
        """
        lines = []
        try:
            while True:
                line = read_line()
                if not line:
                    break
                    ser.flush_input()
                lines.append(line)
            return lines
        
        except SerialException as e:
            print( "Error, ", e)
            return None	


