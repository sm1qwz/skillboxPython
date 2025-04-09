number = int(input("Choose secret number: "))
answer = 0
count = 0
if 1 <= number <= 10:
    answer = int(input("Okay, what is your number? : "))
    while answer != number:
        if answer < number:
            print(f"No, try again. The number is bigger")
            answer = int(input("Choose your number again: "))
        else:
            print(f"No, try again. The number is smaller")
            anser = int(input("Choose your number again: "))
        count += 1
    print(f"You got it! Your number of attempts was {count}")
else:
    print("Please enter a number between 1 and 10")


#Как тут еще можно было бы обработать случай когда указывает с первого раза?
#Не хотел добавлять еще одну условие, думаю можно как-то более оптимизировано
