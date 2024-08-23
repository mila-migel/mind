lenght = int(input("Введите длинну строки: "))

str = ""
for i in range(lenght):
    str = str + "*"

print(str)

index = int(input(f"Введите index от 0 до {lenght - 1}: "))

result = ""
for s in range(len(str)):
    if s == index:
        result += "#"
    else:
        result += "+"

print(result)