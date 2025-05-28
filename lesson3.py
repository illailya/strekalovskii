#Списки

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