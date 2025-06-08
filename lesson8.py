
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