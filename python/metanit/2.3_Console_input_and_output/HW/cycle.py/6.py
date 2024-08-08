#Напишите программу, которая выводит числа Фибоначчи до 100.

i = 2
previous = 1
while i <= 80:  
    a = i
    i = i + previous
    print(i) 
    previous = a

print("end")