#!/usr/bin/env python3
import numbers
import os
import temp
from re import findall

def welcomeMessage():
    os.system('clear')

def displayTemp(therm):
    temp = therm.readTemp()
    files = [open(numbers.findFile(n)) for i in temp]

def shellSize():
    line = os.system('stty size').read()
    row = findall(r'^\d*', line)[0]
    col = findall(r'\d*$', line)[0]
    return row, col

def main():
    shell_row, shell_col = shellSize()
    welcomeMessage()
    
    # Code goes here


if __name__ == "__main__":
    main()
