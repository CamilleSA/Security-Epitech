#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## CAESAR
## File description:
## AES IN ECB MODE
##

import sys

def helper():
    print("USAGE")
    print("\t./challenge07 input07.txt\n")
    print("DESCRIPTION\n")
    print("You are to decrypt a hexadecimal version of a text encrypted using repeating-key XOR, contained in a file given as argument\n")
    exit(0)

def check_rigor():

    if len(sys.argv) < 2:
        print("Error: need more arguments ! Please ./challenge07 -h")
        exit(84)

    if len(sys.argv) > 2:
        print("Error: too many arguments ! Please ./challenge07 -h")
        exit(84)

    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            helper()


def main():
    
    check_rigor()

    try: 
        _filedata = sys.argv[1]
        _file = open(_filedata, "r")
    except:
        print("Error: no file or directory !")
        exit(84)

    data = _file.read()

    if data == "":
        print("Error: the file is not valid !")
        exit(84)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        sys.exit(84)
    else:
        sys.exit(0)