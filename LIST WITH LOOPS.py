print("--------WELCOME TO GOAL STORED--------")

def store():
    GOALS = []
    first_goal = input("TYPE YOUR GOAL: ")
    GOALS.append(first_goal)
    USER_NEED = input("WANT TO ADD MORE (y/n): ")

    while USER_NEED == "y":
        more_goal = input("TYPE YOUR GOAL: ")
        GOALS.append(more_goal)
        USER_NEED = input("WANT TO ADD MORE (y/n): ")
        
    print("\nYOUR FINAL GOALS ARE:")
    print(GOALS)
store()
