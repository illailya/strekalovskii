#Списки
from os import remove

#Задача 1

x = 1
if x > 0:
    print('Число положительное')


fruits = ["Яблоко", "Банан", "Киви"]
print(fruits)

#задача2

numbers = [10, 20, 30]

numbers.append(40)
numbers[1] = 25
print(numbers)

#Задача 3

letters = ['a', 'b', 'c', 'd', 'e', 'f']

slice_letters = letters[2:5]
print(slice_letters)

#задача 4

colors = ['red', 'green', 'blue', 'yellow', 'black']

colors.remove("blue")
print(colors)
del colors[2]
print(colors)
colors.clear()
print(colors)

#Задача 5

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list1.extend(list2)
print(list1)

#Задача 6

animals = ['кошка', 'собака', 'хомяк']
animals.insert(2,'попугай')
animals.insert(0,'рыбка')
print(animals)

#Задача 7

electronics = ['телефон', 'ноутбук', 'наушники', 'мышка']
electronics[2] = 'клавиатура'
electronics[-1] = 'монитор'
print(electronics)

#Задача 8

cars = ['Toyota', 'BMW', 'Mercedes', 'Audi', 'Tesla']
print(f"{cars[0]}\n{cars[-1]}\n{cars[2]}")

#Задача 9

inventory = ['меч', 'щит', 'зелье', 'карта']
inventory.clear()
if not inventory:
    print("Инвентарь пуст")
else:
    print("В инвентаре есть предметы")

#Задача 10

movies = ['брат', 'брат 2', 'брат 3']
movies.append("форсаж")
movies[1] = 'Титаник'
print(f"{movies}\nДлина списка: {len(movies)}")

#задача 11

fruits = ["яблоко", "банан"]
fruits.append("апельсин")
fruits.insert(0, "киви")
print(f"Итоговый список: {fruits}")

#Задача 12

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result1 = numbers[1:5]
result2 = numbers[::2]
result3 = numbers[::-1]
print(f"Извлечь элементы со 2-го по 5-й (включительно): {result1}, \nИзвлечь каждый второй элемент списка: {result2}, \nИзвлечь список в обратном порядке: {result3}")

#Задача 13

languages = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'PHP']
del languages[2]
print(f"Удалить 'C++' по значению: {languages}")
del languages[3]
print(f"Удалить элемент с индексом 3: {languages}")
languages.clear()
print(f"Очистить список полностью: {languages}")


#Задача 14

animals = ['кошка', 'собака', 'попугай', 'хомяк']
print(animals[2])


#Задача 15

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

#Задача 16

letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters[1:5])

#Задача 17

fruits = ['яблоко', 'груша', 'банан', 'киви']
fruits[1] = "апельсин"
print(fruits)

#Задача 18

colors = ['красный', 'зеленый', 'синий', 'желтый']
colors.remove("синий")
print(colors)

#Задача 19

words = ["привет", "Python"]
words.insert(1, "мир")
print(words)

#Задача 20

list1 = [1, 2]
list2 = [3, 4]
result1 = list1 + list2
print(result1)

#Задача 21

data = [10, 20, 30, 40]
data.clear()
print(data)

#

fruits = ["банан", "яблоко", "киви"]

#

cars = ["BMW", "Audi", "Tesla", "Toyota"]
print(cars[1])

#

animals = ["cat", "dog"]
animals.append("bird")
print(animals)

#

colors = ["red", "blue", "green"]
colors.insert(1, "yellow")
print(colors)

#

laptops = ["Lenovo", "Acer", "Dell", "HP"]
laptops[2] = "Asus"
print(laptops)

#

numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print(numbers)

#

temperatures = [25, 30, 18, 22]
temperatures.clear()
print(temperatures)

#

letters = ['a', 'b', 'c', 'd', 'e', 'f']
result = letters[1:4]
print(result)

#

tools = ["молоток", "отвёртка", "пила", "гаечный ключ"]
removed_tool = tools.pop(2)
print(tools)
print(removed_tool)

#

numbers = [5, 3, 9, 1]
numbers.reverse()
print(numbers)

#

words = ["яблоко", "банан", "яблоко", "вишня", "яблоко"]
print(words.count("яблоко"))

temperatures = [-5, 12, 3, 0, -10]
minimum =min(temperatures)
maximum = max(temperatures)
print(minimum)
print(maximum)

#

num = []
for n in range(2,11,2):
    print(n)

#

num = [n for n in range(2,11) if n%2 ==0]
print(num)

#

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])
print(matrix[1][1])

#

data = [["a", "b"], ["c", "d"], ["e", "f"]]
print(data[0][0:2][0:1])

#

animals = ["кошка", "собака", "птица"]
print(animals)

#

fruits = ["яблоко", "груша", "банан"]
print(fruits[0])

#

items = []
items.append("книга")
print(items)

#

colors = ["красный", "синий", "зеленый"]
print(len(colors))

#

tools = ["молоток", "пила", "отвертка"]
print("пила" in tools)

#

numbers = [10, 20]
numbers.append(30)
print(numbers)

#

letters = ['a', 'b', 'c']
print(letters[-1])

#

fruits = ["яблоко", "груша", "вишня"]
fruits.remove("вишня")
print(fruits)

#

ages = [25, 30, 18]
ages[1] = 35
print(ages)

#

empty = []
print(empty != [])

#

mixed = [1, "текст", True]
print(type(mixed))


#

fruits = ["банан", "киви", "абрикос"]

#

colors = ["красный", "зелёный", "синий", "жёлтый"]

print(colors[1])

#

animals = ["кошка", "собака", "хомяк"]
animals.append("попугай")
animals[1] = "рыбка"
print(animals)

#

numbers = [10, 20, 40, 50]
numbers.insert(2, 30)
print(numbers)

#

tools = ["молоток", "отвёртка", "пила", "гаечный ключ"]

tools.remove("пила")
print(tools)

#

letters = ['a', 'b', 'c', 'd', 'e', 'f']

new_letter = letters[1:4]
print(new_letter)

#

list1 = [1, 2, 3]
list2 = [4, 5]
result = list1 + list2
print(result)

#

data = [True, False, 1, "текст", 3.14]
data.clear()
print(data)