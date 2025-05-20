#задача 1

fruits = ["яблоко", "банан"]
fruits.append("апельсин")
fruits.insert(0, "киви")
print(f"Итоговый список: {fruits}")

#Задача 2

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result1 = numbers[1:5]
result2 = numbers[::2]
result3 = numbers[::-1]
print(f"Извлечь элементы со 2-го по 5-й (включительно): {result1}, \nИзвлечь каждый второй элемент списка: {result2}, \nИзвлечь список в обратном порядке: {result3}")

#Задача 3

languages = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'PHP']
del languages[2]
print(f"Удалить 'C++' по значению: {languages}")
del languages[3]
print(f"Удалить элемент с индексом 3: {languages}")
languages.clear()
print(f"Очистить список полностью: {languages}")