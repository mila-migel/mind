# Создайте программу, которая запрашивает у пользователя числа 
# и завершает работу, когда введено число 0.

while True:  
    number = int(input("Введите число: "))   
    
    if number == 0:  
        print("Программа завершена.")  
        break 
    else:
        print(f"Вы ввели число {number}") 
