#Циклы
#задание1
from mmap import error

from lesson1 import count

text = "Python"
for text1 in text:
    print(text1)


#задание2

print(list(range(5,11)))

#задание3

i = 1
while i <= 5:
    print(i)
    i += 1


#задание4

for num in range(3,9):
    print(num)

#Задача 5

for num in range(0,5):
    print(num)

#Задача 6

for text in "код":
    print(text)

#Задача 7

num = 5
while num > 0:
    print(num)
    num -=1

#задача 8

temps = [25.3, 18.7, 30.5, 22.0, 17.1]
for temp in temps:
    print(f"Температура: {temp}")

#задача

fruits = ["яблоко", "банан", "апельсин"]
for fruit in fruits:
    print(fruit)

#Задача

count = 1
while count < 6:
    print(count)
    count +=1

#Задача

print(list(range(10,20)))

#Задача

for item in range(3, 9):
  print(item)

#Задача

x = 0
while True:
    x += 1
    print(x)
    if x == 5:
     break

#Задача

x = 10
while True:
    x -= 1
    print(x)
    if x < 4:
        break


#задача

# count = 0
# while True:
#     x = input("Введите число (0 для выхода): ")
#     if x == "0":
#         break
#     count += 1
# print(f"Вы ввели {count} чисел")

#Задача

x = 1
while x < 6:
    print(x)
    x += 1

#

x = "Привет"
for y in x:
    print(y)

#


for item in range(2,7,2):
    print(item)

#

x = 2
while x < 7:
    print(x)
    x += 2

#

text = "Python"
for result in text:
    print(result)

#

for num in range(0,10,2):
    print(num)

#

for num in range(1,6):
    print(num **2)

#

x = 5
while x >= 1:
    print(x)
    x -= 1

#
x = 1
while x < 10:

    print(x)
    x += 1
    if x >= 5:
     break


#

for num in range(0,10,2):
    print(num)

#

x = 10
while x >0:
    print(x)
    x -=1


#



animals = ["кошка", "собака", "попугай", "хомяк", "рыбка"]
count = 0
for animal in animals:
    if len(animal):  # Проверяем чётность длины слова
        print(f"{animal} ({len(animal)} букв)")
        count += 1
print(f"Всего: {count}")

#

fruits = ["яблоко", "банан", "вишня"]
for fruit in fruits:
    print(fruit)

#

for num in range(3,9):
    print(num)

#

x = 5
while x >= 1:
    print(x)
    x -=1
print("Старт! ")

#

x = 1
while x < 10:
    if x == 5:  # Проверяем ДО вывода и увеличения
        break
    print(x)
    x += 1

#

for num in range(2,11,2):
    print(num)

#

numbers = [4, 2, 9, 1, 7, 5]
num = numbers[:3]
print(num)
numbers.sort()
print(numbers)

#

colors = ["красный", "синий", "зеленый", "желтый"]
colors.insert(1, "оранжевый")
colors.remove("зеленый")
colors.reverse()
print(colors)

#

animals = ["кошка", "собака", "хомяк"]
for animal in animals:
    print(f"Животное: {animal}" )

#

for numbers in range(15,9,-1):
    print(numbers)

#

count = 3
while count >= 0:
    print(count)
    count -=1
print("Старт!")

#

for num in range(1, 11):
    if num %4 ==0:
        break
    print(num)

#

for num in range(1, 7):
    continue
    print(num)

#
a = "задача"
print(a)


numbers = [3, 7, 2, 8, 4, 10]
for num in numbers:
    if num > 5:
        print(f"{num} (больше 5)")
    else:
        print(num)

#


numbers = [3, 7, 2, 8, 4, 10]
for num1 in numbers:
    if num1 == 10:
        break
    print(num1)


#


numbers = [3, 7, 2, 8, 4, 10]
for num2 in numbers:
    if num2 %2 == 0:
        print(f"{num2} Четное")
    else:
        print(num2)


#
text = "Python"
for result in text:
    print(result)

#

for num in range(2,11,2):
    print(num)

#

x = 1
while x < 6:
    print(x)
    x += 1


#

x = 1
while x <= 10:
    print(x)
    if x == 7:
     break
    x += 1

#

for num in range(5,0,-1):
    print(num)

#

fruits = ["яблоко", "банан", "вишня"]
for result in fruits:
    print(f"Фрукт: {result}")