"""

1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.

ZeroDivisionError
"""

def div_nums():
    try:
        div = firstNum / secondNum
        print(div)
        return div
    except ZeroDivisionError as e:
        print("На ноль делить нельзя")

firstNum = []
secondNum = []

while True:
    try:
        firstNum = int(input("Введите первое чило для вычеслений(для завершения введите 999): "))
        secondNum = int(input("Введите второе чило для вычеслений(для завершения введите 999): "))
        if firstNum == 999 or secondNum == 999:
            break
        div_nums()
    except ValueError as i:
        print("Вы ввели не число")







""""


3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.

4. Программа принимает действительное положительное число x и целое отрицательное
число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо
реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись
без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень
с помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.

5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
завершить программу.

6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().

"""