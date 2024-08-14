#Создайте игру, где пользователь должен угадать число от 1 до 10. Используйте цикл while

number = int(input("Введите число: "))

arr = range(number) # [0,1,2]

for z in arr: 
    print(z)
    z += 1 # z = z + 1