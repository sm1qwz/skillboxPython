X = int(input("Enter how many rubles can you invest: ")) #invest
P = int(input("Enter percent of your bank: ")) #percent
Y = int(input("Enter how many rubles are your goal: ")) #goal
years = 0
deposit = X

while deposit < Y:
    deposit += (deposit * P) // 100
    years += 1

print(f"Now is {years} years after. You reach your goal")