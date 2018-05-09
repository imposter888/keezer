#!/usr/bin/env python3
import num_files
import os
import temp
from re import findall

def welcomeMessage():
    row, col = shellSize()
    w_row, w_col = 8, 75
    line = ''
    os.system('clear')
    for i in range(int(row/2)-int(w_row/2)):
        os.system('echo')
    welcome = open('./fonts/welcome.txt', 'r')
    for i in range(w_row):
        line = ''
        line += (' ' * (int(col/2) - int(w_col/2))) + welcome.readline()[:-2]
        print(line)
    welcome.close()
    return

def displayText(text):
    tot_width = 0
    row, col = shellSize()
    t_row = 16
    files = [open('./fonts/'+num_files.findFile(i)) for i in text]
    for i in text:
        tot_width += num_files.numFileWidth(i) + 1
    os.system('clear')
    for i in range(int((row - t_row)/2)):
        os.system('echo')
    for i in range(16):
        line = ' ' * int((col - tot_width)/2)
        for num in files:
            line += num.readline()[:-2] + ' '
        print(line)
    return

def logTemp(temp, pref):
    line = 'echo "' + temp + ',\t"$(date +%s)",\t' + pref + ',\t"$(date +%D+%T) >> ./logs/templog.txt'
    os.system(line)
    return

def shellSize():
    line = os.popen('stty size').read()
    row = int(findall(r'^\d*', line)[0])
    col = int(findall(r'\d*$', line)[0])
    return row, col

def main():
    key = ''
    filename = '/sys/bus/w1/devices/28-01161b0873ee/w1_slave'
    shell_row, shell_col = shellSize()
    welcomeMessage()
    therm = temp.OneThermometer(filename)
    therm.setTempF()
    os.system('sleep 2')
    while(key == ''):
        temp = str('%.2f' % therm.readTemp())
        displayText(temp)
        logTemp(temp, therm.unit_preference)
        os.system('sleep 5')
    # Code goes here


if __name__ == "__main__":
    main()
