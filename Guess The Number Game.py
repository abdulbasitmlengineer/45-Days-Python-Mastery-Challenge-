print("================= Guess The Number ==================")


def game():

    import random

    user_need = input("Want To Play :(y/n): ")

    while user_need == "y":

        number = random.randint(1, 100)

        user = int(input("Type Number: | "))

        while user != number:

            if user < number:
                user = int(input("Type Again (Higher): | "))

            elif user > number:
                user = int(input("Type Again (Lower): | "))

        print("You Win....... 🎉")

        user_need = input("Want To Play Again :(y/n): ")

    print("AllahHafiz")


game() 