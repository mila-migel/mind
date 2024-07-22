class Person:
    def __init__(self, name, age):
        self.name = name    # устанавливаем имя
        self.age = age      # устанавливаем возраст
                 
    def print_person(self):
        print(f"Имя: {self.name}\tВозраст: {self.age}")
         
 
tom = Person("Tom", 39)
tom.name = "Человек-паук"       # изменяем атрибут name
tom.age = -129                  # изменяем атрибут age
tom.print_person()              # Имя: Человек-паук     Возраст: -129
