n = int(input("How many pupils in the class? "))
nice = 0
good = 0
bad = 0
for i in range(n):
    mark = int(input(f"Enter the mark of {i+1} pupil: "))
    if mark == 5:
        nice += 1
    if mark == 4:
        good += 1
    if mark == 3:
        bad += 1
if nice > good and nice > bad:
    print(f"Today 5 is top of day!")
if good > bad and good > nice:
    print(f"Today 4 is top of day!")
if bad > nice and bad > good:
    print(f"Today 3 is top of day!")
