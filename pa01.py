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
class HillCipher:
    def __init__(self, vectorLength: int) -> None:
        self.vectorLength = vectorLength
        self.alphaToNum = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
            'i': 8,
            'j': 9,
            'k': 10,
            'l': 11,
            'm': 12,
            'n': 13,
            'o': 14,
            'p': 15,
            'q': 16,
            'r': 17,
            's': 18,
            't': 19,
            'u': 20,
            'v': 21,
            'w': 22,
            'x': 23,
            'y': 24,
            'z': 25
        }
        self.numToAlpha = {
            0: 'a',
            1: 'b',
            2: 'c',
            3: 'd',
            4: 'e',
            5: 'f',
            6: 'g',
            7: 'h',
            8: 'i',
            9: 'j',
            10: 'k',
            11: 'l',
            12: 'm',
            13: 'n',
            14: 'o',
            15: 'p',
            16: 'q',
            17: 'r',
            18: 's',
            19: 't',
            20: 'u',
            21: 'v',
            22: 'w',
            23: 'x',
            24: 'y',
            25: 'z'   
        }

    def processKeymatrix(self, keyfile) -> list:
        keymatrix: list = []
        currentLine: int = 0
        with open(keyfile) as keytext:
            for line in keytext:
                if currentLine == 0:
                    self.vectorLength = int(line)
                    currentLine += 1
                else:
                    keymatrix.append(line.split())
        return keymatrix

    def stringifyKeymatrix(self, keymatrix) -> str:
        kXString = ""
        for row in keymatrix:
            for element in row:
                kXString += (element + "   ")
            kXString += "\n "
        print("\nKey matrix:\n", kXString)
        return kXString

    def processPlaintext(self, plaintextFile) -> list:
        plaintext = ''
        with open(pX, 'r') as file:
            rawPx = file.read()
            for char in rawPx:
                if char.isalpha() and char.isascii():
                    plaintext += char.lower()
        padding = len(plaintext) % self.vectorLength
        if padding != 0:
            for i in range(self.vectorLength - padding):
                plaintext += 'x'
        return plaintext

    def stringifyPlaintext(self, plaintext) -> str:
        #break string into lines of length 80 characters
        plaintextString = ""
        for i in range(len(plaintext)):
            if i % 80 == 0:
                plaintextString += "\n"
            plaintextString += plaintext[i]
        print("\nPlaintext:", plaintextString)
        return plaintextString
    
    def splitPlaintext(self, plaintext) -> list:
        plaintextVector = []
        for i in range(len(plaintext)):
            if i % self.vectorLength == 0:
                plaintextVector.append(plaintext[i:i+self.vectorLength])
        return plaintextVector
    
    def encrypt(self, plaintextVector, keymatrix):
        numValues = []
        for pV in plaintextVector:
            for kV in keymatrix:
                numValues.append(str(self.multiplyVector(pV, kV)))       
        cipherText = ""
        for num in numValues:
            cipherText += self.numToAlpha[int(num)]
        return cipherText
            
    def multiplyVector(self, pV, kV):
        result = 0
        for i in range(len(pV)):
            result += self.alphaToNum[pV[i]] * int(kV[i])
        return result % 26
    
    def stringifyCiphertext(self, ciphertext) -> str:
        #break string into lines of length 80 characters
        ciphertextString = ""
        for i in range(len(ciphertext)):
            if i % 80 == 0:
                ciphertextString += "\n"
            ciphertextString += ciphertext[i]
        print("\nCiphertext:", ciphertextString)
        return ciphertextString
        


"""
Runtime code
"""
if (len(sys.argv) <= 2):
    raise RuntimeError("Incorrect usage, to run enter python ./pa01.py <keytext file path> <plaintext filepath>")

kX: str = sys.argv[1]
pX: str = sys.argv[2]  
 
hill_cipher = HillCipher(0)

keymatrix = hill_cipher.processKeymatrix(kX)           
hill_cipher.stringifyKeymatrix(keymatrix)
plaintext = hill_cipher.processPlaintext(pX)
hill_cipher.stringifyPlaintext(plaintext)
plaintextVector = (hill_cipher.splitPlaintext(plaintext))
cipherText = hill_cipher.encrypt(plaintextVector, keymatrix)
hill_cipher.stringifyCiphertext(cipherText)


"""
/*=============================================================================
| I Samuel Woodstock sa941331 affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+=============================================================================*/
"""