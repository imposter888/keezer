#!/usr/bin/env python3

from re import findall
from os import system
from os import path
class OneThermometer:

    dev_file = '/sys/bus/w1/devices/'
    unit_preference = 'C' # 'C' (Celcius, default) or 'F' (Farinheight)

    def __init__ (self, device_location):
        if path.isfile(device_location) == False:
            print('File does not exist!')
            print('Setting default to:', self.dev_file)
        else:
            self.dev_file = device_location
        self.current_temp = None
        self.cieling_temp = None
        self.floor_temp = None

    def setTempC(self):
        self.unit_preference = 'C'
        return

    def setTempF(self):
        self.unit_preference = 'F'
        return

    def printTempPref(self):
        print("Unit Set:" + self.unit_preference +"º")
        return

    # Convert HEX to decimal
    # Accounts for negative value (2s completment)
    # * Assuming leading 2 HEX values are 'FF'
    # Variables:
    #   - hex_temp (string): holds value for incoming hex
    #   - bit (string): holds value for binary
    #   - temp
    def hexToDec(self, hex_temp):
        dec = 0
        temp = 0
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
            dec = int(hex_temp, 16)
        # return (int)
        return dec * 62.5

    def setTempHigh(self, high):
        if self.cieling_temp == None:
            self.cieling_temp = high
            return
        elif self.floor_temp > high:
            print("Temp is lower than 'High' setting!")
            print("'High Temp'not set")
            return -255
        print("'High' Temp set to:" + str(high))
        self.cieling_temp = high
        return

    def setTempLow(self, low):
        if self.floor_temp == None:
            self.floor_temp = low
            return
        elif self.cieling_temp < low:
            print("Temp is higher than 'High' temp setting!")
            print("'Low' Temp not set")
            return -255
        print("'Low' Temp set to:" + str(low))
        self.floor_temp = low
        return

    def setDeviceLocation(self, device_location):
       # Read file
        try:
            if path.isfile(device_location):
                temp_file = open(device_location, 'r')
            else:
                print("Not a file! Returning")
                return False
        # Handle file if it doesn't exist
        except OSError:
            print("File does not exist!")
            return False
        self.dev_file = device_location
        temp_file.close()
        print("Device set to:", self.dev_file)
        return True
    
    # Read the RAW t=##### number
    # Include the '-' if value is negative. Ex: -#####
    # Variables:
    #   - self (object): of OneThermometer
    #   - forc (string): Specifies return of Farinheight ("F) or Celcius ("C")
    def readTemp (self):
        temp_file = ''
        hex_line = ''
        match = ''
        temp = ''
        try:
            if path.isfile(self.dev_file):
                temp_file = open(self.dev_file, 'r')
            else:
                print("Not a file! Returning")
                return -255
        # Handle file if it doesn't exist
        except OSError:
            print("File does not exist!")
            return -254     
        # Take input of first line of w1_slave file
        # Look for 'YES' if both lines match, or 'NO' if they don't
        hex_line = temp_file.readline().upper()
        match = findall("\w*$", hex_line)[0]
        hex_line = hex_line[3:5] + hex_line[:2]
        if match == 'NO':
            print("Readings do not match")
            return -253
        # Convert hex to decimal and divide by 1000 for float (##### -> ##.###)
        # Default unit = Celcius
        temp = self.hexToDec(hex_line) / 1000
        if self.unit_preference == 'F':
            temp = (temp * 1.8) + 32
        # return (float)
        self.current_temp = temp
        return temp


