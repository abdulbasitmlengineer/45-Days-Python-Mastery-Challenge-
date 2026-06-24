
def check_needed_weight(target, current):
    gap = target - current
    return gap  

target_input = int(input("TYPE TARGET WEIGHT: "))
current_input = int(input("TYPE YOUR CURRENT WEIGHT: "))

result = check_needed_weight(target_input, current_input)

print("Aap ko kitna weight chahiye:")
print(result)
