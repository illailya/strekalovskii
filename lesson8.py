from lesson6 import total


# Функции
def greet():
    print("Привет, мир!")


greet()

#

def multiply(a, b):
    print(f"Результат: {a * b}")
multiply(3,4)

#

def is_even(num):
    if num %2==0:
        print(True)
    else:
        print(False)
is_even(4)

#

def calculate(a,b,operator = "+"):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Неизвестная операция"
print(calculate(6,2,"-"))
print(calculate(5,5))

#

def num(a,operator= "**"):
    print(num(5))

#

def greet_user(name):
    print(f"Привет, {name}! Рад тебя видеть!")

greet_user("Илья")

#

def multiply_numbers(a, b):
    return a * b
result = multiply_numbers(4,7)
print(result)

#

def greet(name):
    print(f"Привет, {name}! Добро пожаловать!")

greet("Анна")

#

def calculate(a,b):
    return a + b, a * b
result = calculate(3, 4)
print(result)

#

def smile(func):


 def wrapper():
      print(":)")
      func()
 return wrapper

@smile
def text():
    print("Вывод")
text()

#

def uppercase(ref):
    def wrapper():
        result = ref()
        return result.upper()
    return wrapper
@uppercase
def text():
    return "слово"
print(text())

#

def repeat(func):
    def wrapper():
        print("начало")
        func()
        func()
    return wrapper
@repeat
def hello():
    print("Привет")
hello()

#

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_numbers(1,2,3))

#

def print_user_data(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_user_data(name="Анна", age=25, city="Москва")

#

def greet():
    print("Привет, мир!")
greet()

#

def multiply(a, b):
    return a * b
print(multiply(5, 5))

#

def power(x, n=2):
    return x **n
print(power(5,4))

#

def log_me(func):
    def wrapper():
        print("Функция вызвана")
        return func()
    return wrapper


@log_me
def say_hello():
    print("Привет!")
say_hello()

#

# def repeat(n):
#     def decorator(func):
#       def wrapper():
#         return func()
#     return wrapper
# @repeat(3)
# def say_hello():
#     print("Привет!")
# say_hello()

#

def hello(func):
    def wrapper(*args, **kwargs):
        print("Привет!")
        func(*args, **kwargs)
    return wrapper
@hello
def crfpfnm(name):
    print(f"Меня зовут {name}")
crfpfnm("Анна")

#

def surround_with_text(func):
    def wrapper():
        print("Начало работы функции")
        func()
        print("Функция завершила работу")
    return wrapper
@surround_with_text
def hello():
    print("Привет мир")
hello()

#

def subtract(a, b):
    return a - b
result = subtract(5, 5)
print(result)

#

def double_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper
@double_result
def add(a, b):
    return a + b
print(add(2, 2))

#

def is_positive(num):
    return num > 0
print(is_positive(5))

#

def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"
print(greet("Анна"))
print(greet("Петр", "Здравствуй"))

#

# def calculate_area():
#     length = float(input("Введите ширину: "))
#     width = float(input("Введите высоту: "))
#     area = length * width
#     print(f"Площадь: {area}")
#
# calculate_area()

#

def bold(func):
    def wrapper():
       result = func()
       return f"<b>{result}</b>"
    return wrapper
@bold
def get():
    return "Привет!"
print(get())

#

def power(base, exponent = 2):
    return base ** exponent
print(power(3,3))

#

def create_user(email, name="Пользователь", age=None):
    user = {
        "email": email,
        "name": name
    }
    if age is not None:
        user["age"] = age
    return user
print(create_user("test@mail.ru"))
print(create_user("test@mail.ru", "илья", 33))