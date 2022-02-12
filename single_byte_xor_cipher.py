#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## CAESAR
## File description:
## SINGLE-BYTE XOR CIPHER
##

import sys
import string
import codecs


def helper():
    print("USAGE")
    print("\t./challenge03 input03.txt\n")
    print("DESCRIPTION\n")
    print("Code a program that finds the single byte key that has been XORed against a given string. The input is a hexadecimal encoded file. The byte used for the XOR operation should be printed on the standard output in capital hexadecimal..\n")
    exit(0)


def check_rigor():

    if len(sys.argv) < 2:
        print("Error: need more arguments ! Please ./challenge03 -h")
        exit(84)

    if len(sys.argv) > 2:
        print("Error: too many arguments ! Please ./challenge03 -h")
        exit(84)

    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            helper()



def getLanguageScore(input_bytes):

    DicFrequency = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }

    count_scores = 0
    for byte in input_bytes.lower():
        for i in DicFrequency:
            if chr(byte) == i:
                count_scores += DicFrequency[i]
    return count_scores


def fixed_xor(input_bytes, char_value):

    xord_bytes = bytearray(len(input_bytes))

    for byte in range(len(input_bytes)):
        xord_bytes[byte] += input_bytes[byte] ^ char_value[byte]

    return xord_bytes


def single_byte_xor_cipher(hexstring):

    score = 0

    if (hexstring == ""):
        print("Error: the string is empty !")
        exit(84)

    ciphertext = bytearray.fromhex(hexstring)

    for key_value in range(256):
        char_value = [key_value] * len(ciphertext)
        plaintext = bytes(fixed_xor(ciphertext, char_value))
        count_scores = getLanguageScore(plaintext)

        if score == 0 or count_scores > score:
            score = count_scores
            res = bytes([key_value])

    print(codecs.decode(codecs.encode(res, 'hex'), 'utf-8').upper())


def main():

    check_rigor()
    
    try:
        _filedata = sys.argv[1]
        _file = open(_filedata, "r")
    except:
        print("Error: no file or directory !")
        exit(84)

    data = _file.read().strip()

    single_byte_xor_cipher(data)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        sys.exit(84)
    else:
        sys.exit(0)

