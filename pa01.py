"""
/*============================================================================
| Assignment: pa01 - Encrypting a plaintext file using the Hill cipher
|
| Author: Samuel Woodstock
| Language: python
|
| or python -> python3 pa01.py kX.txt pX.txt
| where kX.txt is the keytext file
| and pX.txt is plaintext file
| Note:
| All input files are simple 8 bit ASCII input
| All execute commands above have been tested on Eustis
|
| Class: CIS3360 - Security in Computing - Fall 2023
| Instructor: McAlpin
| Due Date: October 8th, 2023
+===========================================================================*/
"""
import sys
if (len(sys.argv) <= 2):
    raise RuntimeError("Incorrect usage, to run enter python ./pa01.py <keytext file path> <plaintext filepath>")
kX: str = sys.argv[1]
pX: str = sys.argv[2]
vectorLength: int = 0

def processKeymatrix(keyfile) -> list:
    keymatrix: list = []
    currentLine: int = 0
    with open(keyfile) as keytext:
        for line in keytext:
            if currentLine == 0:
                global vectorLength
                vectorLength = int(line)
                currentLine += 1
            else:
                keymatrix.append(line.split())
    return keymatrix

def stringifyKeymatrix(keymatrix) -> str:
    kXString = ""
    for row in keymatrix:
        for element in row:
            kXString += (element + "   ")
        kXString += "\n "
    print("\nKey matrix:\n", kXString)
    return kXString

def processPlaintext(plaintextFile) -> list:
    plaintext = ''
    with open(pX, 'r') as file:
        rawPx = file.read()
        for char in rawPx:
            if char.isalpha():
                plaintext += char.lower()
    padding = len(plaintext) % vectorLength
    if padding != 0:
        for i in range(vectorLength - padding):
            plaintext += 'x'
    return plaintext
    


keymatrix = processKeymatrix(kX)            
stringifyKeymatrix(keymatrix)
plaintext = processPlaintext(pX)






"""
/*=============================================================================
| I [your name] ([your NID]) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+=============================================================================*/
"""