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