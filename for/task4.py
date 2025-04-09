a = int(input("Enter the start of segment: "))
b = int(input("Enter the end of segment: "))
summa = 0
count = 0
for i in range(a, b+1):
    if i % 3 == 0:
        print(f"The {i} number can be divided by 3")
        count += 1
        summa += i
print(f"The avegare of theese numbers is {summa/(count)}")
