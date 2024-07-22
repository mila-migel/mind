name = "Tom"

def say_hi():
    name = "Bob"        # скрываем значение глобальной переменной
    print("Hello", name)

def say_bye():
    print("Good bye", name)
 
say_hi()    # Hello Bob
say_bye()   # Good bye Tom