#importing Modules
import os
import random
import sys
from os import system

def encrypt(string):

	counter = 0
	charList = []
	newList = []
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
		charList[counter] = chr(ord(data) + random.randint(0,128))
		counter += 1 
	
		
	for datas in charList:
		sys.stdout.write(datas)
		system('echo -n %s >> encrypted.txt' %(datas))

	print "\n"

		
        
	# print charList


if __name__ == '__main__':
	encrypt(sys.argv[1])

	
