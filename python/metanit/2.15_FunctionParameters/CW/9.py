# Используйте for для создания нового списка, содержащего только четные числа из исходного списка.

original_list = [1, 'a', 2, 'b', 3, 'c']
numbers_list = []

for item in original_list:
    if isinstance(item, int):
        numbers_list.append(item)

        print(numbers_list)