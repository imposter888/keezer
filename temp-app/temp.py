#!/usr/bin/env python3

from re import findall
from os import system
from os import popen

class OneThermometer:

    self.dev_loc = '/sys/bus/w1/devices/'

    def __init__ (self, device_location):
        try:
            open(device_location, 'r')
        except FileNotFoundError():
            print('Device file not found!')
            raise AssertionError
        self.current_temp = None
        self.cieling_temp = None
        self.floor_temp = None

    # Read the RAW t=##### number
    # Include the '-' if value is negative. Ex: -#####
    def readRAW (self):
        # Read file
        if os.is_file(self.temp_file)
            temp_file = open(self.device_location, 'r')
        # Handle file if it doesn't exist
        except FileDoesNotExist():
            print("File does not exist!")
            return -255
            
        # Take input of first line of w1_slave file
        # Look for 'YES' if both lines match, or 'NO' if they don't
        line = temp_file.readline().upper()
        match = findall("\w*$", line)[0]

        if match == 'NO':
            print("Readings do not match")
            return -254
        
        if line[3:5] == 'FF':
            # Compute negative (2s complement in HEX)
            
            

        # Convert hex to decimal
        self.current_temp =  int(str(findall("=-*\d*$", temp_file.readline()))
