#!/usr/bin/env python3

def numFileWidth(num):
    filewidth = {
        '0' : 20,
        '1' : 20,
        '2' : 20,
        '3' : 20,
        '4' : 20,
        '5' : 20,
        '6' : 20,
        '7' : 20,
        '8' : 20,
        '9' : 20,
        '.' : 12,
        '-' : 20,
        'º' : 16,
        'F' : 20,
        'C' : 20
    }

    return filewidth[num]

def findFile(x):
    filename = {
        '0' : '0.txt',
        '1' : '1.txt',
        '2' : '2.txt',
        '3' : '3.txt',
        '4' : '4.txt',
        '5' : '5.txt',
        '6' : '6.txt',
        '7' : '7.txt',
        '8' : '8.txt',
        '9' : '9.txt',
        '.' : 'dot.txt',
        '-' : 'minus.txt',
        'º' : 'degree.txt',
        'F' : 'F.txt',
        'C' : 'C.txt'
    }
    return filename[x]

