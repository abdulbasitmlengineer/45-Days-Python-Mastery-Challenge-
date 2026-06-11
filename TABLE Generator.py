print("================== TABLE GENERATOR ===================")

def game():
    Table = int(input("Which Table do you want to generate:     |"))
    print("==============================================================================================================")
    for i in range(1, 11):
        new = i * Table
        print(f"{Table}  x   {i} =  {new}")

game()


user = input("Want Another Table?:(y/n) ")


while user == "y":
    game()
    
    user = input("Want Another Table?:(y/n) ")
    

else:
    print("Allahhafiz.....")
    

print("========================")
