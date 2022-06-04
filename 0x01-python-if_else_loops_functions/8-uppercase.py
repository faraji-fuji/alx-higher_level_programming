#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    newStr = ""
    for char in str:
        if islower(char):
            newChar = ord(char) - 32
            newStr += chr(newChar)
        else:
            newStr += char
    print("{}".format(newStr))
