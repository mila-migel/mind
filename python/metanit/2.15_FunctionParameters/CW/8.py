 # Напишите программу, которая проверяет, содержит ли строка гласные буквы.

vowels = "aeiou"
text = input("Enter a string: ")

contains_vowel = False

for char in text.lower():
    if char in vowels:
        contains_vowel = True
        break

if contains_vowel:
    print("The string contains vowels.")
else:
    print("The string does not contain vowels.")