print("----------------------------Welcome GUESS THE NUMBER Game----------------------------")
def game():
    number = 5
    #----------------------------------------------------------------------------------
    user = int(input("TYPE THE NUMBER ⌨️: "))
    #----------------------------------------------------------------------------------
    while user != number:
        if user < number:
            user = int(input("TYPE THE NUMBER AGAIN (🔺): "))
        elif user > number:
            user = int(input("TYPE THE NUMBER AGAIN (🔻): "))
    print("----------------------------------------------------------------------------------")
    print("CONGRATULATIONS 🥳 YOU WIN ........")
    userneed = input("WANT TO PLAY AGAIN? (y/n): ")
    if userneed == "y":
        game()
    else:
        print("HAVE A NICE DAY ALLAH-HAFIZ....🥰")
game()
