n = int(input("Enter your number: "))
count = 0
if n == 0:
    print(f"Count of numbers = 1")
elif n > 0:
    while n > 0:
        n //= 10
        count += 1
    print(f"Count of numbers = {count}")
else:
    print("Enter correct number, number must be > 0 or = 0")