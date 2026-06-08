print("=============== PROGRAMMERS ATM SYSTEM ================")
balance = 1000
Attempts = 4
pin = 1234

user_name = input("Type your Name:                        |")

user_pin = int(input("Type your 4 Digit pin:                 |"))

while user_pin != pin:

	Attempts -= 1
	user_pin = int(input(f"Type your 4 Digit pin:({Attempts} Attempts Left)|"))
	if Attempts <= 1 and user_pin != pin:
		print("Your Account Is Blocked....")
		break
else:
		user_need = input("Deposit Or Withdraw (d/w):             |")
		if user_need == "d":
			print("============= Deposit ================")
			amount = int(input("Type Amount:                          |"))
			balance = amount + balance
			print(f"Your Amount was Successfully Deposited...\nYour Balance {balance}")
		elif user_need == "w":
			print("============= Withdraw ================")
			withdraw = int(input("Type Amount:               |"))
			if withdraw > balance or withdraw <= 0:
				print("Insufficient Balance")
			else:
			  	balance = balance - withdraw
			  	print(f"Withdrawal Successfully\nYour Balance {balance}")
			
	

