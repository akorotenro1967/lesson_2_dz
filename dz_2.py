
'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# for i in range(1,6):
#     input = ('0000000000000000000000000')
#     print(i, input)


'''
# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
# '''
# sum = 0
#
# for i in range(10):
#     quantity = int(input('Введите число до 10 :'))
#     if quantity == 5: sum += 1
#
#     print("Количество введенных цифр 5:", sum)

#
# '''
# Задача 3
# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
# '''
# # sum = 0
# #
# # for i in range(1,101):
# #     sum+=i
# # print(sum)
#
# '''
# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
# '''
# composition = 1
# for i in range(1, 10):
#     composition *= i
# print(composition)
#
# composition = 2
# for i in range(1, 10):
#     composition -= i
# print(composition)
#
# '''
# Задача 5
# Вывести цифры числа на каждой строчке.
# '''
#
# # integer_number = 2129
# #
# # #print(integer_number%10,integer_number//10)
# #
# # while integer_number>0:
# #     print(integer_number%10)
# #     integer_number = integer_number//10
#
#
#
# '''
# Задача 6
# Найти сумму цифр числа.
# '''
# sum = 0
# number = 254619
#
# while number > 0:
#     sum += number % 10
#     number = number//10
# print(sum)
#
#
#
# '''
# Задача 7
# Найти произведение цифр числа.
# '''
# total =1
# number = 2345
# while number > 0:
#     total*= number %10
#     number = number//10
# print(total)
#
#
#
#
# '''
# Задача 8
# Дать ответ на вопрос: есть ли среди цифр числа 5?
# # '''
# # integer_number = 213413
# # while integer_number>0:
# #     if integer_number%10 == 5:
# #         print('Yes')
# #         break
# #     integer_number = integer_number//10
# # else: print('No')
#
# '''
# Задача 9
# Найти максимальную цифру в числе
# '''
# a = 42598
# d = a%10
# a =a//10
# while a > 0:
#      if a%10 > d:
#          d = a%10
#      a = a//10
# print(d)
#
# '''
# Задача 10
# Найти количество цифр 5 в числе
# '''
# number = 245785695
# sum = 0
# while number > 0:
#      if number % 10 == 5:
#          sum += 1
#      number = number//10
# print(sum)
