lesson1 = ["Практическое задание пункт 1:", "Парктическое задание пункт 2:",\
        "Практическое задание пунтк 3:", "Практическое задание пунтк 4:",\
        "Практическое задание пунтк 5:","Практическое задание пунтк 6:"]

print(lesson1[0])

hello = ["питон", "Привет", "!"]
print(hello[1] + " " + hello[0] + hello[2])

a = 15 + 6
print("Число А = " + str(a))

b = input("Введите число B ")
b = int(b)
print("Сумма чисел А и B равняется: " + str(a + +b))

print(lesson1[1])

time = int(input("Введите время в секундах "))

seconds = time % 60
minutes = (time//60) % 60
hours = (time//3600)

print(f"Вермя в формате часы:минуты:секунды будет: {hours:02}:{minutes:02}:{seconds:02}")#нове решение
# старое решение: print("Вермя в формате часы:минуты:ссекунды будет:"
# + str(hours) + ':' + str(minutes) + ':' + str(seconds))

print(lesson1[2])

num = input("Введите число N ")

#num = str(num) - убрал, работает!
a = num + num
b = num + num + num
total = int(num) + int(a) + int(b)
print(f"Сумма чисе N+NN+NNN= {total}") #применил f форматирование
#print("Сумма чисе N+NN+NNN= " + str(total))

print(lesson1[3])

num1 = int(input("Введите целое положительное число "))
max = num1 % 10
while num1 >= 1:
    num1 = num1 // 10
    if num1 % 10 > max:
        max = num1 % 10
    if num1 > 9:
        continue
    else:
        print(f"Максимальное цифра в числе {max}")
        break

print(lesson1[4])

revenue = int(input("Введите выручку фирмы "))
cost = int(input("Введите издержки фирмы "))
profit1 = round(revenue - cost, 2)#Точно! Ну бывает...

if revenue > cost:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit1}")
    workers = int(input("Введите количество сотрудников фирмы "))
    profit2 = round(profit1 / workers, 2)
    print(f"Прибыль в расчете на одного сторудника сотавила {profit2}")
elif revenue == cost:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

print(lesson1[5])

startRun = float(input("Введите результаты первой пробежки спортсмена в км "))#заменил названия переменных
resultRun = float(input("Введите необходимый результат спортсмена в км "))
days = 1
km = startRun
while km < resultRun:
        startRun = startRun + 0.1 * startRun
        days += 1
        km = km + startRun
print(f"В результате тренировок вы пребежите {resultRun}км на {days} день")
