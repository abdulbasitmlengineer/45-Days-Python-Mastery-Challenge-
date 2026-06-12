print("=======================================================               ")
print("================== 🪳 CJP ATM 🍹 ====================")
name = "basit"
balance = 5800
attempts = 4
pin = 1234

#-------------------------------------------------------
user_name = input("\nType Your Name :|")
user_pin = int(input("Type The Pin :  |"))

#-------------------------------------------------------

while user_name != name or user_pin != pin:
	attempts -=1
	print("______________________")
	print(f"Wrong Incredients 🚨")
	print(f"Attempts Left : {attempts} ⚠️")
	print("=====================")
	user_name = input("\nType Your Name :|")
	user_pin = int(input("Type The Pin :  |"))
	if attempts == 1:
		print("_______________________")
		print("Account Blocked.....☠️")
		break
else:
	print("_____________________________")
	withdraw = int(input("Type Ammount To Cash Out:|"))
	balance = balance - withdraw
	print(f"Withdraw Succesfull🎉")
	print("================")
	print(f"New Balance: {balance} ")
	
	