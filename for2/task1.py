kilograms = 100
kilograms_per_month = 4
months = kilograms // kilograms_per_month
for month in range(1, months +1):
    remaining = kilograms - month * kilograms_per_month
    print(f"After {month} month we have {remaining} kilograms")
print(f"The grechka is over.")