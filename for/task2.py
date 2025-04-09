summa = 0
for i in range(0, 12):
    salary = int(input(f"Enter the salary of {i+1} worker: "))
    summa += salary
print(f"The average salary is {summa/12}")
