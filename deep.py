# # # # 1
# # # from lesson3 import minimum, maximum
# # #
# # # a = 1
# # # b =1.1
# # # c ="123"
# # # print(f"{a}, {b}, {c}")
# # # #2
# # # s = "Привет, мир!"
# # # print(len(s))
# # # print(s[0])
# # # print(s[-2])
# # # #3
# # # lst = [1, 2, 3, 4, 5]
# # # lst.append(6)
# # # del lst[1]
# # # print(lst)
# # # #4
# # # x = 55
# # # if x > 10:
# # #     print("Больше 10")
# # # else:
# # #     print("10 или меньше")
# # # #5
# # # person = {
# # # "name": "Илья",
# # # "age": 33
# # # }
# # # print(person)
# # # #6
# # # for num in range(1,6):
# # #     print(num**2)
# # # #7
# # # with open("test.txt", "w", encoding="utf-8") as file:
# # #     file.write("Hello, file!")
# # # #8
# # # def multiply(a, b):
# # #     return a * b
# # # print(multiply(5,5))
# # # #8
# # # class Car:
# # #     def __init__(self, color):
# # #         self.color = color
# # #     def show_color(self):
# # #         print(self.color)
# # #
# # #     def change_color(self, new_color):
# # #         self.color = new_color
# # # c = Car("Зеленый")
# # # c.show_color()
# # # c.change_color("Черный")
# # # c.show_color()
# # #
# # # ######################################################
# # # # 1
# # # num = 15
# # # text = "лет"
# # # num_str = str(num)
# # # result = num_str + " " + text
# # # print(result)
# # # #2
# # # s = "Python"
# # # result = s[::-1]
# # # print(result[0:3])
# # # #3
# # # numbers = [10, 20, 30, 40]
# # # numbers[1] = 25
# # # del numbers[-1]
# # # print(numbers)
# # # print(len(numbers))
# # # #4
# # # temperature = 25
# # # if temperature > 30:
# # #     print("Жарко")
# # # elif temperature < 15:
# # #     print("Холодно")
# # # else:
# # #     print("Нормально")
# # # #5
# # # book = {
# # # "title": "Название",
# # # "author": "Автор",
# # # "year": 111
# # # }
# # # book["pages"] = 158
# # # print(book)
# # # #6
# # # x = 2
# # # while x <= 10:
# # #     if x %2 ==0:
# # #      print(x)
# # #     x +=1
# # # #7
# # # with open("test.txt", "r", encoding="utf-8") as file:
# # #     result = file.read()
# # #     print(result)
# # # #8
# # # def is_even(n):
# # #     if n %2 ==0:
# # #         return True
# # #     else:
# # #         return False
# # # print(is_even(6))
# # # #9-10
# # # class Dog:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age
# # #     def bark(self):
# # #         print("Гав!")
# # #     def human_age(self):
# # #         return self.age * 7
# # # d = Dog("Тузик", 3)
# # # print(d.human_age())
# # # #11
# # # for num in range(1,6):
# # #     print(num)
# # # with open("numbers.txt", "w", encoding="utf-8") as file:
# # #     file.write(f"{num}")
# # # with open("numbers.txt", "r", encoding="utf-8") as file:
# # #     result = file.read()
# # # print(result)
# # # #############################3
# # # #1
# # # price = 19.99
# # # quantity = 3
# # # total = price * quantity
# # # print(f"Итого: {total} руб.")
# # # #2
# # # s = "Я изучаю Python"
# # # new_s = s.replace("изучаю", "люблю")
# # # result = new_s.split()
# # # print(new_s)
# # # print(result)
# # # #3
# # # fruits = ["яблоко", "банан", "апельсин"]
# # # fruits.insert(1,"киви")
# # # del fruits[-1]
# # # if "банан" in fruits:
# # #     print(True)
# # # else:
# # #     print(False)
# # # #4
# # # score = 85
# # # if score >= 90:
# # #     print("Отлично")
# # # elif 89 >= score >= 70:
# # #     print("Хорошо")
# # # elif 69 >= score >= 50:
# # #     print("Удовлетворительно")
# # # else:
# # #     print("Неудовлетворительно")
# # # #5
# # # movie = {
# # # "title": "Фильм",
# # # "director": "Режисер",
# # # "year": 77
# # # }
# # # print(movie)
# # # movie["rating"] = 10
# # # movie["year"] = 5
# # # print(movie)
# # # #6
# # # n = 5
# # # for i in range(1,n + 1):
# # #     print(str(i) * i)
# # # #7
# # # with open("diary.txt", "w", encoding="utf-8") as file:
# # #     file.write("Сегодня хороший день.\nЯ научился работать с файлами.")
# # # with open("diary.txt", "r", encoding="utf-8") as file:
# # #     text = file.readlines()
# # #     line = text[1]
# # # print(line)
# # # #8
# # # def greet(name):
# # #     print(f"Привет, {name}!")
# # # greet("Илья")
# # # #9 - 10
# # # class Book:
# # #     def __init__(self, title, author, pages):
# # #         self.title = title
# # #         self.author = author
# # #         self.pages = pages
# # #     def info(self):
# # #         print(f"Книга: {self.title}, Автор: {self.author}")
# # #     def is_thick(self):
# # #         if self.pages > 300:
# # #             print(True)
# # #         else:
# # #             print(False)
# # # b = Book(1,2,3)
# # # b.is_thick()
# # # #############################################################
# # #
# # # #1
# # # a = 5
# # # b = 3
# # # print(f"{a} + {b} = {a + b}")
# # # print(f"{a} - {b} = {a - b}")
# # # print(f"{a} * {b} = {a * b}")
# # # print(f"{a} / {b} = {a / b}")
# # # #2
# # # s = "hello"
# # # s = "hello!!!"
# # # s1 = s.upper()
# # # print(s1, len(s1))
# # # #3
# # # nums = [1, 2, 3]
# # # nums.append(4)
# # # del nums[0]
# # # print(nums, len(nums))
# # # #4
# # # x = 10
# # # if x % 2 == 0:
# # #     print("Чётное")
# # # else:
# # #     print("Нечётное")
# # # #5
# # # student = {
# # # "name": "Илья",
# # # "age": 33
# # # }
# # # student["age"] += 1
# # # print(student)
# # # #6
# # # for num in range(1,11):
# # #     if num != 5:
# # #      print(num)
# # # #7
# # # n = 3
# # # count = 0
# # # while count < n:
# # #     print("Loading...")
# # #     count += 1
# # # #8
# # # with open("task.txt", "w", encoding="utf-8") as file:
# # #     file.write("Python is awesome!")
# # # #9
# # # def multiply(a, b):
# # #     return a * b
# # # print(multiply(2, 4))
# # # #10
# # # class Cat:
# # #     name = "Барск"
# # #     def meow(self):
# # #         print(f"{self.name} говорит Мяу!")
# # # c = Cat()
# # # c.meow()
# # # #11
# # # n = 4
# # # numbers = []
# # # count = 1
# # # while count <= n:
# # #     numbers.append(count)
# # #     count += 1
# # # with open("numbers.txt", "w", encoding="utf-8") as file:
# # #     for num in numbers:
# # #      file.write(f"{num}\n")
# # # with open("numbers.txt", "r", encoding="utf-8") as file:
# # #     result = file.readlines()
# # #     total = sum(int(line.strip()) for line in result)
# # #     print(total)
# # # ###########################
# # # #1
# # # price = 100
# # # discount = 50
# # # result = price - (price * (discount / 100))
# # # print(f"Итоговая цена: {result} руб.")
# # # #2
# # # s = "Я изучаю Python"
# # # s = s.upper()
# # # s = s.replace(" ", "_")
# # # print(f"{s}, Длинна: {len(s)}")
# # # #3
# # # nums = [4, 2, 9, 1, 5]
# # # nums.sort()
# # # minimum = nums[0]
# # # maximum = nums[-1]
# # # print(f"Отсортированный список {nums}")
# # # print(f"Минимальное значение {minimum}")
# # # print(f"Максимальное значение {maximum}")
# # # #4
# # # age = 20
# # # if 1 <= age <= 12:
# # #     print("Детство")
# # # elif 13 <= age <= 19:
# # #     print("Юность")
# # # elif 20 <= age <= 65:
# # #     print("Взрослый")
# # # elif age <= 66:
# # #     print("Детство")
# # # else:
# # #     print("Возраст некорректный")
# # # #5
# # # country = {
# # # "name":  "Россия",
# # # "population": 165
# # # }
# # # country["capital"] = 100
# # # country["name"] = "США"
# # # print(country)
# # # #6
# # # for num in range(10,0,-1):
# # #     print(num)
# # # #7
# # # s = "hello"
# # # index = 0
# # # while index < len(s):
# # #     print(s[index])
# # #     index += 1
# # # #8
# # # with open("data.txt", "w", encoding="utf-8") as file:
# # #     file.write("1\n2\n3\n")
# # # with open("data.txt", "r", encoding="utf-8") as file:
# # #     total = sum(int(line.strip())for line in file)
# # # print(total)
# # # #9
# # # def is_palindrome(word):
# # #     return word == word[::-1]
# # # p = is_palindrome("топот")
# # # print(p)
# # # #10
# # # class BankAccount:
# # #     def __init__(self, balance = 0):
# # #         self.balance = balance
# # #     def deposit(self, amount):
# # #         self.balance += amount
# # #     def withdraw(self, amount):
# # #         if self.balance >= amount:
# # #             self.balance -= amount
# # #         else:
# # #             print("Недостаточно средств")
# # # bank = BankAccount()
# # # print(bank.balance)
# # # bank.deposit(1000)
# # # print(bank.balance)
# # # bank.withdraw(10)
# # # print(bank.balance)
# # # #11
# # # import random  # Импортируем модуль для работы со случайными числами
# # #
# # # n = 5  # Количество чисел для генерации
# # #
# # # # 1. Генерация списка случайных чисел
# # # random_numbers = [random.randint(1, 10) for _ in range(n)]
# # # print("Сгенерированные числа:", random_numbers)
# # # #######################################################################
# # # #1
# # # price = 1500
# # # discount = 25
# # # result = price - (price * (discount / 100))
# # # print(f"Цена со скидкой: {result} руб.")
# # # #2
# # # city = "Москва"
# # # temp = 20
# # # new = "е"
# # # text = city[:-1] + new
# # # result = f"В {text} сейчас {temp}°C"
# # # print(result)
# # # #3
# # # items = ["яблоко", "груша", "апельсин"]
# # # items.insert(1, "банан")
# # # del items[-1]
# # # print(items)
# # # #4
# # # def check_password(password):
# # #     return len(password) >= 8
# # # print(check_password("1545"))
# # # #5
# # # numbers = [10, 3, 17, 5, 24]
# # # new_num = [num for num in numbers if num % 2 == 0]
# # # print(new_num)
# # # #6
# # # def count_words(text):
# # #     return len(text.split())
# # # print(count_words("ыкп ыка ыкпм"))
# # # #7
# # # with open("notes.txt", "w", encoding="utf-8") as file:
# # #     file.write("1: Помыть\n2: Погладить\n3: Повесить")
# # # with open("notes.txt", "r", encoding="utf-8") as file:
# # #     result = file.readline()
# # # print(result)
# # # #8
# # # class Product:
# # #     def __init__(self, name, price, quantity):
# # #         self.name = name
# # #         self.price = price
# # #         self.quantity = quantity
# # #     def total_cost(self):
# # #         return self.price * self.quantity
# # # p = Product("вам", 12, 43)
# # # print(p.total_cost())
# # # #9
# # # # numbers = input("Введите число: ")
# # # # if numbers != int():
# # # #     print("Ошибка: нужно ввести число!")
# # # # else:
# # # #     print(numbers **2)
# # # #######################################################
# # # #1
# # # # name = input("Ведите ваше имя: ")
# # # # age = int(input("Введите ваш возраст: "))
# # # # age1 = age +1
# # # # text1 = "лет"
# # # # text2 = "год"
# # # # text3 = "года"
# # # # if age1[-1] == 1:
# # # #     retern year
# # # # print(f"Привет, {name}! В следующем году тебе будет {age1} лет.")
# # # #2
# # # a = 10
# # # b = 3
# # # result = (a / b, 2)
# # # result1 = a // b
# # # result2 = a ** b
# # # ##########################################################3
# # # #1
# # # num = 10
# # # pi = 3.14
# # # name = "имя"
# # # print(f"{num}, {pi}, {name}")
# # # #2
# # # s = "Программирование"
# # # print(len(s))
# # # print(s[0])
# # # print(s[-1])
# # # #3
# # # lst = [5, 2, 8, 1, 9]
# # # del  lst[1]
# # # lst.append(10)
# # # print(lst)
# # # #4
# # # x = 15
# # # if x > 20:
# # #     print("Больше 20")
# # # else:
# # #     print("20 или меньше")
# # # #5
# # # car = {
# # # "brand": "Toyota",
# # # "year": 2020
# # # }
# # # print(car["brand"])
# # # #6
# # # for num in  range(1,6):
# # #     print(num)
# # # #7
# # # n = 3
# # # text = "Hello"
# # # while n > 0:
# # #     print(text)
# # #     n -= 1
# # # #8
# # # with open("test.txt", "w", encoding="utf-8") as file:
# # #     file.write("Тест записи")
# # # #9
# # # def is_positive(n):
# # #     return n > 0
# # # print(is_positive(-5))
# # # #10
# # # class Dog:
# # #     def __init__(self, name):
# # #         self.name = name
# # #     def bark(self):
# # #         print("Гав!")
# # #     def change_name(self, new_name):
# # #         self.name = new_name
# # # d = Dog("gh")
# # # ###########################################################
# # # #1
# # # a = 5
# # # b = 2.5
# # # c = "3"
# # # c = int(c)
# # # print(a + b + c)
# # # #2
# # # s = "автоматизация"
# # # s = s.replace("а", "@")
# # # s = s.upper()
# # # print(s)
# # # #3
# # # numbers = [4, 7, 1, 9, 3]
# # # numbers.sort()
# # # result = numbers[0] + numbers[-1]
# # # print(numbers)
# # # print(result)
# # # #4
# # # age = 19
# # # result1 = "Доступ запрещён" if age < 18 else "Доступ разрешён"
# # # print(result1)
# # # #5
# # # student = {
# # # "name": "Илья",
# # # "grades": [5, 4, 3]
# # # }
# # # student["grades"].append(5)
# # # print(student)
# # # #6
# # # fruits = ["яблоко", "банан", "апельсин"]
# # # print(f"Фрукт: {fruits[0]}, длинна: {len(fruits[0])}")
# # # print(f"Фрукт: {fruits[1]}, длинна: {len(fruits[1])}")
# # # print(f"Фрукт: {fruits[2]}, длинна: {len(fruits[2])}")
# # # #7
# # # n = 4
# # # while n >= 1:
# # #     print(n)
# # #     n -= 1
# # # #8
# # # with open("log.txt", "w", encoding="utf-8") as file:
# # #     file.write("21:58 22.06.2025")
# # # with open("log.txt", "r", encoding="utf-8") as file:
# # #     result = file.read()
# # # print(result)
# # # #9
# # # def is_even(n):
# # #     return n %2==0
# # # print(is_even(6))
# # # #10
# # # class Book:
# # #     def __init__(self, title, author, pages):
# # #         self.title = title
# # #         self.author = author
# # #         self.pages = pages
# # #     def info(self):
# # #         print(f"Книга: {self.title}, Автор: {self.author}")
# # #     def is_thick(self):
# # #         return self.pages > 300
# # # b = Book("rtgrt","rtg",2282)
# # # b.info()
# # # print(b.is_thick())
# # # #11
# # # import random
# # # n = 5
# # # numbers  = [random.randint(1,100) for _ in range(n)]
# # # with open("numbers.txt", "w", encoding="utf-8") as file:
# # #     for num in numbers:
# # #      file.write(f"{num}\n")
# # # with open("numbers.txt", "r", encoding="utf-8") as file:
# # #     result = file.read()
# # # print(result)
# # # #################################################
# # # #1
# # # a = 7
# # # b = 3.5
# # # c = "5"
# # # print(a + b + int(c))
# # # #2
# # # s = "декоратор"
# # # s = s.replace("о", "0")
# # # s = s.upper()
# # # print(s)
# # # #3
# # # numbers = [8, 3, 12, 5, 9]
# # # numbers.sort()
# # # min_num = numbers[0]
# # # max_num = numbers[-1]
# # # result = max_num - min_num
# # # print(f"Отсортированный список {numbers}")
# # # print(f"Разница между первым и последним {result}")
# # # #4
# # # score = 85
# # # if score >= 90:
# # #     print("Отлично")
# # # elif score >= 70:
# # #     print("Хорошо")
# # # elif score >= 50:
# # #     print("Удовлетворительно")
# # # else:
# # #     print("Неудовлетворительно")
# # # #5
# # # movie = {
# # # "title": "название",
# # # "year": 2025
# # # }
# # # movie["rating"] = 8.5
# # # print(movie)
# # # #6
# # # colors = ["красный", "зелёный", "синий"]
# # # for color in colors:
# # #     print(f"Цвет: {color}, букв: {len(color)}")
# # # #7
# # # n = 5
# # # total = 1
# # # while total <= n:
# # #     print(total)
# # #     total +=2
# # # #8
# # # with open("data.txt", "w", encoding="utf-8") as file:
# # #     file.write("Тест декораторов")
# # # with open("data.txt", "r", encoding="utf-8") as file:
# # #     result = file.read()
# # #     print(result)
# # # #9
# # # def multiply(a, b):
# # #     print(a * b)
# # # multiply(5, 5)
# # # #10
# # # def uppercase(func):
# # #     def wrapper():
# # #         result = func()
# # #         return result.upper()
# # #     return wrapper
# # # @uppercase
# # # def say_hello():
# # #     return "hello"
# # #
# # # print(say_hello())
# # # #11
# # # class Car:
# # #     def __init__(self, brand, speed = 0):
# # #         self.brand = brand
# # #         self.speed = speed
# # #     def accelerate(self):
# # #         self.speed += 10
# # # c = Car("kgfyjk")
# # # c.accelerate()
# # # c.accelerate()
# # # print(c.speed)
# # # #12
# # # import random
# # #
# # # n = 5
# # # random_numbers = [random.randint(10,50) for _ in range(n)]
# # # with open("random_numbers.txt", "w", encoding="utf-8") as file:
# # #     for num in random_numbers:
# # #      file.write(f"{num}\n")
# # # with open("random_numbers.txt", "r", encoding="utf-8") as file:
# # #     result = file.read()
# # # print(result)
# # # #################################################################
# # # #1
# # # a = 10
# # # b = "3.72"
# # # b = float(b)
# # # print(f"{a + b:.1f} ")
# # # ############################################
# # # #1
# # # name = "Илья"
# # # age = 33
# # # print(f"Меня зовут {name}, мне {age} лет")
# # # #2
# # # a = 5
# # # b = 3
# # # print(f"Сумма: {a + b}")
# # # print(f"Разность: {a - b}")
# # # print(f"Произведение: {a * b}")
# # # #3
# # # s = "Привет"
# # # print(f"Длинна: {len(s)}")
# # # print(f"Первый символ: {s[0]}")
# # # print(f"Последний символ: {s[-1]}")
# # # #4
# # # numbers = [1, 2, 3]
# # # numbers.append(4)
# # # del numbers[0]
# # # print(numbers)
# # # #5
# # # x = 10
# # # if x > 5:
# # #     print("Больше 5")
# # # else:
# # #     print("5 или меньше")
# # # #6
# # # for num in range(1,6):
# # #  print(num)
# # #  #7
# # # x = 3
# # # while x >= 1:
# # #     print(x)
# # #     x -= 1
# # # #8
# # # student = {
# # # "name": "Илья",
# # # "age": 33
# # # }
# # # print(student)
# # # #9
# # # def square(n):
# # #     return n**2
# # # print(square(5))
# # # #10
# # # with open("test.txt", "w", encoding="utf-8") as file:
# # #     file.write("Это тест")
# # # ########################################################
# # # #1
# # # city = "Архангельск"
# # # population = 165000
# # # print(f"Город: {city}, Население: {population} человек")
# # # #2
# # # a = 8
# # # b = 2
# # # print(a / b)
# # # print(a % b)
# # # #3
# # # s = "питон"
# # # s = s.capitalize()
# # # s = s + " - это язык программирования"
# # # print(s)
# # # #4
# # # fruits = ["яблоко", "груша"]
# # # fruits.insert(1,"апельсин")
# # # del fruits[-1]
# # # print(fruits)
# # # #5
# # # temperature = 25
# # # if temperature >= 30:
# # #     print("Жарко")
# # # elif temperature <= 10:
# # #     print("Холодно")
# # # else:
# # #     print("Нормально")
# # # #6
# # # for num in range(1,6):
# # #     print(num**2)
# # # #7
# # # n = 4
# # # total = 1
# # # while total <= n:
# # #     print(f"Итерация {total}")
# # #     total +=1
# # # #8
# # # movie = {
# # #     "title": "название",
# # #     "year": 2020
# # # }
# # # movie["rating"] = 10
# # # print(movie)
# # # #9
# # # def is_negative(n):
# # #     return n > 0
# # # print(is_negative(5))
# # # #10
# # # with open("notes.txt", "w", encoding="utf-8") as file:
# # #     file.write("Мои заметки")
# # # #11
# # # class Cat:
# # #     def __init__(self, name):
# # #         self.name = name
# # #     def meow(self):
# # #         print("Мяу!")
# # # c = Cat("мурзик")
# # # c.meow()
# # # #12
# # # def bold(func):
# # #     def wrapper():
# # #         result = func()
# # #         return f"**{result}**"
# # #     return wrapper
# # # @bold
# # # def say_hi():
# # #     return "Привет"
# # #
# # # print(say_hi())
# # # #######################################################
# # # #1
# # # product = "Товар"
# # # priceprice = 10
# # # quantity = 10
# # # print(f"Товар: {product}, Сумма: {price * quantity} руб.")
# # # #2
# # # a = 15
# # # b = 4
# # # print(a / b)
# # # print(a % b)
# # # print(a %2 ==0)
# # # #3
# # # s = "КОД"
# # # s = s.lower()
# # # x = 3
# # # total = 1
# # # while total < n:
# # #     total += 1
# # #     print(s)
# # # #4
# # # nums = [5, 2, 8, 2]
# # # uniq = list(set(nums))
# # # uniq.sort()
# # # print(uniq)
# # # #5
# # # num = 7
# # # if 5 <= num <= 10:
# # #     print("В диапазоне")
# # # else:
# # #     print("Вне диапазона")
# # # #6
# # # words = ["яблоко", "груша", "апельсин"]
# # # for word in words:
# # #     print(f"{word} - {len(word)} букв")
# # # #7
# # # for num in range(10, 0, -1):
# # #     print(num)
# # # #8
# # # user = {
# # #     "login": "логин",
# # #     "password": "****"
# # # }
# # # print(user.keys())
# # # #9
# # # def circle_area(r):
# # #     return 3.14 * (r**2)
# # # result = circle_area(5)
# # # print(result)
# # # #10
# # # with open("data.txt", "w", encoding="utf-8") as file:
# # #     for num in range(1,6):
# # #      file.write(f"{num}\n")
# # # #11
# # # class Dog:
# # #     def __init__(self, name):
# # #         self.name = name
# # #     def bark(self):
# # #         print(f"{self.name} говорит Гав!")
# # # d = Dog("тузик")
# # # d.bark()
# # # #12
# # # # text = input("Введите число: ")
# # # # if text != int:
# # # #     print("Некорректное значение")
# # # # else:
# # # #   print(f"{text ** 2}")
# # # ##############################################################
# # # #1
# # # city = "Архангельск"
# # # population = 165
# # # print(f"В городе {city} проживает {population} млн человек")
# # # #2
# # # a = 7
# # # b = 3
# # # print(f"{a / b: .2f}")
# # # print(a / b ==0)
# # # #3
# # # s = "программирование"
# # # s = s.capitalize()
# # # s = s.replace("р", "*")
# # # print(s)
# # # #4
# # # nums = [4, 7, 1, 4, 9]
# # # uniq = list(set(nums))
# # # result = sum(uniq)
# # # print(uniq)
# # # print(result)
# # # #5
# # # age = 17
# # # result = "Доступ разрешен" if age >= 18 else "Доступ запрещен"
# # # print(result)
# # # #6
# # # fruits = ["яблоко", "банан", "киви"]
# # # count = 0
# # # for fruit in fruits:
# # #     count += 1
# # #     print(f"Фрукт {count}: {fruit}, длина: {len(fruit)}")
# # # #7
# # # power = 1
# # # while power <= 1000:
# # #     print(power)
# # #     power *= 2
# # # #8
# # # book = {
# # #     "title": "название",
# # #     "author": "Автор"
# # # }
# # # book["year"] = 2020
# # # print(book)
# # # #9
# # # def is_palindrome(word):
# # #     print( word[::-1] == word)
# # # is_palindrome("топот")
# # # #10
# # # with open("diary.txt", "w", encoding="utf-8") as file:
# # #     file.write("ghj\nrtg\nrtgrt")
# # # with open("diary.txt", "r", encoding="utf-8") as file:
# # #     result = file.readlines()
# # #     line_count = len(result)
# # # print(line_count)
# # # #11
# # # class BankAccount:
# # #     def __init__(self, balance = 0):
# # #         self.balance = balance
# # #     def deposit(self, amount):
# # #         self.balance += amount
# # #     def check_balance(self):
# # #         print(self.balance)
# # # b = BankAccount()
# # # b.check_balance()
# # # b.deposit(100)
# # # b.check_balance()
# # # ###############################################################
# # # #2
# # # num = [x**2 for x in range(1,21) if x % 3==0 and x % 9 != 0]
# # # print(num)
# # # #3
# # # with open("data.txt", "w", encoding="utf-8") as file:
# # #     for x in range(10,21):
# # #      file.write(f"{x}\n")
# # # sun_num = 0
# # # with open("data.txt", "r", encoding="utf-8") as file:
# # #     for line in file:
# # #         num = int(line.strip())
# # #         if num % 2 == 0:
# # #             sun_num += num
# # # print(sun_num)
# # # ##################################################
# # # #1
# # # name = "Илья"
# # # age = 33
# # # def age_suffix(age):
# # #     if age % 100 in [11, 12, 13, 14]:
# # #         return 'лет'
# # #     elif age % 10 == 1:
# # #         return 'год'
# # #     elif age % 10 in [2, 3, 4]:
# # #         return 'года'
# # #     else:
# # #         return 'лет'
# # # print(f"Меня зовут {name}, мне {age} {age_suffix(age)}.")
# # # #2
# # # a = 15
# # # b = 4
# # # print(a // b)
# # # print(a % b)
# # # #3
# # # s = "Программирование"
# # # print(len(s))
# # # print(f"{s[0]} {s[-1]} {s[2:7]}")
# # # #4
# # # numbers = [5, 2, 8, 1, 9]
# # # numbers.append(10)
# # # del numbers[1]
# # # print(numbers)
# # # #5
# # # x = 12
# # # result = "Больше 10" if x > 10 else "10 или меньше"
# # # print(result)
# # # #6
# # # for num in range(1,6):
# # #  print(f"Число: {num}, Квадрат: {num**2}")
# # # #7
# # # x = 5
# # # while x >= 1:
# # #     print(x)
# # #     x -= 1
# # # #8
# # # book = {
# # # "title": "Автор",
# # # "author": "Название"
# # # }
# # # print(book["author"])
# # # #9
# # # def is_even(n):
# # #      return n %2 ==0
# # # print(is_even(3))
# # # #10
# # # with open("test.txt", "w", encoding="utf-8") as file:
# # #     file.write("Это тестовый файл")
# # #11
# # from selenium.webdriver.support.expected_conditions import title_is
# #
# # from lesson1 import total
# # from lesson2 import age_str
# # from lesson3 import result
# #
# #
# # # class Dog:
# # #     def __init__(self, name):
# # #         self.name = name
# # #     def bark(self):
# # #         print("Гав!")
# # # d = Dog
# # #12
# # # n = 4
# # # total = []
# # # while total <= n:
# # #     print(total)
# # #     total += 1
# # # with open("numbers.txt", "w", encoding="utf-8") as file:
# # #     file.write(f"{total}")
# # # with open("numbers.txt", "r", encoding="utf-8") as file:
# # #     result = file.read()
# # # print(result)
# # # print(sum(int(result)))
# # ###################################################################
# # # a = 10
# # # b = 3
# # # print(f"{a / b:.2f}")
# # # ##
# # # x = 1
# # # total = 5
# # # while total >= x:
# # #     print(total)
# # #     total -= 1
# # # ##
# # # def square(n):
# # #     return n**2
# # # print(square(5))
# # # ##1
# # # product = "Конфета"
# # # price = 55
# # # in_stock = True
# # # print(f"Товар: {product}, Цена: {price} руб., В наличии: {"Да" if in_stock else "Нет"}")
# # # #2
# # # s = "КОД"
# # # s = s.lower()
# # # for _ in range(3):
# # #  print(s)
# # # #3
# # # numbers = [3, 1, 4, 1, 5]
# # # numbers2 = list(set(numbers))
# # # numbers2.sort()
# # # print(numbers2)
# # # #3
# # # with open("data.txt", "w", encoding="utf-8") as file:
# # #     for num in range(10,21):
# # #      file.write(f"{num}\n")
# # # with open("data.txt", "r", encoding="utf-8") as file:
# # #     lines = file.readlines()  # Явно используем readlines()
# # #     numbers = [int(line.strip()) for line in lines]  # Преобразуем строки в числа
# # #     even_sum = sum(num for num in numbers if num % 2 == 0)  # Суммируем чётные
# # #
# # # print(f"Сумма чётных чисел: {even_sum}")
# #
# # ##################################################################################
# # # a = 5
# # # b = 3.14
# # # print(a + b)
# # # #2
# # # x = "Python"
# # # print(x[0])
# # # print(x[-1])
# # # print(len(x))
# # # #3
# # # x = [1, 2, 3, 4, 5]
# # # x.append(6)
# # # del x[1]
# # # print(x)
# # # #4
# # # # try:
# # # #  x = int(input("введите число: "))
# # # #  if x > 10:
# # # #       print("Больше 10")
# # # #  else:
# # # #       print("10 или меньше")
# # # # except ValueError:
# # # #  print("Нужно ввести число")
# # # #5
# # # text = {"name": "Alice", "age": 25}
# # # text["city"] = "New York"
# # # print(text["age"])
# # # print(text)
# # # #6
# # # for num in range(2,11,2):
# # #     print(num)
# # # #7
# # # with open("numbers.txt", "w", encoding="utf-8") as file:
# # #     for num in range(1,6):
# # #      file.write(f"{num}\n")
# # # #8
# # # # def multiply(a, b):
# # # #     return a * b
# # # # print(multiply(5,5))
# # # # #10
# # # # class Dog:
# # # #     def __init__(self, name, __age = 0):
# # # #         self.name = name
# # # #         self.age = __age
# # # #     def bark(self):
# # # #         print(f"{self.name} лает!")
# # # #     def set_age(self, new_age):
# # # #         self.age = new_age
# # # #     def get_age(self):
# # # #         print(self.age)
# # # # d = Dog("dfv")
# # # # d.bark()
# # # #1
# # # nums = [10, 20, 30, 40]
# # # nums.append(50)
# # # del  nums[1]
# # # print(nums)
# # # #2
# # # letters = ['a', 'b', 'c', 'd', 'e']
# # # print(letters[:3])
# # # print(letters[:1])
# # # print(letters[::2])
# # # #3
# # # # fruits = ['apple', 'banana', 'cherry', 'apple']
# # # # ind = fruits.index("apple")
# # # # fruits = fruits('banana', 'orange')
# # # # del fruits[-1]
# # # # #4
# # # num = []
# # # for nums in range(2,21,2):
# # #     num.append(nums)
# # # print(num)
# # # #5
# # # # num = []
# # # # numbers = [15, 7, 22, 4, 30, 9]
# # # # for num in numbers:
# # # #     if numbers > 10:
# # #
# # # #6
# # # data = [3, 1, 4, 1, 5, 9, 2]
# # # data.sort()
# # # print(data[::-1])
# # # #7
# # #################################################
# # # #1
# # # a = 5
# # # b = 2.5
# # # print(a + b)
# # # #2
# # # text = "Python"
# # # text = text[::-1]
# # # for result in text:
# # #     print(result)
# # # #3
# # # num = []
# # # numbers = [1, 2, 3, 4, 5]
# # # for num in numbers:
# # #     num += 1
# # #     print(num)
# # # #4
# # # x = 5
# # # if x > 0:
# # #     print("Положительное")
# # # elif x < 0:
# # #     print("Отрицательное")
# # # else:
# # #     print("Ноль")
# # # #5
# # # pro = {
# # # "name": "fgg",
# # # "age": 55,
# # # "city": "lkklk"
# # # }
# # # print(pro["age"])
# # # #6
# # # n = 5
# # # total = 1
# # # while total <= n:
# # #     print(total)
# # #     total += 1
# # # #7
# # # with open("numbers.txt", "w", encoding="utf-8") as file:
# # #     for num in range(1,6):
# # #      file.write(f"{num}\n")
# # # #8
# # # def multiply(a, b):
# # #     return a * b
# # # print(multiply(5,5))
# # # #9
# # # def uppercase(func):
# # #     def wrapper():
# # #         result = func()
# # #         return result.upper()
# # #     return wrapper
# # # @uppercase
# # # def great():
# # #     return "hello"
# # # print(great())
# # # #10
# # # class Person:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age
# # #     def greet(self):
# # #         print(f"Привет, меня зовут {self.name}!")
# # # p = Person("hgf",55)
# # #########################3
# # #1
# # # a = 5
# # # b = "Hello"
# # # print(f"{a}, {b}")
# # # #2
# # # text = "Python is awesome"
# # # print(len(text))
# # # print(text.upper())
# # # #3
# # # numbers = [1, 2, 3, 4, 5]
# # # numbers.append(6)
# # # del  numbers[1]
# # # print(numbers)
# # # #4
# # # x = 10
# # # if x %2 ==0:
# # #     print("Чётное")
# # # else:
# # #     print("Нечётное")
# # # #5
# # # student = {"name": "Alice", "age": 20, "grade": "A"}
# # # student["city"] = "New York"
# # # print("age")
# # # #6
# # # for num in range(2,11,2):
# # #     print(num)
# # # #7
# # # with open("test.txt", "w", encoding="utf-8") as file:
# # #     file.write("Hello, file!")
# # # #8
# # # def multiply(a, b):
# # #     return a * b
# # # print(multiply(3,4))
# # # #9
# # # def uppercase(func):
# # #     def wrapper():
# # #      result = func()
# # #      return result.upper()
# # #     return wrapper
# # # @uppercase
# # # def greet():
# # #     return "hello"
# # # print(greet())
# # # #10
# # # class Dog:
# # #     def __init__(self, name):
# # #         self.name = name
# # #     def bark(self):
# # #         print(f"Woof! My name is {self.name}")
# # # d = Dog("erfv")
# # # d.bark()
# # #######################################
# # # #1
# # # a = 8
# # # b = 5.4
# # # print(a + b)
# # # #2
# # # text = "Python"
# # # print(text[::-1])
# # # #3
# # # num = [3, 7, 1, 9, 2]
# # # num.sort()
# # # print(num[-1])
# # # #4
# # # x = 5
# # # if x %2==0:
# # #     print("Чётное")
# # # else:
# # #     print("Нечётное")
# # # #5
# # # fruits = {"яблоко": 50, "банан": 30, "апельсин": 40}
# # # maximum = max(fruits.keys())
# # # print(maximum)
# # # #6
# # # for num in range(1, 11):
# # #     print(num)
# # # #7
# # # with open("numbers.txt", "w", encoding="utf-8") as file:
# # #     for num in range(1,6):
# # #         file.write(f"{num}\n")
# # # #8
# # # def multiply(a, b):
# # #     return a * b
# # # print(multiply(5,5))
# # # #9
# # # def repeat_twice(func):
# # #     def wrapper():
# # #         result = func()
# # #         return func() * 2
# # #     return wrapper
# # # @repeat_twice
# # # def greet():
# # #     return "trrrr"
# # # print(greet())
# # # #10
# # # class Dog:
# # #     def __init__(self, name):
# # #         self.name = name
# # #     def bark(self):
# # #         print("Гав!")
# # # d = Dog("sgf")
# # # d.bark()
# # #########################################
# # # #1
# # # a = 5
# # # b = 3.14
# # # print(a + b)
# # # #2
# # # text = "Привет, мир!"
# # # print(len(text))
# # # print(text.upper())
# # # #3
# # # numbers = [1, 2, 3, 4, 5]
# # # numbers.append(6)
# # # print(numbers)
# # # #4
# # # # num = int(input("Введите число: "))
# # # # if num %2==0:
# # # #     print("Четное")
# # # # else:
# # # #     print("Нечетное")
# # # #5
# # # student = {"name": "Алексей", "age": 20, "group": "A-101"}
# # # print(f"Имя студента: {student["name"]}")
# # # student["grades"] = [4, 5, 3]
# # # print(student)
# # # #6
# # # nums = [1, 2, 3, 4, 5]
# # # num = []
# # # for num in nums:
# # #       print(num ** 2)
# # # #7
# # # with open("notes.txt", "w", encoding="utf-8") as file:
# # #     file.write("Это моя первая запись.")
# # # #8
# # # def multiply(a, b):
# # #     return a * b
# # # print(multiply(4,4))
# # # #9
# # # def uppercase(func):
# # #     def wrapper():
# # #         resalt = func()
# # #         return resalt.upper()
# # #     return wrapper
# # # @uppercase
# # # def greet():
# # #     return "Привет"
# # # print(greet())
# # # #10
# # # class Car:
# # #     def __init__(self, brand, model):
# # #         self.brand = brand
# # #         self.model = model
# # #     def start_engine(self):
# # #         print("Двигатель запущен")
# # # c = Car("Бренд", "Модель")
# # # print(c.brand)
# # # print(c.model)
# # # c.start_engine()
# # ####################################################
# # #1
# # # with open("numbers.txt", "w", encoding="utf-8") as file:
# # #     for num in range(1, 101):
# # #      file.write(f"{num}\n")
# # # with open("numbers.txt", "r", encoding="utf-8") as file:
# # #     numbers = [int(line.strip())for line in file]
# # #     result = sum(numbers)
# # # print(numbers)
# # # with open("even.txt", "w", encoding="utf-8") as even_file:
# # #     for num in numbers:
# # #         if num %2==0:
# # #             even_file.write(f"{num}\n")
# # # with open("odd.txt", "w", encoding="utf-8") as odd_file:
# # #     for num in numbers:
# # #         if num %2!=0:
# # #             odd_file.write(f"{num}\n")
# # # class FileManager:
# # #     def
# # ##############################################################
# # # #1
# # # # name = input("Введите ваше имя: ")
# # # # age = input("Введите ваш возраст: ")
# # # # print(f"Привет, {name}! Тебе {age} лет.")
# # # #2
# # # text = "Python — это мощный язык программирования"
# # # print(text[::-1])
# # # #3
# # # numbers = [5, 2, 9, 1, 5, 6]
# # # numbers.sort()
# # # max_num = numbers[-1]
# # # min_num = numbers[0]
# # # #4
# # # # x = input("Введите число: ")
# # # # if int(x) %2==0:
# # # #     print("Чётное")
# # # # else:
# # # #     print("Нечётное")
# # # #5
# # # student = {"имя": "Илья",
# # #            "возраст": 33,
# # #            "курс": 0}
# # # print(student["курс"])
# # # #6
# # # for nun in range(1,11):
# # #     if nun !=5:
# # #      print(nun)
# # # #7
# # # with open("notes.txt", "w", encoding="utf-8") as file:
# # #     file.write("Это моя первая запись в файле.")
# # # #8
# # # def multiply(a, b):
# # #     return a * b
# # # print(multiply(5,5))
# # # #9
# # # def uppercase(func):
# # #     def wrapper():
# # #         result = func()
# # #         return result.upper()
# # #     return wrapper
# # # @uppercase
# # # def greet():
# # #     return "hello"
# # # print(greet())
# # # #10
# # # class Dog:
# # #     def bark(self):
# # #         print("Гав!")
# # # d = Dog()
# # # d.bark()
# # # #11
# # # class Dog:
# # #     def bark(self):
# # #         print("Гав!")
# # #     def __init__(self, name):
# # #         self.name = name
# # #     def get_name(self):
# # #         return self.name
# # # d = Dog("Бобик")
# # # d.bark()
# # # print(d.get_name())
# # ##################################################
# # #1
# # # a = 5
# # # b = 3.14
# # # print(a + b)
# # #2
# #
# # #3
# # # num = [1, 2, 3, 4, 5]
# # # del num[1]
# # # print(num)
# # # #9
# # # def uppercase(func):
# # #     def wrapper():
# # #         result = func()
# # #         return result.upper()
# # #     return wrapper
# # # @uppercase
# # # def text():
# # #     return "hello"
# # # print(text())
# # # #12
# # # class Animal:
# # #     def eat(self):
# # #         print("Ест")
# # # a = Animal()
# # # class Cat(Animal):
# # #     def meow(self):
# # #         print("Мяу!")
# # # c = Cat()
# # # c.eat()
# # # c.meow()
# # #############################################################
# # # #1
# # # name = "Илья"
# # # age = 33
# # # height = 1.8
# # # print(f"Меня зовут {name}, мне {age} лет, мой рост — {height} м.")
# # # #2
# # # text = "Python is awesome"
# # # print(len(text))
# # # print(text[-1])
# # # print(text.upper())
# # # #3
# # # numbers = [5, 2, 8, 1, 9]
# # # numbers.append(10)
# # # del  numbers[1]
# # # numbers.sort()
# # # print(numbers)
# # # #4
# # # # text = int(input("Введите число: "))
# # # # if text > 0:
# # # #     print("Число положительное")
# # # # elif text < 0:
# # # #     print("Число отрицательное")
# # # # elif text != int:
# # # #     print("Это не число")
# # # # else:
# # # #     print("Это ноль")
# # # #5
# # # student = {
# # # "name": "Илья",
# # # "age": 33,
# # # "courses": ["Python", "Math"]
# # # }
# # # print(student["courses"])
# # # #6
# # # n = 5
# # # total = 1
# # # while total <= n:
# # #     print(f"Число: {total}, Квадрат: {total ** 2}")
# # #     total +=1
# # # #7
# # # with open("notes.txt", "w", encoding="utf-8") as file:
# # #     file.write("Hello, file!")
# # # with open("notes.txt", "r", encoding="utf-8") as file:
# # #     result = file.read()
# # # print(result)
# # # #8
# # # def is_even(num):
# # #     return num %2==0
# # # print(is_even(5))
# # #
# # # #9
# # # def uppercase(func):
# # #     def wrapper():
# # #         result = func()
# # #         return result.upper()
# # #     return wrapper
# # # @uppercase
# # # def say_hello():
# # #     return "hello"
# # # print(say_hello())
# # # #10
# # # class Person:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age
# # #     def introduce(self):
# # #         print(f"Меня зовут {self.name}, мне {self.age} лет.")
# # # p = Person("name", 5)
# # # print(p.name, p.age)
# # # p.introduce()
# # # #11
# # # class Student(Person):
# # #     def __init__(self, name, age, student_id):
# # #      super().__init__(name, age)
# # #      self.student_id = student_id
# # # s = Student("Илья", 33, "ST123")
# # # s.introduce()  # Метод из родительского класса
# # # print(s.student_id)
# # ######################################################
# # # #1
# # # # num1 = int(input("Введите целое число: "))
# # # # num2 = float(input("Введите дробное число:"))
# # # # print(num1+num2)
# # # #2
# # # text = "Python"
# # # result = " ".join(text.upper())
# # # print(result)
# # # #3
# # # num = [1, 2, 3, 4, 5]
# # # nums = []
# # # for x in num:
# # #     nums.append(x + 1)
# # # print(nums)
# # # #4
# # # x = 4
# # # if x %2==0:
# # #     print("Четное")
# # # elif x %2!=0:
# # #     print("Нечетное")
# # # else:
# # #     print("Это ноль")
# # # #5
# # # my = {
# # # 'name': "dfv",
# # # 'age': 55,
# # # 'city': "dfv"
# # # }
# # # print(my['age'])
# # # #6
# # # for num in range(5, 0, -1):
# # #     print(num)
# # # #7
# # # with open("numbers.txt", "w", encoding="utf-8") as file:
# # #     for num in range(1,6):
# # #      file.write(f"{num}\n")
# # # #8
# # # def is_positive(num):
# # #     return num >0
# # # print(is_positive(5))
# # # #9
# # # def repeat_twice(func):
# # #     def wrapper():
# # #         result = func()
# # #         return  result * 2
# # #     return wrapper
# # # @repeat_twice
# # # def info():
# # #     return "qwerty"
# # # print(info())
# # #10
# # # class Car:
# # #     def __init__(self, color):
# # #         self.color = color
# # #     def start_engine(self):
# # #         print("Двигатель запущен")
# # # c = Car("red")
# # # c.start_engine()
# # # class ElectricCar(Car):
# # #     def __init__(self, color, battery_level):
# # #         super().__init__(color)
# # #         self.battery_level = battery_level
# # # e = ElectricCar("dsf", 50)
# # # e.start_engine()
# # ###########################################################
# # #1
# # # name = str(input("Введите имя: "))
# # # age = int(input("Введите возраст: "))
# # # print(f"Привет, {name}! Тебе {age} лет.")
# # #2
# # # text = "Python — это мощный язык программирования"
# # # print(text[:7], text[-6:])
# # # #3
# # # num = [10, 20, 30, 40, 50]
# # # nums = []
# # # for i in num:
# # #     nums.append(i + 1)
# # # print(nums)
# # # #4
# # # x = int(input("Введите число: "))
# # # if x % 2==0:
# # #     print("Чётное")
# # # else:
# # #     print("Нечетное")
# # # #5
# # # fruits = {"яблоко": 100, "банан": 80, "апельсин": 120}
# # # result = fruits.keys()
# # # fruits = result +10
# # #############################################
# # # #9
# # # def uppercase(func):
# # #     def wrapper():
# # #         result = func()
# # #         return result.upper()
# # #     return wrapper
# # # @uppercase
# # # def text():
# # #     return "привет"
# # # print(text())
# # # #10
# # # # class Dog:
# # # #     def __init__(self, name, age, breed):
# # # #         self.name = name
# # # #         self.age = age
# # # #         self.__breed = breed
# # # #     def bark(self):
# # # #         print(f"{self.name} says woof!")
# # # #     def set_breed(self, breed):
# # # #         self.__breed = breed
# # # #     def get_breed(self):
# # # #         print(self.__breed)
# # # # d = Dog("Тузик", 55, "q")
# # # # d.bark()
# # # # d.set_breed("erf")
# # # # d.get_breed()
# # # #7
# # # text = "Hello"
# # # n = 3
# # # print(text * n)
# # # #10
# # # def uppercase(func):
# # #     def wrapper():
# # #         result = func()
# # #         return result.upper()
# # #     return wrapper
# # # @uppercase
# # # def text():
# # #     return "Привет"
# # # print(text())
# # # #11
# # # class Cat:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.__age = age
# # #     def meow(self):
# # #         print("Мяу!")
# # #     def new_age(self, new):
# # #         self.__age = new
# # #     def get_age(self):
# # #         print(self.__age)
# # # c = Cat("hg", 4)
# # # c.new_age(8)
# # # c.get_age()
# # # #13
# # # class Animal:
# # #     def eat(self):
# # #         print("1")
# # # class Dog(Animal):
# # #     def bark(self):
# # #         print("2")
# # # d = Dog()
# # # d.eat()
# # # d.bark()
# # ##########################################
# # #7
# # # n  = 5
# # # while n > 0:
# # #     print("Hello")
# # #     n -= 1
# # # #9
# # # def is_even(n):
# # #     return n %2 ==0
# # # print(is_even(5))
# # # #10
# # # def uppercase(func):
# # #     def wrapper():
# # #         result = func()
# # #         return result.upper()
# # #     return wrapper
# # # @uppercase
# # # def text():
# # #     return "привет"
# # # print(text())
# # # #11
# # # class Book:
# # #     def __init__(self, title, author):
# # #         self.title = title
# # #         self.author = author
# # #     def info(self):
# # #         print(f"Книга: {self.title}, Автор: {self.author}")
# # # b = Book(55, "wd")
# # # class ChildBook(Book):
# # #     def __init__(self, title, author, age_limit):
# # #         super().__init__(title, author)
# # #         self.age_limit = age_limit
# # # c = ChildBook(4, "sd", "+6")
# # # print(c.title)
# # #######################################################
# # # #2
# # # x = "Python"
# # # print(x[::-1])
# # # #3
# # # num = [1, 2, 3, 4, 5]
# # # nums = []
# # # for x in num:
# # #     nums.append(x + 1)
# # # print(nums)
# # # #5
# # # fruit = {"яблоко": 50, "банан": 30, "апельсин": 40}
# # # fruit["банан"] += 10
# # # print(fruit)
# # # #
# # # for num in range(2,11,2):
# # #     print(num)
# # # #
# # # def uppercase(func):
# # #     def wrapper():
# # #         result = func()
# # #         return result.upper()
# # #     return wrapper
# # # @uppercase
# # # def text():
# # #     return "привет"
# # # print(text())
# # # #
# # # class Dog:
# # #     def __init__(self,name):
# # #         self.name = name
# # #     def  bark(self):
# # #         print("Гав!")
# # #     def get_name(self):
# # #         print(self.name)
# # # d = Dog("dvf")
# # # class Cat(Dog):
# # #     def bark(self):
# # #         print("Мяу!")
# # # c = Cat("k")
# # # c.bark()
# # # c.get_name()
# # ####################################
# # # class Person:
# # #     def __init__(self, name):
# # #         self.name = name
# # #     def greet(self):
# # #         print(f"Привет, меня зовут {self.name}!")
# # # class Student(Person):
# # #     def __init__(self, name, student_id):
# # #         super().__init__(name)
# # #         self.student_id = student_id
# # # s = Student("ilya", "545")
# # # print(s.student_id)
# # #
# # # def square(n):
# # #     return n **2
# # # print(square(5))
# # # #
# # # def greet(name, greeting="Привет"):
# # #     return f"{greeting}, {name}!"
# # # print(greet("hgf"))
# # # #
# # # def bold(func):
# # #     def wrapper():
# # #         result = func()
# # #         return f"<b>{result}</b>"
# # #     return wrapper
# # # @bold
# # # def say_hello():
# # #     return "Hello, World!"
# # # print(say_hello())
# # # #
# # # def multiply(a, b):
# # #     return a * b
# # # print(multiply(3, 5))
# # # #
# # # def is_positive(num):
# # #     return num > 0
# # # print(is_positive(5))
# # # #
# # # class Car:
# # #     def __init__(self, brand, color):
# # #         self.brand = brand
# # #         self.color = color
# # #     def info(self):
# # #         return (f"Это {self.color} {self.brand}")
# # #
# # # c = Car("bmw", "black")
# # # massage = c.info()
# # # print(massage)
# # # #
# # # class Dog:
# # #     def __init__(self, name):
# # #         self.name = name
# # #     def bark(self):
# # #         return f"{self.name} говорит: Гав!"
# # # dog = Dog("hgf")
# # # print(dog.bark())
# # # #
# # # class Book:
# # #     library_size = 0
# # #     def __init__(self, title):
# # #         self.title = title
# # #         Book.library_size +=1
# # #     def get_total(self):
# # #         return Book.library_size
# # # print(Book.library_size)
# # # book1 = Book("Война и мир")
# # # book2 = Book("1984")
# # # print(book1.get_total())
# # # #
# # # class Robot:
# # #     battery = 100
# # #     count = 0
# # #     def __init__(self, name):
# # #         self.name = name
# # #         Robot.count += 1
# # #     def greet(self):
# # #         return f"Я {self.name}. Уровень заряда: {self.battery}%"
# # #     def butt(self, pro):
# # #         if self.battery > pro:
# # #          self.battery -= pro
# # #
# # #
# # # r = Robot("gh")
# # # print(r.greet())
# # # print( Robot.count)
# # # r.butt(25)
# # # print(r.battery)
# # # #
# # # class Animal:
# # #     def eat(self):
# # #         print("Я ем")
# # # class Dog(Animal):
# # #     def bark(self):
# # #         print("Гав!")
# # # dog = Dog()
# # # dog.eat()  # Должно вывести "Я ем"
# # # dog.bark()
# # # #
# # # class Vehicle:
# # #     def move(self):
# # #         print("Транспорт движется")
# # # class Car(Vehicle):
# # #     def move(self):
# # #         super().move()
# # #         print(" по дороге")
# # # car = Car()
# # # car.move()
# # # #
# # # class Person:
# # #     def __init__(self, name):
# # #         self.name = name
# # # class Student(Person):
# # #     def __init__(self, name, student_id):
# # #         super().__init__(name)
# # #         self.student_id = student_id
# # # s = Student("jh", "56")
# # # print(s.name)
# # # print(s.student_id)
# # # #
# # # name = "ilya"
# # # age = 33
# # # price = 55.4
# # # print(type(name))
# # # print(type(age))
# # # print(type(price))
# # # #
# # # s = "Питон"
# # # print(s[0])
# # # print(s[-1])
# # # print(s[1:4])
# # # ##
# # # nums = [1, 2, 3]
# # # nums.append(4)
# # # del  nums[1]
# # # print(nums)
# # # #
# # # x = 5
# # # if x > 10:
# # #     print("Больше")
# # # else:
# # #     print("Меньше или равно")
# # # #
# # # person = {"name": "Анна", "age": 25}
# # # person["city"] =  "Москва"
# # # print(person["age"])
# # # #
# # # for x in range(1,6):
# # #
# # #         print(x)
# # # x = 1
# # # while x <= 5:
# # #     print(x)
# # #     x += 1
# # # #
# # # with open("test.txt", "w", encoding="utf-8") as file:
# # #     file.write("Hello!")
# # # with open("test.txt", "r", encoding="utf-8") as file:
# # #     result = file.read()
# # # print(result)
# # # #
# # # def is_even(n):
# # #     return n %2==0
# # # print(is_even(4))
# # # #
# # # for num in range(10,0,-1):
# # #  print(num)
# # # numbers = 0
# # # i = 1
# # # while i <= 100:
# # #     numbers += i
# # #     i +=1
# # # print(numbers)
# # # class Book:
# # #     def __init__(self, title, author):
# # #         self.title = title
# # #         self.author = author
# # #     def info(self):
# # #         print(self.title, self.author)
# # #     def is_thick(self):
# # #         return int(self.title) > 300
# # # b = Book(54, "h")
# # # b.info()
# # # print(b.is_thick())
# # # class EBook(Book):
# # #     def __init__(self, title, author, format):
# # #         super().__init__( title, author)
# # #         self.format = format
# # #     def info(self):
# # #         super().info()
# # #         print(self.format)
# # # e = EBook(55, "hjhhj", "a1")
# # # e.info()
# # #
# # # i = 0
# # # num = 0
# # # while i <= 100:
# # #     num +=i
# # #     i += 1
# # # print(num)
# # # #
# # # def repeat(n):
# # #     def decorator(func):
# # #         def wrapper(*args,**kwargs):
# # #             result = []
# # #             for _ in range(n):
# # #                 result.append(func(*args,**kwargs))
# # #             return result
# # #         return wrapper
# # #     return decorator
# # # @repeat(5)
# # # def text():
# # #     return "12"
# # # print(text())
# # #
# # # s = "automation"
# # # print(s[-3:])
# # # #
# # # def bold(func):
# # #     def wrapper():
# # #         result = func()
# # #         return f"<b>{result}</b>"
# # #     return wrapper
# # # @bold
# # # def text():
# # #     return "kfj"
# # # print(text())
# # # #
# # # class Person:
# # #     def __init__(self, name):
# # #         self.name = name
# # #     def greet(self):
# # #         return f"Hello, {self.name}!"
# # # class Student(Person):
# # #     def __init__(self, name, student_id):
# # #         super().__init__(name)
# # #         self.student_id = student_id
# # # s = Student("ilya", "a4")
# # # print(s.name, s.student_id)
# # #
# # # def get_evens(numbers):
# # #     num = []
# # #     for number in numbers:
# # #         if number %2==0:
# # #           num.append(number)
# # #     return num
# # #
# # # numbers = [1,2,3,4]
# # # print(get_evens(numbers))
# # # #
# # # with open("diary.txt", "w") as file:
# # #     file.write(f"Содержимое файла:\nСегодня прекрасный день.\nЯ изучаю Python!")
# # # with open("diary.txt", "r") as file:
# # #     result = file.read()
# # # print(result)
# # # #
# # # class Car:
# # #     def __init__(self,brand, color, engine_volume):
# # #         self.brand = brand
# # #         self.color = color
# # #         self.engine_volume = engine_volume
# # #         if engine_volume <= 0:
# # #             raise ValueError("Объем двигателя должен быть положительным")
# # #     def is_luxury(self):
# # #         return float(self.engine_volume) > 3.0
# # #     def info(self):
# # #         return f"{self.color} {self.brand}"
# # # c = Car("bmw", "red", -5.0)
# # # print(c.info())
# # # print(c.is_luxury())
# # #
# # # for num in range(1,6):
# # #     print(num**2)
# # # #
# # # result = []
# # # x = 1
# # # while x < 11:
# # #     if x%2==0:
# # #       result.append(x)
# # #     x += 1
# # # print(sum(result))
# # #1
# # # a = 7
# # # b = 3.14
# # # c = "hello"
# # # print(type(a))
# # # print(type(b))
# # # print(type(c))
# # # #2
# # # s = "automation"
# # # print(s[0])
# # # print(s[-1])
# # # print(s.upper())
# # # print(s[0:4])
# # # #3
# # # lst = [1, 2, 3]
# # # lst.append(4)
# # # del  lst[1]
# # # print(lst)
# # # #4
# # # x = 10
# # # if x > 10:
# # #     print("Больше 10")
# # # else:
# # #     print("10 или меньше")
# # # #5
# # # car = {"brand": "Toyota"}
# # # car["year"] = 2020
# # # car["brand"] = "Honda"
# # # print(car)
# # # #6
# # # for int in range(2,11,2):
# # #     print(int)
# # # x = 0
# # # q = 0
# # # while q < 5:
# # #     print(q)
# # #     q +=1
# # #     x += q
# # # print(x)
# # # #7
# # # with open("test.txt", "w") as file:
# # #     file.write("python")
# # # with open("test.txt", "r") as file:
# # #     result = file.read()
# # # print(result)
# # # #8
# # # def multiply(a, b):
# # #     return a * b
# # # print(multiply(5,5))
# # # #9
# # # def bold(func):
# # #     def wrapper():
# # #         result = func()
# # #         return f"<b>{result}<b>"
# # #     return  wrapper
# # # @bold
# # # def teg():
# # #     return "text"
# # # print(teg())
# # # #10
# # # class Dog:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age
# # #     def bark(self):
# # #         return "Гав!"
# # #     def is_puppy(self):
# # #         return self.age < 2
# # # d = Dog("bud", 5)
# # # print(d.is_puppy())
# # # print(d.bark())
# # # class Puppy(Dog):
# # #     def __init__(self, toys, name, age):
# # #         super().__init__(name, age)
# # #         self.toys = toys
# # #     def bark(self):
# # #         return "Тяф!"
# # # p = Puppy("ert","bud", 5)
# # # print(p.bark())
# # #1
# # # class Car:
# # #     wheels = 4
# # #     def __init__(self, brand):
# # #         self.brand = brand
# # #     def honk(self):
# # #         return  "Beep!"
# # # my_car = Car("Toyota")
# # # #6
# # # # id class
# # # # id method
# # # #7
# # # class Book:
# # #     def __init__(self, title, pages):
# # #         self.title = title
# # #         self.pages = pages
# # #     def info(self):
# # #         return f"{self.title}, {self.pages}"
# # # b = Book("rgv", "rt")
# # # print(b.info())
# # #
# # #1
# # # age = 7
# # # price = 2.4
# # # name = "tr"
# # # print(type(age))
# # # print(type(price))
# # # print(type(name))
# # # #2
# # # text = "Программирование"
# # # print(text[0])
# # # print(text[-5:])
# # # print(text.upper())
# # # #3
# # # numbers = [10, 20, 30, 40, 50]
# # # numbers.append(60)
# # # del numbers[1]
# # # print(len(numbers))
# # # #4
# # # # x = input("Введите число: ")
# # # # if int(x) %2==0:
# # # #     print("Чётное")
# # # # else:
# # # #     print("Нечётное")
# # # #5
# # # student = {"name": "Анна", "age": 20}
# # # student["group"] = "A1"
# # # student["age"] = 21
# # # print(student)
# # # #6
# # # for num in range(10,0,-1):
# # #     print(num)
# # # a = 0
# # # b = 0
# # # while b < 100:
# # #     b += 1
# # #     a += b
# # # print(a)
# # # #7
# # # with open("notes.txt", "w") as file:
# # #     file.write("Hello, Python!")
# # # with open("notes.txt", "r") as file:
# # #     result = file.read()
# # # print(result)
# # # #8
# # # def calculate(a, b):
# # #     return a + b, a * b
# # # print(calculate(5,5))
# # # #9
# # # def repeat(n):
# # #     def decorator(func):
# # #         def wrapper():
# # #             results = []
# # #             for _ in range(n):
# # #                 results.append(func())
# # #             return results
# # #         return wrapper
# # #     return decorator
# # # @repeat(2)
# # # def text():
# # #     return "abc"
# # # print(text())
# # # #10
# # # class Book:
# # #     def __init__(self, title, author):
# # #         self.title = title
# # #         self.author = author
# # #     def info(self):
# # #         return f"{self.title}, {self.author}"
# # #     def  is_thick(self):
# # #         return self.title >= 300
# # # b = Book(52,"yi")
# # # print(b.info())
# # # print(b.is_thick())
# # # class Car:
# # #     pass
# # # c = Car()
# # # #2
# # # class Car:
# # #     wheels = 4
# # #     def __init__(self, brand, color):
# # #         self.brand = brand
# # #         self.color = color
# # #     def info(self):
# # #         return f"Марка: {self.brand}, Цвет: {self.color}"
# # # c = Car("Toyota", "красный")
# # # print(c.info())
# # # print(c.wheels)
# # # #5
# # # #по 5 задаче выдаст ошибку, тюкю не опредилили обьект класса
# # # #7 задача, ошибка из за некоректно прописанного атрибута в ф строке
# # #
# # # class Lamp:
# # #     def __init__(self, is_on = False):
# # #         self.is_on = is_on
# # #     def switch(self):
# # #         self.is_on = not self.is_on
# # #     def status(self):
# # #         if self.is_on == True:
# # #             return ("Лампа включена")
# # #         else:
# # #             return ("Лампа выключена")
# # # l = Lamp()
# # # print(l.status())
# # # l.switch()
# # # print(l.status())
# # # class Student:
# # #     total_students = 0
# # #     def __init__(self, name):
# # #         Student.total_students += 1
# # #         self.name = name
# # #     def get_total(self):
# # #         return  Student.total_students
# # #
# # # print(Student.total_students)  # Должно вывести 0
# # # s1 = Student("Анна")
# # # s2 = Student("Петр")
# # # print(s1.get_total())
# # # class BankAccount:
# # #     def __init__(self, owner, balance = 0):
# # #         self.balance = balance
# # #         self.owner = owner
# # #     def deposit(self, amount):
# # #         self.balance += amount
# # #     def withdraw(self, amount):
# # #         if self.balance >= amount:
# # #             self.balance -= amount
# # #     def check_balance(self):
# # #         return f"{self.owner}, баланс: {self.balance} руб."
# # # account = BankAccount("Иван")
# # # account.deposit(1000)
# # # account.withdraw(500)
# # # print(account.check_balance())
# # # class Student:
# # #     total_students = 0
# # #     def __init__(self, name):
# # #         Student.total_students += 1
# # #         self.name = name
# # #         self.grades = []
# # #     def add_grade(self, grade):
# # #         self.grades.append(grade)
# # #     def get_average(self):
# # #         return  sum(self.grades) / len(self.grades)
# # # print(Student.total_students)
# # # student = Student("Анна")
# # # student.add_grade(5)
# # # student.add_grade(4)
# # # print(student.get_average())
# # #
# # # class Animal:
# # #     def __init__(self, name, species):
# # #         self.name = name
# # #         self.species = species
# # #     def make_sound(self):
# # #         pass
# # # class Dog(Animal):
# # #     def __init__(self, name, species, breed):
# # #         super().__init__(name, species)
# # #         self.breed = breed
# # #     def make_sound(self):
# # #         return "Гав!"
# # # class Cat(Animal):
# # #     def __init__(self, name, species):
# # #         super().__init__(name, species)
# # #     def make_sound(self):
# # #         return "Мяу!"
# # # dog = Dog("Бобик", "Собака", "Двортерьер")
# # # print(dog.make_sound())
# # # class Car:
# # #     def __init__(self, brand, color, mileage = 0):
# # #         self.brand = brand
# # #         self.color = color
# # #         self.mileage = mileage
# # #     def info(self):
# # #         return f"Это {self.color} {self.brand}"
# # #     def drive(self, km):
# # #         if int(km) > 0:
# # #          self.mileage += km
# # # car = Car("Kia", "синий")
# # # car.drive(150)
# # # print(car.mileage)
# # # age = 55
# # # price = 2.5
# # # name = "ilya"
# # # print(f"тип: {type(age)}, значение: {age}")
# # # print(f"тип: {type(price)}, значение: {price}")
# # # print(f"тип: {type(name)}, значение: {name}")
# # # #
# # # # num = input("Введите число: ")
# # # # if int(num) > 0:
# # # #     print("Положительное")
# # # # elif int(num) < 0:
# # # #     price("Отрицательное")
# # # # else:
# # # #     print("Ноль")
# # # #
# # # for num in range(2,21,2):
# # #     print(num)
# # # #
# # # fruits = ["яблоко", "банан", "апельсин"]
# # # fruits.append("киви")
# # # del  fruits[1]
# # # print(fruits)
# # # #
# # # def is_even(n):
# # #     return True if n %2==0 else False
# # # print(is_even(5))
# # # #
# # # with open("test.txt", "w") as file:
# # #     file.write("Привет, мир!")
# # # with open("test.txt", "r") as file:
# # #     result = file.read()
# # # print(result)
# # # #
# # # class Dog:
# # #     def __init__(self,name):
# # #         self.name = name
# # #     def bark(self):
# # #         return f"{self.name} говорит: Гав!"
# # # class Puppy(Dog):
# # #     def __init__(self,name):
# # #         super().__init__(name)
# # #     def play(self):
# # #         return f"{self.name} играет!"
# # # p = Puppy("hg")
# # # print(p.play())
# # # student = {
# # # "name": "ilya",
# # # "age": 55,
# # # "courses":[1,2,3]
# # # }
# # # print(student["age"])
# # # #
# # # # total = 0
# # # # while True:
# # # #     num = int(input("Введите число (0 для выхода): "))
# # # #     if num == 0:
# # # #         break
# # # #     total += num
# # # # print(f"Итогавая сумма {total}")
# # # #
# # # s = "Программирование"
# # # print(len(s))
# # # print(s[-4:])
# # # if "а" in s.lower():
# # #     print("Буква а есть")
# # # else:
# # #     print("Буквы а нет")
# # # #
# # # def multiply(a, b = 2):
# # #     return a * b
# # # print(multiply(4,))
# # # #
# # # x = []
# # # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # for num in numbers:
# # #     if num % 2 == 0:
# # #      x.append(num)
# # # print(x)
# # # #
# # # with open("test.txt", "a") as file:
# # #     file.write("\nЭто тестовый файл")
# # # with open("test.txt", "r") as file:
# # #     result = file.read()
# # # print(result)
# # # #
# # # class Rectangle:
# # #     def __init__(self, width, height):
# # #         self.width = width
# # #         self.height = height
# # #     def area(self):
# # #         return self.width * self.height
# # # r =Rectangle(4,5)
# # # print(r.area())
# # # class Square(Rectangle):
# # #     def __init__(self, side):
# # #         super().__init__(side, side)
# # #
# # # class Calculator:
# # #     operation_count = 0
# # #     def add(self, a , b):
# # #         Calculator.operation_count +=1
# # #         return a + b
# # #
# # #         operation_count +=1
# # #     def subtract(self, a, b):
# # #         Calculator.operation_count +=1
# # #         return a - b
# # #     def get_total_operations(self):
# # #         return Calculator.operation_count
# # #
# # # calc = Calculator()
# # # print(calc.add(5, 3))
# # # print(calc.add(5, 3))
# # # print(Calculator.operation_count)
# # #
# # # #
# # # # в 7 задаче отсутствует self
# # # #
# # # class Robot:
# # #     pass
# # # robo = Robot()
# # #
# # # class BankAccount:
# # #     def __init__(self, account_number, balance = 0):
# # #         self.account_number = str(account_number)
# # #         self.balance = balance
# # #     def deposit(self, amount):
# # #         self.balance += amount
# # #     def withdraw(self, amount):
# # #         if self.balance >= amount:
# # #             self.balance -= amount
# # #         else:
# # #             print("Недостаточно средств")
# # #     def check_balance(self):
# # #         return self.balance
# # # money = BankAccount("k55")
# # # print(money.check_balance())
# # # money.deposit(52)
# # # print(money.check_balance())
# # # money.withdraw(87)
# # # class Student:
# # #     count = 0
# # #     def __init__(self, name, grades= None):
# # #         self.name = name
# # #         self.grades = list(grades)
# # #         Student.count += 1
# # #     def add_grade(self, grade):
# # #         self.grades += [grade]
# # #     def get_average(self):
# # #         return sum(self.grades) / len(self.name)
# # # s = Student("Анна")
# # # s.add_grade(5)
# # # s.add_grade(4)
# # # print(s.get_average())
# # # name = "ilya"
# # # age = 33
# # # height = 1.8
# # # print(f"Меня зовут {name}, мне {age} лет, мой рост — {height} м.")
# # # #
# # # text = "Python"
# # # print(text[0])
# # # print(text[-1])
# # # print(text[1:4])
# # # #
# # # x = [1, 2, 3, 4, 5]
# # # x.append(6)
# # # del x[1]
# # # print(text)
# # # #
# # # x = 10
# # # if x > 10:
# # #     print("Больше 10")
# # # elif x < 10:
# # #     print("Меньше 10")
# # # else:
# # #     print("Равно 10")
# # # #
# # # student = {
# # # "name":"ilya",
# # # "age": 33,
# # # "courses": ["Math", "Physics", "Python"]
# # # }
# # # print(student["courses"])
# # # #
# # # for num in range(1,6):
# # #     print(num * 2)
# # # #
# # # with open("test.txt", "w", encoding="utf-8") as file:
# # #     file.write("Hello, Python!")
# # # #
# # # def multiply(a, b):
# # #     return a * b
# # # print(multiply(5,5))
# # # #
# # # def uppercase(func):
# # #     def wrapper():
# # #         result = func()
# # #         return result.upper()
# # #     return wrapper
# # # @uppercase
# # # def text():
# # #     return "ilya"
# # # print(text())
# # # #
# # # class Car:
# # #     def __init__(self, brand, model):
# # #         self.brand = brand
# # #         self.model = model
# # #     def info(self):
# # #         return f"Это {self.brand} {self.model}"
# # # c = Car("bmw", "red")
# # # print(c.info())
# # # class ElectricCar(Car):
# # #     def __init__(self, brand, model, battery_size):
# # #         super().__init__(brand, model)
# # #         self.battery_size = battery_size
# # # e = ElectricCar("bmw", "red", 55)
# # # print(e.info())
# # #1
# # # class Book:
# # #     def __init__(self, title):
# # #         self.title = title
# # #     def get_title(self):
# # #         return self.title
# # #
# # # my_book = Book("Преступление и наказание")
# # # print(my_book.get_title())
# # # #
# # # class Car:
# # #     wheels = 4
# # #     def __init__(self, brand, year):
# # #         self.brand = brand
# # #         self.year = year
# # #     def info(self):
# # #         return f"Марка: {self.brand}, Год: {self.year}, Колеса: {self.wheels}"
# # # car1 = Car("BMW", 2022)
# # # car2 = Car("Audi", 2021)
# # # print(car1.wheels)  # Должно вывести 4
# # # print(car2.wheels)
# # # car = Car("Ford", 2019)
# # # print(car.info())
# # # #
# # # class Animal:
# # #     def __init__(self, species):
# # #         self.species = species
# # #     def eat(self):
# # #         return "Животное ест"
# # # class Dog(Animal):
# # #     def __init__(self,species, name, breed,vaccinated = False):
# # #         super().__init__(species)
# # #         self.name = name
# # #         self._breed = breed
# # #         self.__vaccinated = vaccinated
# # #     def bark(self):
# # #         return "Гав-гав!"
# # #     def get_breed(self):
# # #         return self._breed
# # #     def eat(self):
# # #         return "Собака ест кость"
# # #     def set_vaccinated(self, status):
# # #         self.__vaccinated = status
# # # dog = Dog("Шарик", "Овчарка", "Собака")
# # # print(dog.get_breed())  # Овчарка
# # # dog.set_vaccinated(True)
# # # #
# # # class Bird:
# # #     def fly(self):
# # #         return "Птица летит"
# # #     def make_sound(self):
# # #         return "Чирик-чирик"
# # # class Duck(Bird):
# # #     def make_sound(self):
# # #         return "Кря-кря"
# # #     def swim(self):
# # #         return "Утка плавает"
# # # class Penguin(Bird):
# # #     def fly(self):
# # #         return "Пингвин не умеет летать"
# # # duck = Duck()
# # # penguin = Penguin()
# # # print(duck.fly())        # Птица летит
# # # print(duck.make_sound()) # Кря-кря
# # # print(penguin.fly())     # Пингвин не умеет летать
# # # print(penguin.make_sound())
# # #
# # # name = "Анна"
# # # age = 25
# # # print(f"Имя: {name}, Возраст: {age}")
# # # #2
# # # a = 10
# # # b = "20"
# # # c = 5.5
# # # print(type(a))
# # # print(type(b))
# # # print(type(c))
# # # #3
# # # result = (15 + 3) * 2 - 10 / 5
# # # print(result)
# # # #4
# # # x = 10
# # # y = 20
# # # result = True if x < y else False
# # # print(result)
# # # #5
# # # x = "123"
# # # x = int(x)
# # # result = x + 7
# # # print(result)
# # # #6
# # # # 1name = "A" допустимо
# # # # first_name = "B" допустимо
# # # # age@ = 10 недопустимо
# # # #7
# # # count = 5
# # # count = 10
# # # print(count)
# # # #8
# # # no = [100, [1, 2], 3.14, True]
# # # yes = "строка"
# # # yes = {"ключ": "значение"}
# # # #9
# # # a = "hello"
# # # b = "world"
# # # result = a == b
# # # print(result)
# # # #10
# # # x = 4
# # # y = 7
# # # result = x * y
# # # print(f"Площадь: {result}")
# # # #11
# # # # 2nd_place = "Silver"
# # # # total$ = 50.5  оба недопустимы
# # # #12
# # # data = [[1, 2], {"name": "Alex"}]
# # # #13
# # # x = "5.7"
# # # x = float(x)
# # # result = x * 2
# # # print(result)
# # # #14
# # # result = (2 ** 3) + (10 % 3)
# # # print(result)
# # # #15
# # # x = "100"
# # # y = 100
# # # result = x == y
# # # print(result)
# # # # разные типы данных
# # # #16
# # # score = "10"
# # # score = int(score)
# # # score = 15
# # # print(type(score), score)
# # # #17
# # #
# # # class Car:
# # #     wheels = 4
# # #     def __init__(self, model, color):
# # #         self.__model = model
# # #         self.color = color
# # #     def get_model(self):
# # #         return self.__model
# # #     def info(self):
# # #         return f"Это автомобиль {self.__model} цвета {self.color}"
# # #     def change_color(self, new_color):
# # #         self.color = new_color
# # #
# # # # bmw = Car()
# # # # print(bmw.wheels)
# # # ford = Car("Focus", "синий")
# # # audi = Car("A4", "чёрный")
# # # print(f"Модель: {ford.get_model()}, Цвет: {ford.color}")
# # # print(audi.info())
# # # car1 = Car("Model S", "красный")
# # # car2 = Car("Civic", "белый")
# # # tesla = Car("Model 3", "белый")
# # # tesla.change_color("синий")
# # # print(f"Модель: {tesla.get_model()}, Цвет: {tesla.color}")
# # #
# # # class ElectricCar(Car):
# # #     def __init__(self, model, color, battery_size):
# # #         super().__init__(model, color)
# # #         self.battery_size = battery_size
# # #     def info(self):
# # #         return f"Это автомобиль {self.get_model()} цвета {self.color}, батарея: {self.battery_size} kWh"
# # # tesla = ElectricCar("Model S", "красный", 100)
# # # print(tesla.info())
# #
# # # class Book:
# # #     library_name = "Central"
# # #     total_books = 0
# # #     def __init__(self, title, author):
# # #         self.title = title
# # #         self.author = author
# # #         Book.total_books += 1
# # #     def display_info(self):
# # #         return f"Книга: {self.title}, Автор: {self.author}, Библиотека: {Book.library_name}"
# # # library_1 = Book("jhg", "jhg")
# # # library_2 = Book("jgg", "hk")
# # # print(library_1.library_name)
# # # print(library_2.library_name)
# # # print(Book.library_name)
# # # print(Book.total_books)
# # # book = Book("1984", "Оруэлл")
# # # print(book.display_info())
# # #
# # age = 25
# # height = 1.75
# # name = "Alex"
# # print(f"{age}, {name}, {height}")
# # #
# # text = "Hello, World!"
# # print(text.upper())
# # print(text.lower())
# # #
# # numbers = [1, 2, 3, 4, 5]
# # numbers.append(6)
# # print(numbers)
# # #
# # x = 10
# # result = "Больше 5" if x > 5 else  "5 или меньше"
# # print(result)
# # #
# # person = {"name": "Alice", "age": 30}
# # print(person["age"])
# # #
# # word = "Python"
# # for text in word:
# #     print(text)
# # #
# # with open("test.txt", "w", encoding="utf-8") as file:
# #     file.write("This is a test file.")
# # #
# # def add(a, b):
# #     return a + b
# # print(add(5,5))
# # #
# # def uppercase(func):
# #     def wrapper(*args, **kwargs):
# #         result = func(*args, **kwargs)
# #         return result.upper()
# #     return wrapper
# # @uppercase
# # def text(name, age):
# #     return f"Hello {name}, {age} года"
# # print(text("Илья","33"))
# # # #
# # class Car:
# #     def __init__(self,color):
# #         self.color = color
# #     def start_engine(self):
# #         return "Engine started"
# # car = Car("red")
# # #
# # class ElectricCar(Car):
# #     def __init__(self, color, battery_level = 100):
# #         super().__init__(color)
# #         self.battery_level = battery_level
# #     def show_battery(self):
# #           return self.battery_level
# # electro = ElectricCar("black")
# # print(electro.color)
# # print(electro.start_engine())
# #
# # count = 5
# # name = "Alex"
# # is_active = True
# # print(type(count))
# # print(type(name))
# # print(type(is_active))
# # #
# # s = "Python"
# # print(s)
# # class Dog:
# #     def __init__(self,name, age = 1):
# #         self.name = name
# #         self.age = age
# #     def bark(self):
# #         return  "Гав!"
# # dog = Dog("Шарик")
# # print(dog.bark())
# # class Puppy(Dog):
# #     def __init__(self,name, age, toy =  "мячик"):
# #         super().__init__(name, age)
# #         self.toy = toy
# # p = Puppy("drrgr",55)
# # class Book:
# #     library_name = "City Library"
# #     def __init__(self, title, author):
# #         self.title = title
# #         self.author = author
# #     def get_info(self):
# #         return f"Название: {self.title}, Автор: {self.author}"
# #     def update_title(self, new_title):
# #         self.title = new_title
# # book = Book("title", "author")
# # print(book.get_info())
# # book.update_title("tit2")
# # print(book.get_info())
# # book1 = Book("1984","Оруэлл")
# # print(book1.get_info())
# # #
# # class Car:
# #     pass
# # c = Car()
# # from lesson3 import fruits
# #
#
# # class BankAccount:
# #     def __init__(self, balance = 0):
# #         self.__balance = balance
# #     def deposit(self, amount):
# #         self.__balance += amount
# #     def get_balance(self):
# #         return self.__balance
# # b= BankAccount()
# # print(b.get_balance())
# # class Animal:
# #     def make_sound(self):
# #         return "Some sound"
# #     def get_species(self):
# #         return "Animal"
#
# # class Dog(Animal):
# #     def __init__(self, name):
# #         self.name = name
# #     def make_sound(self):
# #         return "Гав!"
# #     def get_species(self):
# #         return "Собака"
# #     def info(self):
# #         return f"{self.name} {self.get_species()} {self.make_sound()}"
# #
# # class Cat(Animal):
# #     def __init__(self, name):
# #         self.name = name
# #     def make_sound(self):
# #         return "Мяу!"
# #     def get_species(self):
# #         return "Кошка"
# #     def info(self):
# #         return f"{self.name} {self.get_species()} {self.make_sound()}"
# # dog = Dog("Шарик")
# # cat = Cat("Барсик")
# # print(dog.make_sound())  # "Гав!"
# # print(cat.get_species())
# # print(dog.name)
# # print(cat.name)
# # print(dog.info())
# # print(cat.info())
# # class Vector:
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
# #     def __add__(self, other):
# #         # return Vector(self.x + other.x, self.y + other.y)
# #     def __str__(self):
# #         return f"Vector({self.x}, {self.y})"
# # v1 = Vector(2, 3)
# # v2 = Vector(1, 4)
# # v3 = v1 + v2
# # print(v3)
# # class Zoo(Animal):
# #     def __init__(self, animals = []):
# #         self.animals = animals
# #     def add_animal(self, animal):
# #         self.animals += animal
# #     def make_all_sounds(self):
# #         return Zoo.make_sound()
# # zoo = Zoo()
# # zoo.add_animal(Dog("Шарик"))
# # zoo.add_animal(Cat("Мурзик"))
# # print(zoo.make_all_sounds())
# # class Robot:
# #     pass
# # r = Robot()
# #
# # class Robot:
# #     power_source = "батарейка"
# #     def __init__(self, name):
# #         self.__name = name
# #     def greet(self):
# #         return f"Привет, я робот по имени {self.__name}"
# #     def get_name(self):
# #         return self.__name
# #     def set_name(self,new_name):
# #         if new_name != "":
# #          self.__name = new_name
# #         else:
# #             print("Ошибка: имя не может быть пустым")
# # r = Robot("Ilya")
# # r2 = Robot("R2-D2")
# # print(r2.greet())
# # r.set_name("")
# # r.set_name("name")
# # print(r.get_name())
# #
# # class Android(Robot):
# #     def __init__(self, name, os):
# #         super().__init__(name)
# #         self.os = os
# #     def greet(self):
# #         if self.os == "Android":
# #             return "Я робот на Android!"
# #         else:
# #             return super().greet()
# # r = Android("R2-D2", "iOS")
# # print(r.greet())  # "Привет, я робот по имени R2-D2"
# #
# # a = Android("C-3PO", "Android")
# # print(a.greet())
# #
# # class RobotTeam:
# #     def __init__(self, Robot, Android):
# #         self.Robot = Robot
# #         self.Android = Android
# #     def team_greet(self):
# # fruits = ["банан", "яблоко", "киви"]
# # print(fruits)
# #
# # numbers = [10, 20, 30, 40, 50]
# # print(numbers[2])
# #
# # animals = ["кошка", "собака"]
# # animals.append("птица")
# # animals[0] = "рыба"
# # print(animals)
# #
# # colors = ["красный", "синий", "зеленый"]
# # colors.insert(1,"желтый")
# # print(colors)
# #
# # items = ["книга", "ручка", "карандаш", "ластик"]
# # items.remove("карандаш")
# # print(items)
# # items.clear()
# # print(items)
# #
# # letters = ['a', 'b', 'c', 'd', 'e', 'f']
# # print(letters[1:5])
# #
# # list1 = [1, 2, 3]
# # list2 = [4, 5, 6]
# # list = list1 + list2
# # print(list)
# #
# # numbers = [5, 10, 15, 20]
# # numbers[1] = 25
# # numbers[3] = 30
# # print(numbers)
# #
# # shopping_list = []
# # shopping_list.append("хлеб")
# # shopping_list.append("молоко")
# # shopping_list.append("яйца")
# # print(shopping_list)
# #
# # languages = ['Python', 'Java', 'C++', 'JavaScript']
# # del languages[2]
# # print(languages)
# #
# # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# # print(alphabet[::2])
# #
# # x = 5
# # if x > 0:
# #     print("Число положительное")
# #
# # y = 4
# # result = "Чётное" if y % 2 == 0 else "Нечётное"
# # print(result)
# # t = 10
# # if t < 0:
# #     print("Холодно")
# # elif  0 <= t < 15:
# #      print("Прохладно")
# # elif 15 <= t < 25:
# #     print("Тепло")
# # else:
# #     print("Жарко")
# #
# # z = 12
# # if z % 2 == 0 and z % 3 == 0:
# #     print("Делится на 6")
# # else:
# #     print("Не делится")
# #
# # answer = ""
# # if answer.lower() == "да" or answer.lower() == "yes":
# #     print("Согласен")
# # elif answer.lower() == "нет" or answer.lower() == "no":
# #     print("Не согласен")
# # else:
# #     print("Не понял")
# #
# # num = 7
# # result = "Нулевым" if num == 0 else "Положительным чётным" if num % 2 == 0 and num > 0 else "Положительным нечётным" if num % 2 != 0 else "Отрицательным"
# # print(result)
# #
# # text = "Привет"
# # result = "Короткая" if len(text) < 5 else "Средняя" if 5 <= len(text) <= 9 else "Длинная"
# # print(result)
# #
# # items = ["Python", 42, True]
# # if type(items[0]) == str:
# #     print(f"Первый элемент - строка: {len(items[0])}")
# # elif type(items[0]) == int:
# #     result = "ЧЁТНОЕ" if items[0] % 2 == 0 else "НЕЧЁТНОЕ"
# #     print(f"Первый элемент - число: {result}")
# # else:
# #     print("Первый элемент другого типа")
# # fruit_prices = {
# #     "яблоко": 50,
# #     "банан": 30,
# #     "апельсин": 70
# # }
# #
# # student = {"name": "Алексей", "age": 20, "group": "A-101"}
# # student["age"]
# #
# # book = {"title": "1984", "author": "Оруэлл"}
# # book["year"] = 1949
# # book["title"] = "1984. Роман"
# #
# # pc = {"brand": "HP", "ram": 16, "os": "Windows", "price": 50000}
# # del pc["price"]
# #
# # country = {"name": "Япония", "capital": "Токио", "population": 126_500_000}
# # country.keys()
# # country.values()
# #
# # colors = {"red": "красный", "blue": "синий", "green": "зеленый"}
# # result =  "yellow" in colors.keys()
# # result2 =  "синий" in colors.values()
# #
# # weather = {"city": "Москва", "temp": -5, "wind": "северный"}
# # weather.get("humidity", "нет данных")
# #
# # user = {"login": "admin", "access_level": "full"}
# # user["password"] = "qwerty123"
# # result = "email" in user
# # print(result)
# # inventory = {"яблоки": 10, "груши": 5, "бананы": 7}
# # deleted_value = inventory.pop("груши")
# # profile = {"name": "Anna", "age": 30, "city": "Berlin"}
# # profile["age"] = 31
# # profile["job"] = "developer"
# # del profile["city"]
# # result = "country" in profile
# #
# # fruits = ["яблоко", "банан", "апельсин"]
# # for fruit in fruits:
# #     print(fruit)
# #
# # count = 0
# # while count < 5:
# #     print(count)
# #     count += 1
# #
# # numbers = [1, 3, 5, 7, 9, 2, 4, 6]
# # for number in numbers:
# #     if number % 2 == 0:
# #         break
# #     print(number)
# #
# # numbers = [1, 2, 3, 4, 5, 6]
# # for number in numbers:
# #     if number % 2 !=0:
# #         number +=10
# #         print(numb
#
# # with open("notes.txt", "w", encoding="utf-8") as file:
# #     file.write("Мои заметки")
# # with open("notes.txt", "r", encoding="utf-8") as file:
# #     result = file.read()
# #
# # lines = ["Первая строка", "Вторая строка", "Третья строка"]
# # with open("output.txt", "w", encoding="utf-8") as file:
# #     for line in lines:
# #         file.write(f"{line}\n")
# # with open("output.txt", "r", encoding="utf-8") as file:
# #     for line in file:
# #      print(line.strip())
# #
# # with open("notes.txt", "a", encoding="utf-8") as file:
# #     file.write("\nДополнение")
# # with open("notes.txt", "r", encoding="utf-8") as file:
# #     result = file.read()
# # print(result)
# #
# # age = 25
# # name = "Анна"
# # print(f"{age}, {name}")
# #
# # text = "Привет, мир!"
# # print(len(text))
# #
# # numbers = [1, 2, 3, 4]
# # numbers.append(5)
# #
# # x = 10
# # if x == 5:
# #     print("Равно")
# # else:
# #     print("Не равно")
# #
# # book = {"title": "Гарри Поттер", "year": 1997}
# # print(book["title"])
# #
# # for num in range(1,4):
# #     print(num)
# #
# # with open("test.txt", "w", encoding="utf-8") as file:
# #     file.write("Hello")
# #
# # def greet():
# #     return "Привет!"
# #
# # print(greet())
# #
# # def uppercase(func):
# #     def wrapper():
# #         result = func()
# #         return result.upper()
# #     return wrapper
# # @uppercase
# # def text():
# #     return "hello"
# # print(text())
# #
# # class Dog:
# #     def __init__(self, name):
# #         self.name = name
# #     def bark(self):
# #         return "Гав!"
# # d = Dog("шарик")
# #
# # class Cat(Animal):
# #     def meow(self):
# #         pass
# # c = Cat()
#
# # def repeat(n):
# #     def count(func):
# #      def wrapper():
# #          for _ in range(n):
# #            result = func()
# #          return result
# #      return wrapper
# # @repeat(2)
# # def text():
# #     return "hello"
# # print(text())
# # ##########
# # class Car:
# #     def meow(self):
# #         return "Мяу!"
# # c = Car()
# #
# # class Dog:
# #     species = "Canis familiaris"
# # d = Dog()
# #
# # class Book:
# #     def __init__(self, title):
# #         self.title = title
# # b = Book("qwerty")
# #
# # class Phone:
# #     ph = "nok"
# # p = Phone()
# # print(type(p.ph))
# #
# # class Person:
# #     def __init__(self, name):
# #         self.name = name
# #     def introduce(self):
# #         return f"Меня зовут {self.name}"
# # p = Person("qaz")
# # print(p.introduce())
#
# a = 5
# b = 3
# result = a + b
# print(result)
# x = "10"
# y = 5
# x = int(x)
# print(x + y)
# m = 7
# n = 12
# print(m < n)
#
# students_count = 25
# print(students_count)
#
# price = 100
# price = 90
# print(price)
#
# a = 15
# b = "Привет"
# c = 3.14
# print(type(a))
# print(type(b))
# print(type(c))
#
# num = "123"
# num = int(num)
# result = num * 2
# print(result)
#
# x = 10
# y = 4
# print(x%y)
#
# a = 5
# b = 5
# print(a==b)
# is_active = True
# print(type(is_active))
#
# s = "Automation"
# print(s[2])
#
# word = "Hello"
# print(word[1:4])
# str1 = "Hello, "
# str2 = "world!"
# result = str1 + str2
# print(result)
#
# name = "Alice"
# age = 25
# print(f"Name: {name}, Age: {age}")
#
# text = " python "
# text = text.strip()
# print(text)
#
# s = "Automation"
# print(len(s))
#
# text = "hello world"
# text = text.upper()
# print(text)
#
# s = "Programming"
# print(s[-3:])
#
# part1 = "Auto"
# part2 = "mation"
# result = part1 + part2
# print(result)

#
# fruits = ["apple", "banana", "cherry"]
# print(fruits)
# numbers = [10, 20, 30, 40]
# print(numbers[1])
#
# colors = ["red", "green"]
# colors.append("blue")
# print(colors)
#
# letters = ["a", "b", "c", "d", "e"]
# print(letters[1:4])
#
# items = ["book", "pen", "pencil"]
# items[1] = "notebook"
# print(items)
#
# nums = [1, 2, 3, 4, 5]
# nums.remove(3)
# print(nums)
#
# list1 = [1, 2, 3]
# list2 = [4, 5]
# result = list1 + list2
# print(result)
#
# animals = ["cat", "dog", "fish"]
# animals.insert(1, "bird")
# print(animals)
#
# data = [True, False, 1, "text"]
# data.clear()
# print(data)
#
# digits = [0, 1, 2, 3, 4, 5]
# print(digits[:3])

# x = 5
# if x > 0:
#     print("Число положительное")
#
# y = 10
# if y % 2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное")
#
# age = 18
# if age >= 18:
#     status = "Взрослый"
# else:
#     status = "Ребёнок"
#
# age = 18
# result = "Взрослый" if age >= 18 else "Ребёнок"
# print(result)
#
# z = 15
# if z % 3 == 0 and z > 10:
#     print("Подходит")
# else:
#     print("Не подходит")
#
# n = -5
# if n < 0:
#     print("Отрицательное")
# elif n == 0:
#     print("Ноль")
# else:
#     print("Положительное")
#
# price = 250
# if price < 100:
#     print("Бюджетный")
# elif 100 <= price < 500:
#     print("Средний класс")
# else:
#     print("Премиум")
#
# num = 12
# if num % 2 == 0 and num % 3 == 0:
#     print("Делится на 6")
# elif num % 2 == 0 and num % 3 != 0:
#     print("Чётное, но не делится на 3")
# else:
#     print("Нечётное")
#
#
# for num in range(1,6):
#     print(f"{num}: {num ** 2}")
#
#
# student = {
#     "имя": "Алексей",
#     "возраст": 20,
#     "курс": 2
# }
# print(student["возраст"])
#
# car = {
#     "марка": "Toyota",
#     "модель": "Camry"
# }
# car["год"] = 2020
# car["модель"] = "Corolla"
# print(car)
#
# book = {
#     "название": "1984",
#     "автор": "Джордж Оруэлл",
#     "год": 1949,
#     "жанр": "антиутопия"
# }
# del book["жанр"]
# print(book)
#
# country = {
#     "название": "Япония",
#     "столица": "Токио",
#     "население": 125_800_000
# }
# print(country.keys())
# print(country.values())
#
# movie = {
#     "название": "Крестный отец",
#     "год": 1972,
#     "режиссер": "Фрэнсис Форд Коппола"
# }
#
# result = "режиссер" in movie.keys()
# result2 = "Квентин Тарантино" in movie.values()
# print(result, result2)
#
# phone = {
#     "модель": "iPhone 13",
#     "память": "128GB"
# }
# phone["цвет"] = "синий"
# print("цвет" in phone.keys())
# print(phone.values())
#
# university = {
#     "название": "МГУ",
#     "адрес": {
#         "город": "Москва",
#         "улица": "Ленинские горы"
#     }
# }
#
# print(university["название"])
# print(university["адрес"]["город"])
#
# laptop = {
#     "модель": "MacBook Pro",
#     "характеристики": {
#         "год": 2023,
#         "оперативная память": "16GB"
#     }
# }
# laptop["характеристики"]["год"] = 2025
# laptop["характеристики"]["SSD"] = "1TB"
# print(laptop)

# class Robot:
#     pass
# r = Robot()
#
# class Car:
#     wheels = 4
# c = Car()
#
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
# b = Book("jfh", "j")
#
# class Calculator:
#     def add(self,a ,b):
#         return a + b
# c = Calculator()
# print(c.add(5,5))
#
# class Dog:
#     def __init__(self, name):
#         self.name = name
# d1 = Dog("Бобик")
# d2 = Dog("Шарик")
# print(d1.name)
# print(d2.name)
#
# class User:
#     def get_info(self):
#         return "Пользователь"
# u = User()
# p(u.get_info())

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return f"{self.name} издает звук."
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} гавкает!"
# d = Dog("bob")
# print(d.speak())

# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
#     def info(self):
#         return f"Марка: {self.brand}"
#
# class Car(Vehicle):
#     def __init__(self, model, brand):
#         super().__init__(brand)
#         self.model = model
#     def info(self):
#         return f"Марка: {self.brand}, Модель: {self.model}"
# c = Car("Camry", "Toyota")
# print(c.info())

#
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def introduce(self):
#         return f"Меня зовут {self.name}."
# class Student(Person):
#     def __init__(self, name, student_id):
#         super().__init__(name)
#         self.student_id = student_id
#     def study(self):
#         return f"{self.name} учится."
# s = Student("ilya", "uy667")
# print(s.introduce())

# class Car:
#     def __init__(self,brand, model):
#         self.brand = brand
#         self.model = model
#     def start_engine(self):
#         return f"Двигатель запущен"
# c = Car("TOYOTA", "srg")
# print(c.brand)
# print(c.model)
#
# class ElectricCar(Car):
#     def __init__(self,brand, model, battery_capacity):
#         super().__init__(brand, model)
#         self.battery_capacity = battery_capacity
# e = ElectricCar("tgj", "jlh", "jhbhj")


# class Book:
#     library_name = "Главная библиотека"
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#     def get_info(self):
#         return f"Название: {self.title}, Автор: {self.author}"
#     def change_author(self, new_author):
#         self.author = new_author
# book1 = Book("dfg", "sg")
# book2 = Book("1984", "Оруэлл")
# print(book2.title)
#
# class Student:
#     pass
# s = Student()
#
# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
# dog1 = Dog("dfv", "sf")
# print(dog1.name)
# print(dog1.breed)
#
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#     def info(self):
#         return f"Баланс {self.__balance}"
#     def new_balance(self, new):
#         self.__balance += new
#     def min_balance(self, min):
#         if min <= self.__balance:
#          self.__balance -= min
# bank = BankAccount(100)
# class Person:
#     def __init__(self, age):
#         self._age = age
#     def set_age(self, new_age):
#         if new_age >= 0 and new_age <= 120:
#             self._age = new_age
#         else:
#             print("Некорректный возраст")
# pers1 = Person(50)
# pers1.set_age(23)
# print(pers1._age)

class Animal:
    def speak(self):
        print("Some sound")
class Dog(Animal):
    def speak(self):
        print("Woof")
d1 = Dog()

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
