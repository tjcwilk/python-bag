import string
import base64

def normalBase64:
	string = "fdgsetguehgfhfdjhdghjfjhdkjdjhv"
	print base64.decodestring(string)



def base64ModifiedAlphabet:
	s = ""
	custom = "9ZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012345678+/"
	Base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

	ciphertext = "fhj4hfjf5jjf"

	for ch in ciphertext:
		if( ch in Base64):
			s = s+ Base64[string.find(custom, str(ch))]
		elif (ch == '='):
			s += '='

	result = base64.decodestring(s)