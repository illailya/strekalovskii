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