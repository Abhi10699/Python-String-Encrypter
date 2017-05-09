#importing Modules
import os
import random
import sys
from os import system

randomNumbersList = []
randomNumber = random.randint(0,128)
mainStringData = 'Abhi'
# Encryption

def encrypt(string):
	global mainStringData
	mainStringData = string
	counter = 0
	# Defining the lists
	charList = []
	newList = []


	# Variables
	global randomNumber
	# Fill the data in a list
	for char in string:
		try:
			charList.append(char)
			pass
		except Exception as e:
			print e
	print charList
	# Change their ascii values

	for data in charList:
		charList[counter] = chr(ord(data) + randomNumber)
		print "Random Number: ",randomNumber
		print "ORD Data: ",ord(data)
		print "Encrypted :",chr(ord(data) + randomNumber)
		counter += 1 
		
	for datas in charList:
		sys.stdout.write(datas)
		system('echo -n %s >> encrypted.txt' %(datas))

	print "\n"


	# print charList
def decrypt(encryptedDataFile):
	decCounter = 0
	decryptedData = []
	global randomNumber
	with open(encryptedDataFile) as f:
		for i in f.read():
			decryptMath = ord(i) - randomNumber
			decryptedData.append(chr(decryptMath))
        		
	for text in decryptedData:
		sys.stdout.write(text)
		system('echo -n %s >> decrypted.txt' %(text))

	print "\n"
    


if __name__ == '__main__':

	encrypt(sys.argv[1])
	print mainStringData
	print randomNumber
	decrypt('encrypted.txt')
	

