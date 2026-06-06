print("========== AGE CALCULATOR ==========")

name = input("Enter Your Name: ")
birth_year = int(input("Enter Your Birth Year: "))
current_year = int(input("Enter Current Year: "))

age = current_year - birth_year

print(f"\nHello {name}!")
print(f"You are {age} years old.")