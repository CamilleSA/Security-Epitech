
#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## CAESAR
## File description:
## DETECT SINGLE-BYTE XOR
##

import sys

def helper():
    print("USAGE")
    print("\t./challenge04 input04.txt\n")
    print("DESCRIPTION\n")
    print("Given a file containing one hex-encoded string per line, among which one has been encrypted by a singlebyte XOR, write a program that detects this string, decrypts it (in the 3rd challenge fashion) and prints the key used to encrypt it in hexadecimal, prefixed with the line number.\n")
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
        count_scores += DicFrequency.get(chr(byte), 0)

    return count_scores

def fixed_xor(input_bytes, char_value):

    xord_bytes = bytearray()
    for byte in input_bytes:
        xord_bytes += bytes([byte ^ char_value])
    return xord_bytes

def detect_single_byte(hexstring, lineNb):

    if (hexstring == ""):
        print("Error: the string is empty !")
        exit(84)

    ciphertext = bytes.fromhex(hexstring)

    listPossibilities = []

    for key_value in range(256):
        listPossibilities.append((getLanguageScore(fixed_xor(ciphertext, key_value)),key_value, lineNb))

    res = max(listPossibilities, key = lambda i : i[0])

    return res

def main():

    check_rigor()

    try:
        _filedata = sys.argv[1]
        _file = open(_filedata, "r")
    except:
        print("Error: no file or directory !")
        exit(84)
    
    lines = _file.read().splitlines()
    listval = []

    for line in lines:
        listval.append(detect_single_byte(line, lines.index(line)))
    
    res = max(listval, key = lambda i : i[0])
    print(res[2], str(hex(res[1]))[2:]).upper()

       
if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        sys.exit(84)
    else:
        sys.exit(0)
