#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## CAESAR
## File description:
## Implement CBC mode
##

import sys

def helper():
    print("USAGE")
    print("\t./challenge09 input09.txt\n")
    print("DESCRIPTION\n")
    print("Make this program decrypt the ciphertext using the provided key and IV, and print on the standard output the obtained plaintext in base64, followed by a newline.\n")
    exit(0)

def check_rigor():

    if len(sys.argv) < 2:
        print("Error: need more arguments ! Please ./challenge09 -h")
        exit(84)

    if len(sys.argv) > 2:
        print("Error: too many arguments ! Please ./challenge09 -h")
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