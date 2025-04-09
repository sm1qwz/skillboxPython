start = 10
end = 99
for i in range(start, end+1):
    first_digit = i //10
    second_digit = i % 10
    final = (first_digit * second_digit) * 3
    if final == i:
        print(f"The {i} number is goooooood!")
