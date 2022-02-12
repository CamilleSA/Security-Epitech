#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## CAESAR
## File description:
## Fixed XOR
##

import sys
import string
from base64 import b64encode, b64decode

def helper():
    print("USAGE")
    print("\t./challenge01 input01.txt\n")
    print("DESCRIPTION\n")
    print("Make a program that converts the content of the file given as first argument from hexadecimal to base64 and prints it on the standard output.\n")
    exit(0)


def check_rigor():

    if len(sys.argv) < 2:
        print("Error: need more arguments ! Please ./challenge01 -h")
        exit(84)

    if len(sys.argv) > 2:
        print("Error: too many arguments ! Please ./challenge01 -h")
        exit(84)

    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            helper()
    
def hex_to_base64():

    _filedata = sys.argv[1]

    try:
        _file = open(_filedata, "r").read()
    except:
        print("Error: no file or directory !")
        exit(84)

    if (len(_file) <= 0):
        print("Error File: File is empty !")
        exit(84)

    
    if _file.islower():
        print("Error File: the data file must be only capital letter !")
        exit(84)

    try:
        b64 = b64encode(bytes.fromhex(_file)).decode()
        print(b64)
    except ValueError:
        print("Error File: Is not convertible !")
        exit(84)


def main(args):
    
    check_rigor()
    hex_to_base64()

if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as error:
        sys.exit(84)
    else:
        sys.exit(0)
