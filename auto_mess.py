import getpass
import time
import os
import pyautogui

from rich.tree import Tree
from rich import print

user = getpass.getuser()
curdir = os.getcwd()
print(" ___________________________________\n choose a text file")
x = os.listdir()
tree = Tree("[red1]" + curdir, guide_style="blue")
for i in x:
    tree.add("[cyan1]" + str(i))
print(" ", tree, "\n exit")
user = getpass.getuser()
while True:
	print(" ___________________________________" + "\n __ " + curdir )
	command = input("(__" + user + "___: ")
	if command in x:
		print(" User has four seconds to focus on a message box at the beginning,\n and 3 seconds every message sent. Starting now")
		time.sleep(4)
		#Opening the file with absolute path
		word = open(command, 'r')
		word.readline()
		for i in word:
			#read file
			print(i)
			time.sleep(2)
			#print(i)
			pyautogui.typewrite(i)
			pyautogui.press('enter')
		# Closing the file after reading
		word.close()
		print(" File iteration finished")
		break
	
	elif command == "exit":
		os.system('cls')
		break