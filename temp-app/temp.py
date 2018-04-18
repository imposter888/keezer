#!/usr/bin/env python3

from re import findall
from os import system
from os import popen

class OneThermometer:

    self.dev_file = '/sys/bus/w1/devices/'

    def __init__ (self, device_location):
        try:
            os.is_device_location, 'r')
        except FileNotFoundError():
            print('Device file not found!')
            raise AssertionError
        
        self.unit_preference = None # 'C' (Celcius) or 'F' (Farinheight)
        self.current_temp = None
        self.cieling_temp = None
        self.floor_temp = None

    # Convert HEX to decimal
    # Accounts for negative value (2s completment)
    # * Assuming leading 2 HEX values are 'FF'
    # Variables:
    #   - hex_temp (string): holds value for incoming hex
    #   - bit (string): holds value for binary
    #   - temp
    def hexToDec(hex_temp):
        dec = 0
        
        # Convert negative value if leading byte is 'FF'
        if hex_temp[:2] == 'FF':
            hex_temp = bin(int(hex_temp, 16))[2:]
            # Flip bits
            for bit in hex_temp:
                if bit == '1':
                    temp += '0'
                elif bit == '0':
                    temp += '1'
            temp = bin(int(temp, 2))[:2]
            # Add 1 to binary string, convert to dec, make negative (int)
            dec = -int(bin(int(temp,2) + int('1',2))[2:], 2)
        else:
            # Positive temp from hex to dec (int)
            dec = int(temp, 16)

        # return (int)
        return dec


    # Read the RAW t=##### number
    # Include the '-' if value is negative. Ex: -#####
    # Variables:
    #   - self (object): of OneThermometer
    #   - forc (string): Specifies return of Farinheight ("F) or Celcius ("C")
    def readRAW (self, forc):
        temp_file = ''
        hex_line = ''
        match = ''
        temp = ''

        # Read file
        if os.is_file(self.dev_file)
            __temp_file = open(self.device_location, 'r')
        # Handle file if it doesn't exist
        except FileDoesNotExist():
            print("File does not exist!")
            return -255
            
        # Take input of first line of w1_slave file
        # Look for 'YES' if both lines match, or 'NO' if they don't
        hex_line = temp_file.readline().upper()
        match = findall("\w*$", line)[0]
        hex_line = hex_line[3:5] + hex_line[:2]
        
        if match == 'NO':
            print("Readings do not match")
            return -254

        # Convert hex to decimal and divide by 1000 for float (##### -> ##.###)
        # Default unit = Celcius
        temp = hexToDec(hex_line) / 1000
        
        if forc.upper() == 'F':
            

        
