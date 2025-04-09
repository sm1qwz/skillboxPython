count = 0
for i in range(10):
    code_of_human = int(input(f"Enter the code of {i+1} your human: "))
    if code_of_human > 0 and code_of_human % 2 ==0:
        count += 1
print(f"You got the {count} correct numbers!")

