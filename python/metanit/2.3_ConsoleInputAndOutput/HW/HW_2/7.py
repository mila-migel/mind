#Создайте игру, где пользователь должен угадать число от 1 до 10. Используйте цикл while

import random

secret_number = random.randint(1, 10)
guess = None

while guess != secret_number:
    guess = int(input("Угадайте число от 1 до 10: "))
    
    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    else:
        print("Поздравляем, вы угадали!")

