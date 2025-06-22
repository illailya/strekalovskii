# 1
from lesson3 import minimum, maximum

a = 1
b =1.1
c ="123"
print(f"{a}, {b}, {c}")
#2
s = "Привет, мир!"
print(len(s))
print(s[0])
print(s[-2])
#3
lst = [1, 2, 3, 4, 5]
lst.append(6)
del lst[1]
print(lst)
#4
x = 55
if x > 10:
    print("Больше 10")
else:
    print("10 или меньше")
#5
person = {
"name": "Илья",
"age": 33
}
print(person)
#6
for num in range(1,6):
    print(num**2)
#7
with open("test.txt", "w", encoding="utf-8") as file:
    file.write("Hello, file!")
#8
def multiply(a, b):
    return a * b
print(multiply(5,5))
#8
class Car:
    def __init__(self, color):
        self.color = color
    def show_color(self):
        print(self.color)

    def change_color(self, new_color):
        self.color = new_color
c = Car("Зеленый")
c.show_color()
c.change_color("Черный")
c.show_color()

######################################################
# 1
num = 15
text = "лет"
num_str = str(num)
result = num_str + " " + text
print(result)
#2
s = "Python"
result = s[::-1]
print(result[0:3])
#3
numbers = [10, 20, 30, 40]
numbers[1] = 25
del numbers[-1]
print(numbers)
print(len(numbers))
#4
temperature = 25
if temperature > 30:
    print("Жарко")
elif temperature < 15:
    print("Холодно")
else:
    print("Нормально")
#5
book = {
"title": "Название",
"author": "Автор",
"year": 111
}
book["pages"] = 158
print(book)
#6
x = 2
while x <= 10:
    if x %2 ==0:
     print(x)
    x +=1
#7
with open("test.txt", "r", encoding="utf-8") as file:
    result = file.read()
    print(result)
#8
def is_even(n):
    if n %2 ==0:
        return True
    else:
        return False
print(is_even(6))
#9-10
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("Гав!")
    def human_age(self):
        return self.age * 7
d = Dog("Тузик", 3)
print(d.human_age())
#11
for num in range(1,6):
    print(num)
with open("numbers.txt", "w", encoding="utf-8") as file:
    file.write(f"{num}")
with open("numbers.txt", "r", encoding="utf-8") as file:
    result = file.read()
print(result)
#############################3
#1
price = 19.99
quantity = 3
total = price * quantity
print(f"Итого: {total} руб.")
#2
s = "Я изучаю Python"
new_s = s.replace("изучаю", "люблю")
result = new_s.split()
print(new_s)
print(result)
#3
fruits = ["яблоко", "банан", "апельсин"]
fruits.insert(1,"киви")
del fruits[-1]
if "банан" in fruits:
    print(True)
else:
    print(False)
#4
score = 85
if score >= 90:
    print("Отлично")
elif 89 >= score >= 70:
    print("Хорошо")
elif 69 >= score >= 50:
    print("Удовлетворительно")
else:
    print("Неудовлетворительно")
#5
movie = {
"title": "Фильм",
"director": "Режисер",
"year": 77
}
print(movie)
movie["rating"] = 10
movie["year"] = 5
print(movie)
#6
n = 5
for i in range(1,n + 1):
    print(str(i) * i)
#7
with open("diary.txt", "w", encoding="utf-8") as file:
    file.write("Сегодня хороший день.\nЯ научился работать с файлами.")
with open("diary.txt", "r", encoding="utf-8") as file:
    text = file.readlines()
    line = text[1]
print(line)
#8
def greet(name):
    print(f"Привет, {name}!")
greet("Илья")
#9 - 10
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def info(self):
        print(f"Книга: {self.title}, Автор: {self.author}")
    def is_thick(self):
        if self.pages > 300:
            print(True)
        else:
            print(False)
b = Book(1,2,3)
b.is_thick()
#############################################################

#1
a = 5
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
#2
s = "hello"
s = "hello!!!"
s1 = s.upper()
print(s1, len(s1))
#3
nums = [1, 2, 3]
nums.append(4)
del nums[0]
print(nums, len(nums))
#4
x = 10
if x % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")
#5
student = {
"name": "Илья",
"age": 33
}
student["age"] += 1
print(student)
#6
for num in range(1,11):
    if num != 5:
     print(num)
#7
n = 3
count = 0
while count < n:
    print("Loading...")
    count += 1
#8
with open("task.txt", "w", encoding="utf-8") as file:
    file.write("Python is awesome!")
#9
def multiply(a, b):
    return a * b
print(multiply(2, 4))
#10
class Cat:
    name = "Барск"
    def meow(self):
        print(f"{self.name} говорит Мяу!")
c = Cat()
c.meow()
#11
n = 4
numbers = []
count = 1
while count <= n:
    numbers.append(count)
    count += 1
with open("numbers.txt", "w", encoding="utf-8") as file:
    for num in numbers:
     file.write(f"{num}\n")
with open("numbers.txt", "r", encoding="utf-8") as file:
    result = file.readlines()
    total = sum(int(line.strip()) for line in result)
    print(total)
###########################
#1
price = 100
discount = 50
result = price - (price * (discount / 100))
print(f"Итоговая цена: {result} руб.")
#2
s = "Я изучаю Python"
s = s.upper()
s = s.replace(" ", "_")
print(f"{s}, Длинна: {len(s)}")
#3
nums = [4, 2, 9, 1, 5]
nums.sort()
minimum = nums[0]
maximum = nums[-1]
print(f"Отсортированный список {nums}")
print(f"Минимальное значение {minimum}")
print(f"Максимальное значение {maximum}")
#4
age = 20
if 1 <= age <= 12:
    print("Детство")
elif 13 <= age <= 19:
    print("Юность")
elif 20 <= age <= 65:
    print("Взрослый")
elif age <= 66:
    print("Детство")
else:
    print("Возраст некорректный")
#5
country = {
"name":  "Россия",
"population": 165
}
country["capital"] = 100
country["name"] = "США"
print(country)
#6
for num in range(10,0,-1):
    print(num)
#7
s = "hello"
index = 0
while index < len(s):
    print(s[index])
    index += 1
#8
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("1\n2\n3\n")
with open("data.txt", "r", encoding="utf-8") as file:
    total = sum(int(line.strip())for line in file)
print(total)
#9
def is_palindrome(word):
    return word == word[::-1]
p = is_palindrome("топот")
print(p)
#10
class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств")
bank = BankAccount()
print(bank.balance)
bank.deposit(1000)
print(bank.balance)
bank.withdraw(10)
print(bank.balance)
#11
import random  # Импортируем модуль для работы со случайными числами

n = 5  # Количество чисел для генерации

# 1. Генерация списка случайных чисел
random_numbers = [random.randint(1, 10) for _ in range(n)]
print("Сгенерированные числа:", random_numbers)
#######################################################################
#1
price = 1500
discount = 25
result = price - (price * (discount / 100))
print(f"Цена со скидкой: {result} руб.")
#2
city = "Москва"
temp = 20
new = "е"
text = city[:-1] + new
result = f"В {text} сейчас {temp}°C"
print(result)
#3
items = ["яблоко", "груша", "апельсин"]
items.insert(1, "банан")
del items[-1]
print(items)
#4
def check_password(password):
    return len(password) >= 8
print(check_password("1545"))
#5
numbers = [10, 3, 17, 5, 24]
new_num = [num for num in numbers if num % 2 == 0]
print(new_num)
#6
def count_words(text):
    return len(text.split())
print(count_words("ыкп ыка ыкпм"))
#7
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("1: Помыть\n2: Погладить\n3: Повесить")
with open("notes.txt", "r", encoding="utf-8") as file:
    result = file.readline()
print(result)
#8
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_cost(self):
        return self.price * self.quantity
p = Product("вам", 12, 43)
print(p.total_cost())
#9
# numbers = input("Введите число: ")
# if numbers != int():
#     print("Ошибка: нужно ввести число!")
# else:
#     print(numbers **2)
#######################################################
#1
# name = input("Ведите ваше имя: ")
# age = int(input("Введите ваш возраст: "))
# age1 = age +1
# text1 = "лет"
# text2 = "год"
# text3 = "года"
# if age1[-1] == 1:
#     retern year
# print(f"Привет, {name}! В следующем году тебе будет {age1} лет.")
#2
a = 10
b = 3
result = (a / b, 2)
result1 = a // b
result2 = a ** b
##########################################################3
#1
num = 10
pi = 3.14
name = "имя"
print(f"{num}, {pi}, {name}")
#2
s = "Программирование"
print(len(s))
print(s[0])
print(s[-1])
#3
lst = [5, 2, 8, 1, 9]
del  lst[1]
lst.append(10)
print(lst)
#4
x = 15
if x > 20:
    print("Больше 20")
else:
    print("20 или меньше")
#5
car = {
"brand": "Toyota",
"year": 2020
}
print(car["brand"])
#6
for num in  range(1,6):
    print(num)
#7
n = 3
text = "Hello"
while n > 0:
    print(text)
    n -= 1
#8
with open("test.txt", "w", encoding="utf-8") as file:
    file.write("Тест записи")
#9
def is_positive(n):
    return n > 0
print(is_positive(-5))
#10
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print("Гав!")
    def change_name(self, new_name):
        self.name = new_name
d = Dog("gh")
###########################################################
#1
a = 5
b = 2.5
c = "3"
c = int(c)
print(a + b + c)
#2
s = "автоматизация"
s = s.replace("а", "@")
s = s.upper()
print(s)
#3
numbers = [4, 7, 1, 9, 3]
numbers.sort()
result = numbers[0] + numbers[-1]
print(numbers)
print(result)
#4
age = 19
result1 = "Доступ запрещён" if age < 18 else "Доступ разрешён"
print(result1)
#5
student = {
"name": "Илья",
"grades": [5, 4, 3]
}
student["grades"].append(5)
print(student)
#6
fruits = ["яблоко", "банан", "апельсин"]
print(f"Фрукт: {fruits[0]}, длинна: {len(fruits[0])}")
print(f"Фрукт: {fruits[1]}, длинна: {len(fruits[1])}")
print(f"Фрукт: {fruits[2]}, длинна: {len(fruits[2])}")
#7
n = 4
while n >= 1:
    print(n)
    n -= 1
#8
with open("log.txt", "w", encoding="utf-8") as file:
    file.write("21:58 22.06.2025")
with open("log.txt", "r", encoding="utf-8") as file:
    result = file.read()
print(result)
#9
def is_even(n):
    return n %2==0
print(is_even(6))
#10
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def info(self):
        print(f"Книга: {self.title}, Автор: {self.author}")
    def is_thick(self):
        return self.pages > 300
b = Book("rtgrt","rtg",2282)
b.info()
print(b.is_thick())
#11
import random
n = 5
numbers  = [random.randint(1,100) for _ in range(n)]
with open("numbers.txt", "w", encoding="utf-8") as file:
    for num in numbers:
     file.write(f"{num}\n")
with open("numbers.txt", "r", encoding="utf-8") as file:
    result = file.read()
print(result)