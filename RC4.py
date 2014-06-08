#!/usr/bin/python

#
# TPyTools - RC4
#   DESCRIPTION
#       Simple RC4 implementation in python
#

import struct

class RC4:
    def __init__(self, InitializeKeyStream = []):
        #Place the keystream in the following array
        #The following is just an example of a keystream
        if InitializeKeyStream == []:
             self.keystream = [0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xCD, 0xEF]
        else:
             self.keystream = InitializeKeyStream

        self.state = range(256)
        length = len(self.keystream)
        x = 0
        for i in range(256):
            #Randomization step
            x = (self.keystream[i % length] + self.state[i] + x) & 0xFF

            #Swap the array index i and x in the "state" array
            self.state[i], self.state[x] = (self.state[x], self.state[i])

    
    def crypt(self, string):
        #Create an array filled with 0's the same size as the length
        #of the string
        output = [0] * len(string)

        #Change the string into an array of numbers
        string = struct.unpack('%dB' % len(string), string)

        #Copy the keystream over to a local variable
        keys = [i for i in self.state]

        #Begin PRGA
        x = 0 ; y = 0
        for i, character in enumerate(string):
            x = (x + 1) & 0xFF
            y = (y + keys[x]) & 0xFF
            keys[x], keys[y] = (keys[y], keys[x])
            output[i] = character ^ keys[(keys[x] + keys[y]) & 0xFF]

        #Change the numbers into a string
        return struct.pack('%dB' % len(output), *output)


if __name__ == "__main__":

    # Create object and Set key
    crypto = RC4([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07])

    # Perform crypt
    message = "SecretMessage"
    print "Plaintext message::" + message
    cyphertext = crypto.crypt(message)
    print "Ciphertext::" + cyphertext
    decrypted = crypto.crypt(cyphertext)
    print "DecryptedText::" + decrypted


