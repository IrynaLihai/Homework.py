# Задание 1
# Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world... if you do so, you are insulting yourself.”
# Bill Gates
# def textedit():
#     indent = "    "
#     indent_max = "                                                "
#     italic_code = "\033[3m"
#     line1 = "“Don't compare yourself with anyone in this world..."
#     line2 = "if you do so, you are insulting yourself.”"
#     line3 = "Bill Gates"
#     print(indent_max)
#     print(italic_code + indent + line1)
#     print(italic_code + indent + line2)
#     print(italic_code + indent_max + line3)
#     print(indent)
#
# textedit()
#
# Задание 2
# Напишите функцию, которая принимает два числа в качестве параметра и отображает
# все четные числа между ними.
#
# def even_numbers(num1, num2):
#     if num1 >= num2:
#         num2, num1 = num1, num2
#     even_list = []
#     while num1 < num2:
#         if num1 % 2 == 0 and num1 != 0:
#             even_list.append(num1)
#         num1 += 1
#     return even_list
#
# print(even_numbers(8,-4))
#
# Задание 3
# Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа.
# Функция принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный; ■ если False, квадрат пустой.
#
# def square(length, symbol, bool):
#     try:
#         if length <= 0:
#             raise ValueError("Length should be a positive number!")
#         if not (bool == True or bool == False):
#             raise ValueError("Bool should be True or False")
#         i = 0
#         if bool == False:
#             while i < length:
#                 if i == 0 or i == length - 1:
#                     print((symbol + "  ") * length)
#                 else:
#                     print(symbol + "  " * length + symbol)
#                 i += 1
#         elif bool == True:
#             while i < length:
#                 print(symbol * length)
#                 i += 1
#     except ValueError as ex:
#         print(ex)
#
# square(5, "*", False)
#
# Задание 4
# Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров.
# def min_number(num1, num2, num3, num4, num5):
#     try:
#         numbers = [num1, num2, num3, num4, num5]
#         if not all(isinstance(num, (int, float)) for num in numbers):
#             raise TypeError("Arguments should be numbers!")
#
#         return min(numbers)
#     except TypeError as ex:
#         print(ex)
#
# print(min_number(2, -8, 9, 15, 88))
#
#
# Задание 5
# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне.
# Границы диапазона передаются в качестве параметров. Если границы диапа- зона перепутаны
# (например, 5 — верхняя граница, 25 — нижняя граница), их нужно поменять местами.
# import random
#
# number1 = random.randint(-100, 100)
# number2 = random.randint(-100, 100)
#
# def range_product(num1, num2):
#     try:
#         if num1 > num2:
#             num1, num2 = num2, num1
#         total_product = 1
#         current_num = num1
#
#         while current_num <= num2:
#             total_product *= current_num
#             current_num += 1
#
#         return total_product
#     except Exception as ex:
#         print(f"An error occurred: {ex}")
#         return None
#
# result = range_product(number1, number2)
# if result is not None:
#     print(result)
#
# Задание 6
# Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра.
# Из функции нужно вернуть полученное количество цифр. Например, если передали 3456,
# количество цифр будет 4.
# def number_of_numbers(number):
#     try:
#         number_str = str(number)
#         if not number_str.isdigit():
#             raise ValueError("You should enter number!")
#         return len(number_str)
#     except ValueError as ex:
#         print(ex)
#
#
# print(number_of_numbers(9987654))
# Задание 7
# Напишите функцию, которая проверяет является ли число палиндромом.
# Число передаётся в качестве параметра.
# Если число палиндром нужно вернуть из функции true, иначе false.
# «Палиндром» — это число, у которого первая часть цифр равна второй перевернутой части цифр.
# Например, 123321 — палиндром (первая часть 123, вторая 321, которая после переворота становится 123),
# 546645 — палиндром, а 421987 — не палиндром.
#
# def palindrome (number):
#     try:
#         number_str = str(number)
#         if not number_str.isdigit():
#             raise ValueError("You should enter number!")
#         if number_str == number_str [::-1]:
#             return True
#         else:
#             return False
#     except ValueError as ex:
#         print(ex)
#
#
# print(palindrome(12344321))