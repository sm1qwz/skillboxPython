print("Start of the work day:(")
hours_count = 1
deals_count = 0
wife_calling = 0
while hours_count <= 8:
    print(f"{hours_count} hour of work day")
    hours_count += 1
    deals = int(input("How many deals done Maxim? "))
    deals_count += deals
    if wife_calling < 1:
        wife_calling = int(input("Your wife is calling, will you pick up? 1 - yes, 0 - no"))
        if wife_calling != 1 or wife_calling != 0:
            print("Sorry, enter the correct number from hint")
print(f"The work day is off. You done the {deals_count} deals. ")
if wife_calling == 1:
    print(f"Your need to go in market.")


