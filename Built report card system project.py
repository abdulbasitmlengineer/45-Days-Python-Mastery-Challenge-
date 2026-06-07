print("-----------WELCOME TO RESULT IDENTIFY PROGRAM---------")
print("====================================================")

user_name = input("What Is Your Name????          | ")
user_age = input("How old are you????            | ")
user_class = input("In which class do you read???? | ")

user_math = int(input("Marks of Math subject????      | "))
user_english = int(input("Marks of English subject????   | "))
user_science = int(input("Marks of Science????           | "))

user_total_marks = user_math + user_english + user_science

total_marks = 300

percentage = (user_total_marks / total_marks) * 100

print("====================================================")

print(f"{user_name} Here Are Your Score List:")
print(f"English : {user_english}")
print(f"Maths   : {user_math}")
print(f"Science : {user_science}")

print("====================================================")

if percentage < 50:
    print(f"{user_name} You Got {percentage}% in Your {user_class} Class Examination")
    print("You Failed. Better Luck Next Time.")

else:
    print(f"{user_name} You Got {percentage}% in Your {user_class} Class Examination")
    print("Congratulations! You Passed.")

print("====================================================")

if percentage >= 90:
    print(f"{user_name} You Got A+ Grade In Your {user_class} Class Examination")
    print("That's Really Incredible!")
    print("You Are Genius....")

elif percentage >= 80 and percentage < 90:
    print(f"{user_name} You Got A Grade In Your {user_class} Class Examination")
    print("That's Really Incredible!")
    print("You Are Smart....")

elif percentage >= 70 and percentage < 80:
    print(f"{user_name} You Got B Grade In Your {user_class} Class Examination")
    print("That's Really Nice!")
    print("You Are Good....")

elif percentage >= 60 and percentage < 70:
    print(f"{user_name} You Got C Grade In Your {user_class} Class Examination")
    print("That's Nice!")

elif percentage >= 50 and percentage < 60:
    print(f"{user_name} You Got D Grade In Your {user_class} Class Examination")
    print("You Need Some More Effort....")

else:
    print(f"{user_name} You Got F Grade In Your {user_class} Class Examination")
    print("Work Hard And Try Again!")
