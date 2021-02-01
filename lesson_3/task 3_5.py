"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
завершить программу.
userNum = input("Введите числа через пробел(для завершения нажмите Q ").split()
"""

def sumOfUserNums():
    total = 0
    while True:
        userNum = input("Введите числа через пробел(для завершения нажмите Q ").split()
        for el in range(len(userNum)):
            if userNum[el] == "Q":
                print(f"Сумма введеных чисел равняется: {total}.")
                return
            else:
                total = total + int(userNum[el])
        print(f"Сумма введеных чисел равняется: {total}")

sumOfUserNums()