#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## CAESAR
## File description:
## Fixed XOR
##

import sys
from base64 import b64encode, b64decode

def helper():
    print("USAGE")
    print("\t./challenge02 input02.txt\n")
    print("DESCRIPTION\n")
    print("Write a program that takes a file containing two hexadecimal encoded buffers of equal (and only equal) length separated by a newline and produces their XOR combination.\n")
    exit(0)

def check_rigor():

    if len(sys.argv) < 2:
        print("Error: need more arguments ! Please ./challenge02 -h")
        exit(84)

    if len(sys.argv) > 2:
        print("Error: too many arguments ! Please ./challenge02 -h")
        exit(84)

    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            helper()


def fixed_xor(input_bytes_1, input_bytes_2):
    xord_bytes = bytearray()

    for b1, b2 in zip(input_bytes_1, input_bytes_2):
        xord_bytes += (bytes([b1 ^ b2]))
    return xord_bytes

def main():

    check_rigor()

    try:
        _filedata = sys.argv[1]
        _file = open(_filedata, "r")
    except:
        print("Error: no file or directory !")
        exit(84)
    
    data = _file.read()
    first_line = data.split('\n', 1)[0]
    second_line = data.split('\n', 2)[1]

    input_bytes_1 = bytes.fromhex(first_line)
    input_bytes_2 = bytes.fromhex(second_line)
    
    print(fixed_xor(input_bytes_1, input_bytes_2).hex().upper())

if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        sys.exit(84)
    else:
        sys.exit(0)
