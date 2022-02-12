#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## CAESAR
## File description:
## IMPLEMENT REPEATING-KEY XOR
##

import sys
import codecs
import base64

def helper():
    print("USAGE")
    print("\t./challenge05 input05.txt\n")
    print("DESCRIPTION\n")
    print("In repeating-key XOR, a key is XORed sequentially (byte by byte) to the plaintext, repeating from the first index when the key is exhausted.\n")
    exit(0)


def check_rigor():

    if len(sys.argv) < 2:
        print("Error: need more arguments ! Please ./challenge04 -h")
        exit(84)

    if len(sys.argv) > 2:
        print("Error: too many arguments ! Please ./challenge04 -h")
        exit(84)

    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            helper()


def repeating_key_xor(message, key):

    xord_bytes = bytearray()
    index = 0

    for byte in message:
        xord_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1

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

    if data == "":
        print("Error: the file is not valid !")
        exit(84)

    input_byte_1 = data.split('\n', 1)[0]
    input_byte_2 = data.split('\n', 2)[1]

    message_hex = ''.join(input_byte_2).encode()
    key_hex = ''.join(input_byte_1).encode()

    message_text = codecs.decode(message_hex, 'hex')
    key_text = codecs.decode(key_hex, 'hex')
    
    ciphertext = repeating_key_xor(message_text, key_text)
    print(ciphertext.hex().upper())

    
if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        sys.exit(84)
    else:
        sys.exit(0)