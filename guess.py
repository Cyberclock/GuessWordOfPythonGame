print("\nWelcome to the guessing word of python game")

import time
time.sleep(2)

print("You have 5 times to win the game")

import time
time.sleep(2)

print("Let's play the game\n")

import time
time.sleep(2)
import os 
os.system('pause')

word = "string"
guess = ""
guess_number = 0
guess_limit = 5

while guess != word and guess_number < guess_limit:
	guess = str(input("\nEnter the word : "))
	guess_number += 1
	if guess != word:
		print("Opssssss -_-")
		print("Try again")
	elif guess == word:
		print("\nYou WIN\n")
		break
else:
	print("\nyou LOSE\n")


import os 
os.system('pause')