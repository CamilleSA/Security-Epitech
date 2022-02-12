#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## CAESAR
## File description:
## DETECT AES IN ECB MODE
##

import sys

def helper():
    print("USAGE")
    print("\t./challenge08 input08.txt\n")
    print("DESCRIPTION\n")
    print("Write a program able to detect it and that outputs the corresponding line number.\n")
    exit(0)

def check_rigor():

    if len(sys.argv) < 2:
        print("Error: need more arguments ! Please ./challenge08 -h")
        exit(84)

    if len(sys.argv) > 2:
        print("Error: too many arguments ! Please ./challenge08 -h")
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