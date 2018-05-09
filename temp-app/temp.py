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

        self.unit_preference = 'C' # 'C' (Celcius) or 'F' (Farinheight)
        self.current_temp = None
        self.cieling_temp = 125
        self.floor_temp = -55

    def setTempC(self):
        if self.unit_preference == 'F':
            self.cieling_temp = (self.cieling_temp - 32) * (5/9)
            self.floor_temp = (self.floor_temp - 32) * (5/9)
        self.unit_preference = 'C'
        return

    def setTempF(self):
        if self.unit_preference == 'C':
            self.cieling_temp = (self.cieling_temp * 9/5) + 32
            self.floor_temp = (self.floor_temp * 9/5) + 32
        self.unit_preference = 'F'
        return

    def printTempPref(self):
        print("Unit Set: " + self.unit_preference +"º")
        return

    def printTempHigh(self):
        print("Cieling Temp: " + str(self.cieling_temp) + str(self.unit_preference) + "º")

    def printTemp(self):
        print("Floor Temp: " + str(self.floor_temp) + str(self.unit_preference) + "º")

    # Function: Input HEX (string) and return decimal (float)
    #
    # Accounts for negative value in binary (2s completment)
    # * Assuming leading 2 HEX values are 'FF'
    # Input:
    #   * hex_temp (string): contains 4 string HEX
    # Variables:
    #   - hex_temp (string): holds value for incoming hex
    #   - bit (string): binary string iterable
    #   - temp (string): contains binary string for 2s compliment conversion
    #
    def hexToDec(self, hex_temp):
        dec = 0
        temp = ''
        # Convert negative value if leading byte is 'FF'
        if hex_temp[:1] == 'F':
            hex_temp = bin(int(hex_temp, 16))[2:]
            for bit in hex_temp:
                if bit == '1':
                    temp += '0'
                elif bit == '0':
                    temp += '1'
            temp = bin(int(temp, 2))[2:]
            dec = -int(bin(int(temp,2) + int('1',2))[2:], 2)
        else:
            dec = int(hex_temp, 16)
        # return (float)
        return dec * 62.5

    # Function: Set cieling temperature
    #
    # Input:
    #   * high (int): contains cieling temp
    #
    def setTempHigh(self, high):
        if self.unit_preference == 'C' and high <= 125 and self.floor_temp <= high:
            self.cieling_temp = high
        elif self.unit_preference == 'F' and high <= 260 and self.floor_temp <= high:
            self.cieling_temp = high
        else:
            print("'High' temp not set!")
            return False
        print("'High' temp set to: " + str(self.cieling_temp) + "º")
        return True

    def setTempLow(self, low):
        if self.unit_preference == 'C' and low >= -55 and self.cieling_temp >= low:
            self.floor_temp = low
        elif self.unit_preference == 'F' and low >= -64 and self.cieling_temp >= low:
            self.floor_temp = low
        else:
            print("'Low' temp not set!")
            return False

        print("'Low' temp set to: " + str(self.floor_temp) + "º")
        return True

    def setDeviceLocation(self, device_location):
       # Read file
        try:
            print("Device Location target:", device_location)
            if path.isfile(device_location):
                print("File Found!")
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

if __name__ == "__main__":
    app = OneThermometer('/sys/bus/w1/devices/28-/w1_slave')
    print('attempting to set Device Location...')
    app.setDeviceLocation('/sys/bus/w1/devices/28-01161b0873ee/w1_slave')
    print(app.readTemp())
    print(app.setTempF())
    print(app.readTemp())
