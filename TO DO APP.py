print("------------- TO DO APP 📔 ----------------")
print("============================================")
#-----------------------------------------------------
def note():
	goals = []
	goals1 = input("TYPE YOUR GOAL: ")
	need = input("Want to add Another GOAL(y/n): ")
	#-----------------------------------------------------
	goals.append(goals1)
	#-----------------------------------------------------
	while need == "y":
		new_goal = input("TYPE YOUR GOAL: ")
		#-------------------------------------------------
		goals.append(new_goal)
		#-------------------------------------------------
		need = input("Want to add Another GOAL(y/n): ")
	print("\n_________YOUR TODAY's TASKS_________")
	number = 1
	for item in goals:
		print(f"{number}.{item}")
		number +=1
note()
