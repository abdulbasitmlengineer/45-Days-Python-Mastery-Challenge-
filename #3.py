print("-----------------Welcome to Calculator-----------------")
number1 = int(input("Type A Value 1:       "))
number2 = int(input("Type A Value 2:       "))
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
user_input = input("Chose A Operation you want to do Calculation With (+  -  *  ÷)")
if user_input == "+":
	print(f"Your Answere Is {addition}  ")
elif user_input == "-":
	print(f"Yor Answere is {subtraction}")
elif user_input == "*":
	print(f"Your Answer is {multiplication}")
elif user_input == "÷":
	print(f"Your Answer is {division}")
else:
	print("Wrong Input.....")
