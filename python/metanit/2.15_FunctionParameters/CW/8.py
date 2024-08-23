 # Напишите программу, которая проверяет, содержит ли строка гласные буквы.

vowels = "aeiou" # эта строка содержит все гласние буквы на англиском языке
text = input("Enter a string: ") # запрашивает вивод строки у пользивателя 

contains_vowel = False # устанавливает флаг которий будет 
# показывать найдела ли гласная буква в строке

for char in text.lower(): # цикл приходит по каждому символу в строке text 
    # преведенной к нижнему регистеру с помощью  text.lover().
    if char in vowels:
        contains_vowel = True
        break

if contains_vowel:
    print("The string contains vowels.")
else:
    print("The string does not contain vowels.")