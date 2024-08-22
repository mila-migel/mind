# Напишите программу, которая выводит числа Фибоначчи до 100, используя цикл for.

fib1, fib2 = 0, 1

print(fib1)
print(fib2)

for _ in range(2, 100):
    fib_next = fib1 + fib2
    if fib_next >= 100:
        break
    print(fib_next)
    fib1, fib2 = fib2, fib_next