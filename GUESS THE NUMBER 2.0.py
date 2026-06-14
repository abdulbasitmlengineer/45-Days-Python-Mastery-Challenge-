print("===================WELCOME TO GUESS NUMBER GAME=====================")

#-----------------------------------
def game():
	number = 1 
	user = int(input("TYPE THE NUMBER:        |"))
	number += 2
	while user != number:
		if user < number:
			user = int(input("TYPE AGAIN (HIGHER):     |"))
		elif user > number:
			user = int(input("TYPE AGAIN (LOWER):      |"))
	print("------------------------------------------------------------")
	print("YOU WIN .....")
	number += 2
	
	print("=====================================================")
	user_need = input("Play Again ???:(y\n)   ")
	if user_need == "y":
		number += 2
		while user != number:
			if user < number:
				user = int(input("TYPE AGAIN (HIGHER):     |"))
			elif user > number:
				user = int(input("TYPE AGAIN (LOWER):      |"))
				print("------------------------------------------------------------")
		print("YOU WIN .....")
		number += 2
		game()
	elif user_need == "n":
		print("ALLAH HAFIZ......")
game()	
