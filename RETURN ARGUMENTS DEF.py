print("_______________ PROGRAMMERS ATM SYSTEM _________________")
currentbalance = 1000
#-------------------------------------------------------------------------------------------------------
def atm(balance):
	if userinput <= balance:
		balance = balance - userinput
		print(f"TRANSACTION SUCCESFULL\nNEW BALANCE: {balance} PKR")
		return balance
	else:
		print("YOUR ACCOUNT IS BLOCKED......")
		print("INSUFFICINT BALANCE.....")
		return balance
#-------------------------------------------------------------------------------------------------------
userinput = int(input("TYPE AMMOUNT TO WITHDRAW: "))
newbalance = atm(currentbalance)
print(f"REMAINING BALANCE : {newbalance} PKR")
