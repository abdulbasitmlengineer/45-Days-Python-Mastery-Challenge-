print("================= BANK OF PROGRAMMERS =================")

user_name = "basit"
password = "1234"

#============================

user_input = input("Type UserName:                    |")
user_input_password = input("Type Password:                    |")

Attempts = 4

#============================

if user_input == user_name and user_input_password == password:
print("===================")
print("You Successfully Login")

while user_input != user_name or user_input_password != password:
Attempts -= 1
print("======================")
print("Wrong UserName or Password!")
print(f"You Have {Attempts} Attempts Left ! ")
print("----------------------------------------")
user_input = input("Type UserName:                    |")
user_input_password = input("Type Password:                    |")
if Attempts == 1:
print("Your Account Is Blocked......")
exit()

#============================