print("_____________________FAVORITE FOOD_________________________")

FOOD = []

FOOD.append(input("TYPE YOUR FAVORITE FOOD:   "))


user_need = input("WANT TO ADD ANOTHER FOOD? (y/n): ")


while user_need == "y":
    FOOD.append(input("TYPE YOUR FAVORITE FOOD:   "))
    user_need = input("WANT TO ADD ANOTHER FOOD? (y/n): ")


print("==================================================================")
print(f"YOUR FAVORITE FOODS: {FOOD}")
print("--------------------------------------------------------------------")
