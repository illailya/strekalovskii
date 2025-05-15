#Задание 1
text = "Hello, Python!"

print(f"Первые 5 символов: text[:5]")
print(f"Символы с индексами от 7 до 12: text[7:13]")
print(f"Последние 3 символа: text[-3:]")
print(f"Каждый второй символ строки: text[::2]")

#Задание 2
message = "  hello, World!  "

result1 = message.strip()
print(f"Убирает пробелы в начале и конце строки: {result1}")
result2 = result1.upper()
print(f"Приводит строку к верхнему регистру: {result2}")
result3 = result2.replace('WORLD' , 'Python')
print(f"Заменяет 'WORLD' на 'Python': {result3} ")
result4 = result3.startswith('HELLO')
print(f"Проверяет, начинается ли строка с 'HELLO' (после преобразований): {result4}")
result5 = result3.split(',')
print(f"Разделяет строку по запятой (получится список из 2 элементов): {result5} ")