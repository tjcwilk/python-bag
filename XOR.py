#!/usr/bin/python

#
# TPyTools - XOR File
#	DESCRIPTION
#		Simple XOR over a file
#

from itertools import izip, cycle


class XOR:

	def fileXORsingleByte(self, inputFile, outputFile):
		#
		# XORs file with single byte key
		#

		inData = open(inputFile, 'rb')
		outData = open(outputFile, 'w+b')

		byte = inData.read(1)

		counter = 0
		while byte != "":
			if counter % 2 == 1:
				# XOR with 3 (ASCII) (0x33)
				byte = byte ^ 0x33
			outData.write('%c' % byte)
			byte = inData.read(1)
			counter += 1
		outData.close()

	def nullPreservingXOR(input_char,key_char)
		if (input_char == key_char or input_char == chr(0x00)):
			return input_char
		else:
			return chr(ord(input)char) ^ ord(key_char))



	def fileXORKey(self, inputFile, outputFile):
		#
		# XORs file with a key
		#

		inData = open(inputFile, 'rb')
		outData = open(outputFile, 'w+b')

		key = [0x56, 0x55, 0x54]
		counter = 0
		byte = inData.read(1)
		while byte != "":
			byte = ord(byte)
			byte = byte ^ key[counter]
			counter += 1
			if counter > len(key):
				counter = 0
			outData.write('%c' % byte)
			byte = inData.read(1)
		outData.close()

	def xor(self, data, key):
		return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))


if __name__ == "__main__":
	
	key = "\x01\x02\x03\x04"
	data = "ThisIsASecretString"
	#data = bytearray(open('myfile.bin', 'rb').read())

	myXOR = XOR()

	print "Original Data::" + data
	encrypted = myXOR.xor(data, key)
	print "Encrypted data::" + encrypted
	decrypted = myXOR.xor(encrypted, key)
	print "Decrypted data::" + decrypted

