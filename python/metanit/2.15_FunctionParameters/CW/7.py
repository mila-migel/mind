# Используйте for для нахождения наибольшего числа в списке.

numbers = [3, 7, 2, 8, 10, 4]
max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print("The largest number in the list is", max_number)
