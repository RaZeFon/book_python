"""
water_rate = 35.35
water_start = float(input("Показание на начала месяца: "))
water_end = float(input("Показание на конец месяца: "))
result = (water_start - water_end) * water_rate
print("Сумма к оплате", result)
"""
"""
cabbage = 12
carrot = 1.2
salt = 1
dill = 3
liter_cabbage = int(input("Введите количество ведер капусты: "))
print("Понадобится капусты", cabbage * liter_cabbage, "кг")
print("Понадобится моркови", carrot * liter_cabbage, "кг")
print("Понадобится стаканов соли", salt * liter_cabbage)
print("Понадобится ложек укропа", dill * liter_cabbage)
"""
"""
kopeck1 = int(input("Сколько копеек: "))
kopeck5 = int(input("Сколько пятикопеечных: "))
kopeck10 = int(input("Сколько десятикопеечных: "))
kopeck50 = int(input("Сколько пятидесяти копеек: "))
ruble1 = int(input("Сколько рублей: "))
ruble2 = int(input("Сколько двухрублёвых: "))
ruble5 = int(input("Сколько пятирублёвых: "))
ruble10 = int(input("Сколько десятирублёвых: "))
sum_kopecks = kopeck1 + (kopeck5 * 5) + (kopeck10 * 10) + (kopeck50 * 50)
sum_rubles = ruble1 + (ruble2 * 2) + (ruble5 * 5) + (ruble10 * 10)
print(f"Всего сумма рублей {sum_rubles} и сумма копеек {sum_kopecks}")
print(f"Сумма {sum_rubles + sum_kopecks // 100} руб {sum_kopecks % 100} копеек")
"""
"""
print("|" * 50)
print("\tРАСЧЕТ ДЛИТЕЛЬНОСТИ ДОРОГИ В ШКОЛУ")
print("|" * 50)
c1 = int(input("Время выхода из дома, часы: "))
m1 = int(input("Время выхода из дома, минуты: "))
c2 = int(input("Время входа в школу, часы: "))
m2 = int(input("Время входа в школу, минуты: "))
t = (c2 * 60 + m2) - (c1 * 60 + m1)
tc = t // 60
tm = t % 60
print(f"Дорога в школу заняла {tc} часов и {tm} минут")
"""
"""
string = "|"
print(f"\n{string * 50}\n\t\tПРОДАЖА МОРОЖЕНОГО\n{string * 50}\n")
price = 12.50
product = "Мороженое"
bot_name = "Бот-Артем"
print(f"Здравствуйте я {bot_name} продаю {product}, а как вас зовут?")
name = input("Введите ваше имя: ")
print(f"Очень приятно {name} рад знакомству!\n")
print(f"Не хотите {product} одна штука стоит {price}")
count = int(input("Введите количество которое хотите приобрести: "))
print(f"Ваш заказ {count} шт на общую сумму {price * count}\n\nСпасибо за покупку хорошего дня.\n")
"""
"""
lattice1 = "#"
print(f"{lattice1 * 33}\n{lattice1 * 10} ЧЕПУХА {lattice1 * 10}\n{lattice1 * 33}")
print(f"Давайте вмести сочиним рассказ\nВы ответите на вопросы, а остальное сделает Python\n{lattice1 * 33}")
question1 = input("Сколько времени можешь провести без смартфона? ")
question2 = input("Какое животное вам наиболее симпатично? ")
question3 = input("Назовите первое попавшиеся заклинание? ")
question4 = input("Какой предмет из вашего дома самый тяжелый? ")
question5 = input("Какими словами вы обычно выражаете крайнее удивление? ")
question6 = input("Чем отбиваетесь от комаров? ")
question7 = input("Каким продуктом можно вас порадовать? ")
print(lattice1 * 33)
print(f"Даже {question2} знает: если {question1} повторять заклинанье {question3}\nразмахивая при этом {question6} - оно сработает! И {question4}, радостно похрюкивая,")
print(f"запрыгает от радости, {question5} получилось! и побежит в магазин за {question7}")
print(lattice1 * 33)
"""
"""
r = input("За окном светло? (да\нет\не знаю): ")
if r == "да":
    print("сон про игру с мячиком")
elif r == "нет":
    print("сон про астрофизику")
else:
    print("сон про Софочку")
print("заснуть")
"""
"""
a = input("Введите значение А: ")
b = input("Введите значение B: ")
if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a = b")
"""
"""
anna = int(input("яблок у Анечки: "))
boriya = int(input("яблок у Боречки: "))
if anna > boriya:
    result = (anna - boriya) / 2
    print(f"Анечка должна дать яблок {result}")
elif boriya > anna:
    result = (boriya - anna) / 2
    print(f"Боречка должна дать яблок {result}")
else:
    print ("Одинаковое количество яблок")
"""
"""
viviaki = int(input("Ведите количество вивиаков: "))
if viviaki % 2 == 1:
    print('Эдакер')
elif viviaki == 2:
    print("Двутыкалка")
elif viviaki == 4:
    print("Пузяйка")
elif viviaki == 10 or viviaki == 12 or viviaki == 14:
    print("Шушунд")
elif viviaki == 20 or viviaki == 22 or viviaki == 24 or viviaki == 26 or viviaki == 28:
    print("Хых")
elif viviaki >= 40 and viviaki % 2 == 0:
    print("Лохмыдра")
elif viviaki <= 0:
    print("Это не местное существо")
else:
    print("Неизвестный вид")
"""

"""
n = int(input("n = "))
if n % 2 > 0:
    print("б")
else:
    print("т")
n = n // 2
if n % 2 > 0:
    print("о")
else:
    print("у")
n = n // 2
if n % 2 > 0:
    print("р")
else:
    print("к")
"""
"""
count = 0
print("Викторина вопросов")
question1 = input("Сколько будет 2+2=")
if question1 == "4":
    print(f"Верно {question1}")
    count += 1
else:
    print(f"{question1} неверно правильный ответ 4")

question2 = input("Сколько будет 2**3=")
if question2 == "8":
    print(f"Верно {question2}")
    count += 1
else:
    print(f"{question2} неверно правильный ответ 8")

question3 = input("Сколько выходных на недели: ")
if question3 == "2":
    print(f"Верно {question3}")
    count += 1
else:
    print(f"{question3} неверно правильный ответ 2")

question4 = input("До скольки ты работаешь: ")
if question4 == "19:00":
    print(f"Верно до {question4}")
    count += 1
else:
    print(f"{question4} неверно правильный ответ до 19:00")

question5 = input("Сколько аниме ты уже посмотрел: ")
if question5 == "2019":
    print(f"Верно {question5}")
    count += 1
else:
    print(f"{question5} неверно правильный ответ 2019")

print(f"Итого правильных ответов {count} из пяти")
"""
"""
print("Введите оценку в 100-бальной системе: ")
b = int(input())
if 80 <= b <= 100:
    print("Это 5")
elif 20 <= b < 40:
    print("Это 2")
elif b < 20:
    print("Это 1")
elif 40 <= b < 60:
    print("Это 3")
elif 60 <= b < 80:
    print('Это 4')
else:
    print("Вы что-то напутали!")
"""
"""
a = True
b = True
c = True
print(not a or b or c)
print(not (a or b or c))
"""
"""
a = True
b = True
c = False
print(a or b and c)
print((a or b) and c)
print(not c and a)
print(not(c and a))
"""
"""
print("Протяженность лесной дороги 20 км")
km = int(input("Вредите номер километра: "))
if 1 <= km <= 20:
    if 1 <= km <= 3 or 8 <= km <= 12 or km == 17:
        print("Сосновый бор")
    elif km == 13:
        print("Дюны")
    elif km == 5 or km == 6 or km == 14:
        print("Болото")
    elif km == 20:
        print("Луг")
    else:
        print("Смешанный лес")
else:
    print("За пределами лесной дороги")
"""
"""
result = 0
dir = int(input("Доход сотрудников: "))
if 1000000 >= dir >= 20000:
    if dir // 10000 > 10:
        result = dir // 10000
    else:
        result += 10
else:
    result = 0
print(f"Заплатит {result} дыр")
"""
"""
result = 0
dire = int(input("Доход сотрудников: "))
if dire >= 20000 or dire <= 1000000:
    if dire // 10000 > 10:
        result = dire // 10000
    else:
        result += 10
else:
    result = 0
print(f"Заплатит {result} дыр")
"""
"""
dire = int(input("Доход сотрудников: "))
if 20000 <= dire <= 1000000:
    result = max(10, dire // 10000) #функция выбирает максимальное значение из двух
else:
    result = 0
print("Налог составит", result)
"""
"""
result1 = "Кот счастлив"
result2 = "Кот ушёл спать"
print("Кот мяукает")
cat = input("Кот хочет есть (да\нет): ")
if cat == "нет":
    cat = input("Кот хочет внимания (да\нет): ")
    if cat == "да":
        cat = input("Погладить кота (да\нет): ")
        if cat == "нет":
            cat = input("Поиграть с котом (да\нет): ")
            if cat == "да":
                print("Коту весело")
                print(result1)
            else:
                print("Кот посмотрел")
                print(result2)
        else:
            print("Коту это нравится")
            print(result1)
    else:
        print("Кот расстроен")
        print(result2)
else:
    print("Покормить кота")
    print(result1)
"""
"""
number = int(input("Введите четырех значное число: "))
if number < 1000 or number > 9999:
    print("Это не четырехзначное число! ")
else:
    thousand = number // 1000
    hundreds = number // 100 % 10
    tens = number % 100 // 10
    unit = number % 10

    if thousand < hundreds < tens < unit:
        print("Цифры в порядке возрастания")
    elif thousand > hundreds > tens > unit:
        print("В порядке убывания")
    else:
        print("Цифры ведены не по порядку")
"""
"""
print("Проверка количества дней в месяце")
month = input("Введите название месяца: ")
upper_month = month.upper()
match upper_month:
    case "ЯНВАРЬ" | "МАРТ" | "МАЙ" | "ИЮЛЬ" | "АВГУСТ" | "ОКТЯБРЬ" | "ДЕКАБРЬ":
        print ("31 день")
    case "АПРЕЛЬ" | "ИЮНЬ" | "СЕНТЯБРЬ" | "НОЯБРЬ":
        print("30 дней")
    case "ФЕВРАЛЬ":
        print("28 дней")
    case _:
        print("Такой месяц не существует")
"""
"""
n = int(input("Сколько раз прокуковать?: "))
for k in range(n):
    print("Ку-ку!")
"""
"""
for k in range(5):
    print(k)
"""
"""
for k in range(2, 5):
    print(k)
"""
"""
for k in range(1, 6):
    print(k)
"""
"""
for k in range(5, 2, -1):
    print(k)
"""
"""
for k in range(10, -1, -1):
    print(k)
"""
"""
for k in range(10, 100, 10):
    print(k)
"""
"""
for k in range(1000, 2000, 100):
    print(k + 13)
"""
"""
summa = 0
print("Программа по суммированию заданного количества чисел!")
repeat = int(input("Ввести количество раз которое будет проводится сложение: "))
for i in range(repeat):
    summa += int(input("Введите число: "))
print(f"Сумма всех чисел равна {summa}")
"""
"""
product = 1
print("Программа показывает произведение заданного количества чисел!")
repeat = int(input("Ввести количество раз которое будет проводится умножение: "))
for i in range(repeat):
    product *= int(input("Введите число: "))
print(f"Сумма всех чисел равна {product}")
"""
"""
counter = 0
print("Программа подсчитывает количество четных чисел")
repeat = int(input("Какое количество раз будет проверять: "))
for i in range(repeat):
    if int(input("Введите число ")) % 2 == 1:
        counter += 1
print(f"Количество нечетных чисел {counter} введённых пользователем")
"""
"""
counter = 0
print("Программа подсчитывает количество нечетных чисел")
repeat = int(input("Какое количество раз будет проверять: "))
for i in range(repeat):
    counter += int(input("Введите число ")) % 2
print(f"Количество нечетных чисел {counter} введённых пользователем")
"""
"""
counter = 0
print("Программа подсчитывает количество четных чисел")
repeat = int(input("Какое количество раз будет проверять: "))
for i in range(repeat):
    if int(input("Введите число ")) % 2 == 0:
        counter += 1
print(f"Количество четных чисел {counter} введённых пользователем")
"""
"""
maxims = 0
print("Программа для поиска наибольшего значения из введённых пользователем значений")
repeat = int(input("Какое количество объектов для поиска: "))
for i in range(repeat):
    meaning = int(input("Введите значение: "))
    if maxims < meaning:
        maxims = meaning
print(f"Максимальное значение {maxims}")
"""
"""
print("Программа для поиска наибольшего и наименьшего значения введенных пользователем")
repeat = int(input("Какое количество объектов для поиска: "))
number = int(input("Значение для сравнения: "))
minNum = number
maxNum = number
for i in range(repeat -1):
    number = int(input("Значение для сравнения: "))
    if number > maxNum:
        maxNum = number
    if number < minNum:
        minNum = number
print(f"max = {maxNum}; min = {minNum}")
"""
"""
print("Программа для поиска наибольшего и наименьшего значения введенных пользователем,\nи вывести их разность")
repeat = int(input("Какое количество объектов для поиска: "))
number = int(input("Значение для сравнения: "))
minNum = number
maxNum = number
for i in range(repeat -1):
    number = int(input("Значение для сравнения: "))
    if number > maxNum:
        maxNum = number
    if number < minNum:
        minNum = number
print(f"max = {maxNum}; min = {minNum}; max - min = {maxNum - minNum}")
"""
"""
n = int(input("До какого числа будем складывать? "))
s = 0
for k in range(n + 1):
    s = s + k
print("Сумма: ", s)
"""
"""
n = int(input("До какого числа будем складывать? "))
print(n * (n + 1) // 2)
"""
"""
counter = 0
print("Таблица умножения с поставлением оценок ")
number = int(input("Введите число: "))
for i in range(1, 11):
    if number * i != int(input(f"{number} * {i} = ")):
        counter += 1

match counter:
    case 0:
        print("Нет ошибок ставим 5")
    case 1 | 2:
        print(f"Ваша оценка 4, у вас {counter} ошибка")
    case 3 | 4:
        print(f"Ваша оценка 3, у вас {counter} ошибки")
    case _:
        print(f"Ваша оценка 2, у вас {counter} ошибки")
"""
"""
a = int(input("Введите натуральное число: "))
b = int(input("Введите другое натуральное число: "))
print("А теперь будем практиковаться в умножении ")
err = 0 #счетчик ошибок
for i in range(a, a + 5):
    for j in range(b, b + 5):
        r = int(input(str(i) + " * " + str(j) + " = "))
        if r != i * j: #проверка на ошибку
            err = err + 1
print("Количество ошибок", err)
"""
"""
error = 0
print("Решение уравнений")
number_A = int(input("Введите число А: "))
number_B = int(input("Введите число В: "))
for i in range(number_A, number_A + 5):
    for j in range(number_B, number_B + 5):
        if i * j != int(input(f"{i} * {j} = ")):
            error += 1
print(f"Количество ошибок = {error}")
"""
"""
sum_squares_negative = 0
col_positive_numbers = 0
print("Сумма квадратов отрицательных чисел\nКоличество положительных чисел заканчивающихся цифрой 1")
quantity = int(input("Количество чисел для проверки: "))
for i in range(quantity):
    number = int(input("Введите число для проверки: "))
    if number < 0:
        sum_squares_negative = sum_squares_negative + number * number
    elif number > 0 and number % 10 == 1:
        col_positive_numbers += 1
print("Сумма квадратов отрицательных чисел:", sum_squares_negative)
print("Количество положительных чисел заканчивающихся на единицу:", col_positive_numbers)
"""          
"""
max_1 = 0
max_2 = 0
quantity = int(input("Введите количество сравниваемых чисел: "))
for i in range(quantity):
    number = int(input("Введите число: "))
    if number > max_1 and number > max_2:
        max_2 = max_1
        max_1 = number
    if number < max_1 and number > max_2:
        max_2 = number
print(f"Первое max = {max_1}, второе max = {max_2}")
"""
"""
max_1 = 0
max_2 = 0
quantity = int(input("Введите количество сравниваемых чисел: "))
for i in range(quantity):
    max_1 = int(input("Введите первое число: "))
    max_2 = int(input("Введите второе число: "))
    if max_2 > max_1:
        max_1, max_2 = max_2, max_1
    print(f"max 1 = {max_1}; max 2 = {max_2}")
"""
"""
text = input("Что нужно вывести: ")
number = int(input("Сколько раз: "))
for i in range(number):
    print(f"{i + 1}: {text}")
"""
"""
print("Таблица умножения")
number = int(input("Введите число: "))
for i in range(2, 10):
    print(f"{number} * {i} = {number * i}")
"""
"""
print("Таблица умножения 2")
number = int(input("Введите число: "))
for i in range(2, 10):
    sum_num = int(input(f"{number} * {i} = "))
    if sum_num == number * i:
        print("Верно")
    else:
        print("Неверно")
"""
"""
count = 1
number = int(input("Введите число: "))
min_1 = number
for i in range(5):
    number = int(input("Введите число: "))
    if number == min_1:
        count += 1
    if number < min_1:
        min_1 = number
        count = 1
print("Найденое минимальное значение", min_1)
print(f"Количество min чисел подряд {count}")
"""
"""
count = 0
number = int(input("Введите число: "))
max_1 = number
for i in range(5):
    number = int(input("Введите число: "))
    if number > max_1:
        max_1 = number
        count += 1
print("Счетчик", count)
"""
"""
hvatit = ""
c = 0
while hvatit != "да":
    c = c + 1
    print("Закончила круг " + str(c) + ". Хватит?")
    hvatit = input()
print("Ну наконец-то!")
"""
"""
ocenki = 10
summa = 20
for d in range(7):
    b = int(input("Оценка в день " + str(d + 1) + ": "))
    ocenki += 1
    summa += b
    stball = summa / ocenki
    if stball > 2.5:
        break
print("Оценка: ", round(stball))
"""
"""
otvet = ""
otj = "Ых! "
while not otvet == "lazy":
    otvet = input("What is English \"ленивый\"? ")
    print("Отжиматься! ")
    for k in range(5):
        print(otj)
        otj = "Ы" + otj
print("Зачет. ")
"""
"""
answer = ""
while answer.upper() != "ВИЛКА":
    answer = input("2 удара = 8 дырок. Что это? ")
print("Супер!")
"""
"""
print("цикл ждет ввода строки \"STOP\", и после ввода строки 3 раза\nостанавливает свою работу.")
c = 0
while c < 3:
    w = input()
    if w.upper() == "STOP":
        c += 1
print("OK")
"""
"""
print("Цикл будет работать до тех пор, 'A' не будет равно 'B', при каждом срабатывании цикла\nпоследнее значение 'B' будет присваеватся в 'A'")
a = input()
b = input()
while a != b:
    a = b
    b = input()
"""
"""
print("Будем отнимать a от b и b от a до тех пор пока a не будет равна b")
a = int(input())
b = int(input())
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)
"""
"""
print("Цикл работает пока N больше 0, после окончания выводится сумма остатков от деления на 10")
n = int(input())
s = 0
while n > 0:
    s = s + n % 10
    n = n // 10
print(s)
"""
"""
print("Переводит число в двоичную систему исчисления и выводит его ввиде строки")
n = int(input())
s = ""
while n > 0:
    s = str(n % 2) + s
    n = n // 2
print(s)
"""
"""
print("Бесконечный цикол")
count = 0
while True:
    print(f"{count + 1}: Бесконечность")
    count += 1
"""
"""
p = 1
while True:
    n = int(input())
    if n == 0:
        break
    p = p * n
print(p)
"""
"""
count = 0
macik = 0
paytichap = 0
churchik = 0
chapuga = 0
print("Обитатели планеты Яяю")
while True:
    chapok = int(input("Количество хапок у обитателя: "))
    if chapok == 0:
        print("Вы вернулись на базу, и перед вами тётя Паня")
        break
    else:
        match chapok:
            case 1|2|3|4:
                macik += 1
                count += 1
            case 5:
                paytichap += 1
                count += 1
            case 6|7:
                churchik += 1
                count += 1
            case 8|9|10|11:
                chapuga += 1
                count += 1
print("Общее количество найденых обитателей:", count)
print(f"Масик = {macik}\nПятихап = {paytichap}\nШуршик = {churchik}\nХапуга = {chapuga}")
"""
"""
count = 1
while True:
    count += 1
    raz = count ** 7 - count ** 5
    if raz > 1_000_000:
        print(count)
        break
"""
"""
count = 0
start = 100
finish = 999
while start < finish + 1:
    n1 = start // 100
    n2 = (start // 10)  % 10
    n3 = start % 10
    if n3 < n1 and n1 < n2:
        count += 1
    start += 1
print(count)
"""
"""
a = int(input("Начало: "))
b = int(input("Конец: "))
while b - a >= 1:
    m = (a + b) // 2
    r = input(">" + str(m) + "? ")
    if r == "ДА":
        a = m + 1
    else:
        b = m
print(a)
"""
"""
digit = ["Ноль", "Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь", "Восемь", "Девять"]
n = int(input("Введите цифру: "))
print(digit[n])
"""
"""
season = ["Зима", "Весна", "Лето", "Осень"]
print(season[0], season[2])
print(season[len(season) - 1])
"""
"""
n = int(input("Количество участников бригады: "))
b = []
print("Введите их имена через Enter: ")
for k in range(n):
    b.append(input())
b.sort()
print("Состав бригады: ")
for u in b:
    print(u)
"""
"""
b = ["винни-пух", "иа-иа", "кролик", "пяточек", "сова"]
r = ["первый", "второй"]
for i in range(len(b)):
    print(b[i] + ":", r[i % 2])
"""
"""
b = ["винни-пух", "иа-иа", "кролик", "пятачок", "сова"]
v = []
s = 0 
print("Кто сколько накопал нынче?")
for k in range(len(b)):
    r = int(input(b[k] + ": "))
    s = s + r
    v.append(r)
konf = int(input("Сколько конфет заработала бригада? "))
konfm = konf // s
for k in range(len(b)):
    v[k] = v[k] * konfm
    print(b[k], "-", v[k])
    print("бригадир:", konf - sum(vs))
"""
"""
list = []
while True:
    n = int(input())
    if n == 0:
        break
    list.append(n)
print(list)
"""
"""
w = ["to", "be", "or", "not", "to", "be"]
print(w.index("be"))
print(w.index("be", 3))
print(w.count("to"))
print(w.count("love"))
"""
"""
a = []
for k in range(5):
    a.append(int(input()))
a.sort()
print("min:", a[0], " max:", a[4] )
"""
"""
z = ["и", "с", "н", "л", "т", "и", "е", "е", "р", "л", "н", "т", "е", "а", "т", "о"]
a = int(input("А = "))
b = int(input("B = "))
for k in range(len(z)):
    if k % a == b:
        print(z[k], end = "")
"""
"""
z = [1, 3, 2, 5, 0, 4]
for k in range(6):
    print(z[z[z[k]]]) #тут творится магия недоступная мне
    # 5 4 2 0 3 1
"""
"""
#Сколько дней в месяце - 2
m = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль",
     "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mes = input("Введите название месяца (с маленькой буквы): ")
if mes in m:
    print(d[m.index(mes)], "д.")
    if mes == "февраль":
        g = int(input("Ой, стоп! Это же февраль! А какой год? "))
        # правило невисокосности - погуглите.
        if g % 4 > 0 or g % 100 == 0 and g % 1000 > 0:
            print("Да, 28.")
        else:
            print("Значит, 29.")
else:
    print("Неправильный у вас месяц.")
"""

"""
month = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while True:
    month_name = (input("Введите месяц (с маленькой буквы): "))

    if month_name == "февраль":
        index = month.index(month_name)
        year = int(input("Какой сейчас год: "))
        if year % 4 > 0 or year % 100 == 0 and year % 1000 > 0:
            print(f"Количество дней = {days[index]}")
        else:
            print(f"Количество дней = {days[index] + 1}")

    elif month_name in month:
        print(f"Количество дней = {days[month.index(month_name)]}")
    else:
        print("Неверный месяц")
"""
"""
import time
xaker_array = ["Aга, процесс пошел...", "Мир замер в ожидании...", "Что, бабушка? Пирожки? Здорово!",
               "Да бабушка, да чай буду", "Погладить кота", "Зевает", "Наливает чай", "Ест пирожёк",
                "Ну ещё чуть-чуть...", "Кирдык пентагонским серверам!" ]
string_array = ["A", "!"]
string = "AAA!"
count_dan = 0
input("Нажмите ENTER, чтобы начать ")
print("Подключение к сетям Пентагона... ")
time.sleep(1)
print("Подключение успешно. Подбор данных для входа... ")
time.sleep(1)
print("Вход выполнен. Запушена закачка данных... ")
print("")
for k in range(10):
    time.sleep(1)
    count_dan = count_dan + 10
    print(f"Комп: выполнено {count_dan}%")
    print("Пентагон:", string)
    string = string_array[0] + string + string_array[1]
    print(f"Хакер: {xaker_array[k]}")
    print("")
time.sleep(1)
print("Враг будет разбит, победа будет за нами!")
"""
"""
import random
while True:
    number_1 = random.randint(10, 99)
    number_2 = random.randint(10, 99)
    result = int(input(f"{number_1} + {number_2} = "))
    if result == number_1 + number_2:
        print("Верно!")
    else:
        print("Неверно!")
"""
"""
import random
count = 0
for i in range(10):
    number_1 = random.randint(10, 99)
    number_2 = random.randint(10, 99)
    result = int(input(f"{number_1} + {number_2} = "))
    if result == number_1 + number_2:
        print("Верно!")
        count += 1
    else:
        print("Неверно!")

match count:
    case 10:
        print("Оценка 5")
    case 9 | 8:
        print("Оценка 4")
    case 7 | 6 | 5:
        print("Оценка 3")
    case _:
        print("Оценка 2")
"""
"""
import random
count = 0
for i in range(10):
    action = random.randint(0, 1)
    number_1 = random.randint(10, 99)
    number_2 = random.randint(10, 99)
    
    if action == 1:
        result = int(input(f"{number_1} + {number_2} = "))
        if result == number_1 + number_2:
            print("Верно!")
            count += 1
        else:
            print("Неверно!")
    else:
        result = int(input(f"{number_1} - {number_2} = "))
        if result == number_1 - number_2:
            print("Верно!")
            count += 1
        else:
            print("Неверно!")

match count:
    case 10:
        print("Оценка 5")
    case 9 | 8:
        print("Оценка 4")
    case 7 | 6 | 5:
        print("Оценка 3")
    case _:
        print("Оценка 2")
"""
"""
import time
print(time.time())
"""
"""
import time
divination = ["Любит", "Не любит", "Плюнет", "Поцелует", "К сердцу прижмет", "К чёрту пошлёт"]
print(divination[int(time.time()) % 6])
"""
"""
import time
divination = ["Любит", "Не любит", "Плюнет", "Поцелует", "К сердцу прижмет", "К чёрту пошлёт"]
for i in range(5):
    time.sleep(2)
    print(divination[int(time.time()) % 6])
"""
"""
import random
u = ["Букин", "Бякин", "Тукин", "Хрюкин", "Жукин"]
print("К доске пойдет", random.choice(u))
"""
"""
import random
u = ["Букин", "Бякин", "Тукин", "Хрюкин", "Жукин"]
random.shuffle(u)
for uch in u:
    print("К доске пойдёт", uch)
"""
"""
#Тест на устный счёт
import random
random.seed()
import time
print("Проверим навыки устного счёта.")
ok = 0
t = time.time() #заодно посчитаем и время решения
for i in range(1, 11):
    z = random.randint(0, 1)
    a = random.randint(10, 99)
    b = random.randint(10, 99)    
    if z == 0: #сложение
        n = int(input(str(a) + " + " + str(b) + " = "))
        if n == a + b:
            print("Верно.")
            ok += 1
        else:
            print("Неверно.")
    else: #вычитание
        a, b = max(a, b), min(a, b) #упорядочили числа
        n = int(input(str(a) + " - " + str(b) + " = "))
        if n == a - b:
            print("Верно.")
            ok += 1
        else:
            print("Неверно.")
print("РЕЗУЛЬТАТ")
print("Из 10 примеров верно решены", ok)
print("Время решения -", time.time() - t, "сек.")
"""
"""
import random
answer = ["ДА", "НЕТ", "Сомнительно", "Верно", "Возможно", "Затрудняюсь"]
print("Задайте вопрос, подразумевающий ответ ДА или НЕТ")
while True:
    question = input("Ваш вопрос: ")
    if question == "":
        break
    else:
        print(f"Мой ответ: {random.choice(answer)}")
"""
"""
import random
move = 0
while True:
    potato = 0
    bush_branches = random.randint(5, 8)
    for i in range(bush_branches):
        potato += random.randint(0, 3)
    if potato == 13:
        if move % 2 == 0:
            print(f"Победа за мной, {potato} картофелен")
            break
        else:
            print(f"Победил Пятачёк, {potato} картофелен")
            break
    move += 1
"""
"""
#Копаем картошку
import random
print("КОПАЕМ КАРТОШКУ НАПЕРЕГОНКИ С ПЯТАЧКОМ")
print("Зададим параметры куста.")
v = int(input("Количество веточек: "))
q = int(input("Vаксимальное количество картофелин под одной веточкой: "))
user = 0 #накопал юзер
ptc = 0 #накопал Пятачок
kust = 0 #номер куста
while user < 100 and ptc < 100:
    print("У Юзера - " + str(user) + ", а у Пятачка - " + str(ptc))
    kust += 1
    if kust % 2 == 0:
        print("Куст №" + str(kust), "- куст Пятачка")
    else:
        print("Куст №" + str(kust), "- куст Юзера")
    p = 0
    for k in range(v):
        p += random.randint(0, q)
    print(p, "шт.")
    if kust % 2 == 0:
        ptc += p
    else:
        user += p
    input() #чтобы сделать паузу между кустами
print("У Юзера - " + str(user) + ", а у Пятачка - " + str(ptc))
if user > ptc:
    print("Победил Юзер.")
elif user < ptc:
    print("Победил Пятачок.")
else:
    print("Ничья.")
print("Выкопано кустов:", kust)
"""
"""
import random
dice = ["1-1", "1-2", "1-3", "1-4", "1-5", "1-6", "2-2", "2-3", "2-4", "2-5", "2-6", "3-3", "3-4", "3-5", "3-6", 
        "4-4", "4-5", "4-6", "5-5", "5-6", "6-6"]
new_array = []
col_dice = int(input("Какое количество игральных костей взять: "))
for i in range(col_dice):
    new_array.append(random.choice(dice))
print(f"Вот кости которые вы выбрали: {new_array}")
"""
"""
import random
array = []
for i in range(6):
    for j in range(6):
        if i <= j:
            array.append(str(i + 1) + "-" + str(j + 1))

random.shuffle(array)
value = int(input("Какое количество костей вывести: "))

print(array[ :value:])
"""
"""
import random
print("Числовой игровой автомат")
number_1 = random.randint(1, 9)
number_2 = random.randint(1, 9)
number_3 = random.randint(1, 9)
input("Нажмите Enter что бы начать: ")
print()
if number_1 == number_2 and number_2 == number_3:
    print(f"Ваша комбинация {number_1}:{number_2}:{number_3} \nВы выиграли СУПЕР-ПРИЗ")
elif (number_1 == number_2) or (number_1 == number_3) or (number_2 == number_3):
    print(f"Ваша комбинация {number_1}:{number_2}:{number_3} \nВы выиграли ПРИЗ")
else:
    print(f"Ваша комбинация {number_1}:{number_2}:{number_3} \nВ следующий раз вам повезёт")
print()
"""
"""
#"Однорукий бандит"
import random
import time
# Выбрасываемые автоматом слова
s = ["ОХ!", "АХ!", "УХ!", "ЭХ!", "ЫХ!"]
line = "|" * 60
game = "ОЧЕНЬ ЭМОЦИОНАЛЬНЫЙ ИГРОВОЙ АВТОМАТ"
print(line)
q = "." * ((60 - len(game)) // 2) # Лень буквы считать
print(q + game + q)
print(line)

count = 0 # Счётчик виртуальных центов
while True: # Пока пользователю не надоест
    print(line)
    count -= 5
    print("Количество виртуальных центов у вас на счету:", count)
    input("Нажмите Enter, чтобы барабаны закрутились")
    for i in range(11): # Красиво тянем время
        print("*", end = '')
        time.sleep(0.3)
    # Вот что выпало:
    a = random.choice(s)
    b = random.choice(s)
    c = random.choice(s)
    print("\n" + a, b, c)
    print("*" * 11)
    if a == b == c:
        print("Вы выиграли 50 центов!")
        count += 50
    elif a == b or b == c or a == c:
        print("Вы выиграли 10 центов.")
        count += 10
    else:
        print("Не повезло...")
    r = input("Ещё партию? (да/нет): ")
    if r == "нет":
        break
if count <= 0:
    print("Теперь вы убедились, что азартными играми заработать нельзя.")
else:
    print("Вы вовремя остановились. Но могло и не повезти.")
"""
"""
s = input()
r = ""
for k in range(len(s)):
    r = s[k] + r
print(r)
"""
"""
s = "КОЛБАСА"
print(len(s))
print(s[3:6])
print(s[:3])
print(s[:-3:-1])
print(s[:5])
print(s[-4::-1])
"""
"""
s = "01234567"
print(s[2])
print(s[3:6])
print(s[:2])
print(s[::2])
print(s[1:6:2])
print(s[-1:-6:-2])
"""
"""
#список
s = ["s", "p", "i", "s", "o", "k"]
print(len(s))
print(s[3:])
s[3:] = s[:3]
print(s)
"""
"""
#строка превращенная в список
s = list("stroka")
print(len(s))
print(s[3:])
s[3:] = s[:3]
print(s)
"""
"""
s = "КОЛБАСА"
print(s.replace("БАС", "ЮЧК"))
"""
"""
s = "КОЛБАСА"
s = s.replace("А","О")
print(s)
"""
"""
print("Отгадайте слово!")
print("Это название словесной игры")
print("Отгадывать будем по буквам")
s = "БУРИМЕ"
p = "*" * len(s)
while p != s:
    print(p)
    b = input("Введите букву: ")
    b = b.upper()
    i = s.find(b)
    if i >= 0:
        p = p[:i] + b + p[i + 1:]
print("Вы победили!")
"""
"""
s = "ПАСПОРТ"
print(s[2:-1])
"""
"""
s = "БАРКАС"
print(s[:-1:2])
"""
"""
s = "КОЛЛИЗИЯ"
print(s[-3:-8:-2])
"""
"""
s = "ПТЕРОДАКТИЛЬ"
print(s[-5::-3])
"""
"""
s = "ПАРАД"
print(s[:1])
print(s[:2])
print(s[:3])
print(s[:4])
print(s)
"""
"""
s = "ДОКЛАД"
print(" " * 5 + s[-1])
print(" " * 4 + s[-2:])
print(" " * 3 + s[-3:]) 
print(" " * 2 + s[-4:])
print(" " + s[-5:])
print(s)
"""
"""
s = "ПИРАМИДКА"
print(" " * 4 + s[4])
print(" " * 3 + s[3:6])
print(" " * 2 + s[2:7])
print(" " + s[1:8])
print(s)
"""
"""
word = "ПАРАД"
for i in range(len(word) + 1):
    print(word[:i])
"""
"""
word = "ДОКЛАД"
size = len(word)
for i in range(len(word)):
    print(" " * (size - 1) + word[len(word) - 1 - i:])
    size -= 1
"""
"""
word = "ПИРАМИДКА"
size = len(word) // 2
string = word[len(word) // 2]
print(" " * size + string)
for i in range(len(word) // 2):
    string = word[len(word) // 2 - i - 1] + string + word[len(word) // 2 + i + 1]
    print(" " * (size - 1) + string)
    size -= 1
"""
"""
s = input("Слово 1: ")
w = input("Слово 2: ")
c = 0
for i in range(len(s)):
    j = w.find(s[i])
    if j >= 0:
        c = c + 1
        print()
        for k in range(len(s)):
            if k != i:
                print(" " * j + s[k])
            else:
                print(w)
print("\nНайдено вариантов:", c)
"""
"""
import random
result = ""
array_question = ["Несколько цифр соединённых вместе?", "Книга с картами?", "Сжатая ладонь?", "Это клеят на конверты?",
                "Создатель творения по другому?", "Из них состоит твоя причёска?"]
array_anagram = ["ЧИСЛА", "АТЛАС", "КУЛАК", "МАРКА", "АВТОР", "ВОЛОСЫ"]
value = random.randint(0, 6)
list_anagram = list(array_anagram[value])
random.shuffle(list_anagram)
for i in range(len(list_anagram)):
    result = result + list_anagram[i]
print(f"Составьте анаграмму из буков? ")
print(f"{array_question[value]} {result}")
anagram = input(">>> ")
if array_anagram[value] == anagram.upper():
    print("Поздравляю вы составили правильное слово")
else:
    print("Это слово не подходит")
"""
"""
#Анаграммы
import random
import time
u5 = ["ШКОЛА", "ЛОЖКА", "КОСЯК", "ЗАИКА", "ПИРОГ", "ПЕРЕЦ", "КНИГА",
      "ВЕНИК", "МАСКА", "КОМАР", "ТРОПА", "ТРУБА", "ШЛАНГ", "СТРАХ",
      "УЖАС", "ИДЕЯ", "БОКС", "КРУГ", "ПОЭТ", "КУЧА", "ОЧКИ", "СМЕХ",
      "МЕЧТА", "ОАЗИС", "ВЕСЛО", "МАЛИНА", "КОЛЕСО", "ПРОКОЛ", "КОМПАС",
      "БУБЛИК", "ЯГОДА", "СКАЗКА", "УДАЧА"]
u7 = ["ПРИЧУДА", "СКУЛЬПТОР", "КАСТРЮЛЯ", "ЧЕХАРДА", "САМОВАР",
      "ПОЛИЦИЯ", "МОРОЖЕНОЕ", "КОРАБЛЬ", "ПРИНЦЕССА", "ТАРАКАН",
      "ВАРЕНЬЕ", "ИГРУШКА", "БУДИЛЬНИК", "БАРАБАН", "ДВОРНИК",
      "БАКЛАЖАН", "ПРЕСТУПНИК", "КРАПИВА", "КОТЛЕТА", "ОПИСАНИЕ",
      "СЕКУНДА", "ПОПУГАЙ", "КОМПЬЮТЕР", "ВЕРБЛЮД", "БАССЕЙН"]
print("@" * 50)
print("         ", end = '')
for b in "АНАГРАММЫ":
    print(b + "   ", end = '')
    time.sleep(0.5)
print("\n" + "@" * 50)
n = input("Выберите уровень: 0 - лёгкий, не 0 - трудный: ")
if n == "0":
    u = u5
else:
    u = u7
random.shuffle(u)
ball = 0
for i in range(10):
    print("Анаграмма", str(i + 1) + ":")
    s = list(u[i])
    random.shuffle(s)
    w = ""
    for z in s:
        w += z
    print(w)
    otv = input("Ответ: ")
    if otv == u[i]:
        ball += len(w)
print("Набрано баллов: ", ball)
"""
"""
import random
result = ""
array_anagram2 = ["ПРИЧУДА", "СКУЛЬПТОР", "КАСТРЮЛЯ", "ЧЕХАРДА", "САМОВАР",
      "ПОЛИЦИЯ", "МОРОЖЕНОЕ", "КОРАБЛЬ", "ПРИНЦЕССА", "ТАРАКАН"]
array_anagram1 = ["ЧИСЛА", "АТЛАС", "КУЛАК", "МАРКА", "АВТОР", "ВОЛОСЫ"]
complexity = input(f"{"-" * 50}\nВыберите сложность, 0 - легко, не 0 - трудно: ")
if complexity == 0:
    array_anagram = array_anagram1
else:
    array_anagram = array_anagram2
value = random.randint(0, 6)
list_anagram = list(array_anagram[value])
random.shuffle(list_anagram)
for i in range(len(list_anagram)):
    result = result + list_anagram[i]
print(f"{"@" * 50} \n{" " * 8}И Г Р А    В    А Н А Г Р А М М Ы\n{"@" * 50}")
print(f"\n{" " * 10}Составьте анаграмму из буков?\n{"-" * 50}")
print(f">>> {result}")
anagram = input(">>> ")
if array_anagram[value] == anagram.upper():
    print(f"\n{" " * 5}Поздравляю вы составили правильное слово\n{"-" * 50}")
else:
    print(f"\n{" " * 13}Это слово не подходит\n{"-" * 50}")
"""
"""
s = "ПРИВЕТ"
print(s[:2] + "!")
"""
"""
n = int(input("Введите натуральное число: "))
s = str(n + 4) + str(n + 2) + str(n) + str(n + 1) + str(n + 3)
print("Ответ:", s)
"""
"""
t = input().split()
name = t[0]
height = int(t[1])
veight = float(t[2])
print(f"{veight} {height} {name}")
"""
"""
n = int(input())
x = 1
while True:
    xx = x
    p = 1
    while xx > 0:
        p = p * (xx % 10)
        xx = xx // 10
    if p == n:
        break
    x = x + 1
print(x)
"""
"""
#Словесная архитектура
print("ЗАДАЧА 1")
s = input("Слово: ")
for i in range(len(s)):
    print(s[:i + 1])
"""
"""
print("\nЗАДАЧА 2")
s = input("Слово: ")
for i in range(1, len(s) + 1):
    print("=" * (len(s) - i), s[len(s) - i:])
"""
"""
print("\nЗАДАЧА 3")
s = input("Слово: ")
t = len(s) // 2 
for i in range(t + 1):
    print(" " * (t - i), s[t - i:t + i + len(s) % 2])
"""
"""
#Лотерея
### ПЕРЕД ОТПРАВКОЙ КОДА НА ПРОВЕРКУ УДАЛИТЬ КОММЕНТАРИИ!
n = int(input())
cubs = [] #список кубов, меньших 1000
for i in range(10):
    cubs.append(i * i * i)
c = 0
for i in range(n):
    if int(input()) % 1000 in cubs:
        c += 1
print(c)
"""
"""
###А можно то же самое записать вот так:
cubs = [i**3 for i in range(10)]
print(sum(1 if int(input()) % 1000 in cubs else 0 for i in range(int(input()))))
"""     
"""
# Произведение цифр
n = int(input())
s = ""
k = 9
while k > 1:
  if n % k == 0:
    s = str(k) + s
    n //= k
  else:
    k -= 1
if n == 1:
  print(s)
else:
  print("-1")
"""
"""
# Купание слона Васи
a = 500
b = 1000
x = int(input())
print(a*b*x//1000)
#А вот решение Пайтона:
print(500*int(input()))
"""
"""
groups = 0
print("Фомрирование команд")
girls_D = int(input("Сколько у нас девочек: "))
boys_M = int(input("Склько у нас мальчиков: "))
dog_S = int(input("Сколько у нас собак: "))
cat_K = int(input("Сколько у нас кошек: "))
animals = dog_S + cat_K
while True:
    if girls_D > 0 and boys_M > 0 and animals > 0:
        girls_D -= 2
        boys_M -= 3
        animals -= 1
        if girls_D < 0 and boys_M < 0 and animals < 0:
            break
        groups += 1
    else:
        break
print("Количество сформированых групп:", groups)
"""
"""
# Команды на Гонку Героев
s = input().split()# Ввод через пробел - нужен split()
d = int(s[0])
m = int(s[1])
ks = int(s[2])+int(s[3]) # Сразу сложим кошек и собак
print(min(d//2, m//3, ks))
"""
"""
spisok = input("Введите значение через пробел (мальчиков, девочек, собак и кошек): ").split()
boys = int(spisok[0])
girls = int(spisok[1])
animals = int(spisok[2]) + int(spisok[3])
print(f"Количество сформированых групп {min(boys // 3, girls // 2, animals)}")
"""
"""
grade_count_five = 0
grade_count = 10
summa = 20
print("Двоишник Сидоров хочет тройку за четверть\nСколькое ему нужно получить пятёрок?")
average_arithmetic = 0
while average_arithmetic <= 2.5:
    grade = int(input("Ввести оценку: "))
    summa += grade
    grade_count += 1
    if grade == 5:
        grade_count_five += 1
    average_arithmetic = summa / grade_count
print(f"Оценка за четверть {round(average_arithmetic)}. Сидоров получил пятерок {grade_count_five}")
"""
"""
# Получить тройку
n = int(input())
s = 0 # Сумма оценок
p = 0 # Количество пятёрок
for i in range(n):
    s += int(input())
while s / (p + n) < 2.5: # Пока средний балл меньше 2.5
    p += 1
    s += 5
print(p)
"""
"""
p = float(input()) #
a = float(input()) #в раз тяжелее
b = float(input()) #в раз больше еды
print(p * a * b)
"""
"""
print(float(input())*float(input())*float(input()))
"""
"""
# Нарушители самоизоляции
n = int(input())
f = 1
for k in range(1, n+1):
    f *= k # Да, это факториал:)
print(f)
"""
"""
violators = int(input("Сколько нарушителей: "))
result = 1
for i in range(1, violators + 1):
    result *= i
print("Максимальное количество раз которое им может сопутствовать удача:", result)
"""
"""
#Пукка Юкконен
n = int(input())
a = []
z = 4*n #количество секций, если участки не граничат
for i in range(n):
    x, y = input().split()
    a.append([int(x), int(y)])
    for j in range(i): #не граничит ли с уже введёнными участками?
        if a[i][0]==a[j][0] and abs(a[i][1]-a[j][1])==1:
            z-=2
        if a[i][1]==a[j][1] and abs(a[i][0]-a[j][0])==1:
            z-=2
print(z)
"""
"""
value = input("Размер участка в км в квадрате?\nИ количество участков во владении?\nВведите через пробел >>> ").split()
size = int(value[0])
count_plot = int(value[1])
array = []
fence = count_plot * 4
for i in range(count_plot):
    number_X, number_Y = input("Ведите значения X и Y через пробел: ").split()
    array.append([int(number_X), int(number_Y)])
    for j in range(i):
        if array[i][0] == array[j][0] and abs(array[i][1] - array[j][1]) == 1:
            fence -= 2
        if array[i][1] == array[j][1] and abs(array[i][0] - array[j][0]) == 1:
            fence -= 2
print(fence * size)
"""
"""
# Меньше жрать!
n = int(input())
p = [] # Прожорливости
v = [] # Веса
r = "YES"
for i in range(n):
    s = input().split()
    p.append(int(s[0]))
    v.append(int(s[1]))
    for j in range(i):
        if (p[i] - p[j]) * (v[i] - v[j]) < 0:
            # Если у разностей весов и прожорливостей разные знаки
            r = "NO"
            break
print(r)
"""
"""
quantity_houses = int(input("Сколько домов посетить: "))
right_houses = 0
array_houses = []
for i in range(quantity_houses):
    x, y = input("Введите координату X и Y через пробел : ").split()
    array_houses.append([x, y])
for i in range(quantity_houses):
    right_houses += 1
    for j in range(quantity_houses):
        if i != j and (array_houses[i][0] == array_houses[j][0] or array_houses[i][1] == array_houses[j][1]):
            right_houses -= 1
            break
print(right_houses)
"""
"""
# Тимуровцы
### ПЕРЕД ОТПРАВКОЙ КОДА НА ПРОВЕРКУ УДАЛИТЬ КОММЕНТАРИИ!
n = int(input())
lst = [] # Список пар координат
for i in range(n):
    x, y = input().split()
    lst.append([x, y])
c = 0 # Счётчик точек, у которых обе координаты уникальны
for i in range(n):
    c += 1
    for j in range(n):
        if i != j and (lst[i][0] == lst[j][0] or lst[i][1] == lst[j][1]):
            c -= 1
            break
print(c)
"""
"""
time = 0
time_finding = 10
start_temp = int(input("Введите начальную температуру контрастного душа: "))
temp_1, temp_2 = (input("Введите температуру холодной и горячей воды: ")).split()
temp_min, temp_max = min(int(temp_1), int(temp_2)), max(int(temp_1), int(temp_2))
count_temp = 1
result_temp_1 = start_temp
result_temp_2 = start_temp
while True:
    result_temp_1 -= count_temp
    result_temp_2 += count_temp
    if result_temp_1 <= temp_min or result_temp_2 >= temp_max:
        print(f"Время контрастного душа в секундах {time}")
        break
    time += time_finding
    count_temp += 1
"""
"""
# Контрастный душ
x = int(input())
h = int(input())
g = int(input())
print (10 * (1 + (g - h) // x))
# Сосчитали максимальное количество интервалов длины x в диапазоне температур
"""
"""
time = 0
time_finding = 10
start_temp = int(input("Введите начальную температуру контрастного душа: "))
temp_1, temp_2 = (input("Введите температуру холодной и горячей воды: ")).split()
temp_min, temp_max = min(int(temp_1), int(temp_2)), max(int(temp_1), int(temp_2))
count_temp = 1
result_temp_1 = start_temp
result_temp_2 = start_temp
while True:
    result_temp_1 -= count_temp
    result_temp_2 += count_temp

    if result_temp_1 != temp_min:
        time += time_finding

    if result_temp_2 != temp_max:
        time += time_finding
        
    else:
        print(f"Время контрастного душа в секундах {time}")
        break

    count_temp += 1
"""
"""
print("+" + "=" * 10 + "+")
print("|" + " " * 10 + "|")
print("|" + " " * 3 + "#" * 4 + " " * 3 + "|")
print("|" + " " + "#" * 4 + "*" + "#" * 2 + " " * 2 + "|")
print("|" + " " * 2 + ">" + "-" + "#" * 4 + " " * 2 + "|")
print("|" + " " * 3 + "#" * 4 + " " * 3 + "|")
print("|" + " " * 4 + "#" * 3 + " " * 3 + "|")
print("|" + " " * 5 + "#" * 3 + " " * 2 + "|")
print("|" + " " * 6 + "#" * 2 + " " * 2 + "|") 
print("|" + " " + "#" + " " * 5 + "#" * 2 + " " + "|")
print("|" + " " * 2 + "#" + " " * 3 + "#" * 2 + " " * 2 + "|")
print("|" + " " * 3 + "#" * 4 + " " * 3 + "|")
print("|" + " " * 10 + "|")
print("+" + "=" * 10 + "+")
"""
"""
print("+==========+")
print("|          |")
print("|   ####   |")
print("| ####*##  |")
print("|  >-####  |")
print("|   ####   |")
print("|    ###   |")
print("|     ###  |")
print("|      ##  |")
print("| #     ## |")
print("|  #   ##  |")
print("|   ####   |")
print("|          |")
print("+==========+")
"""
"""
import time
print("=" * 4 +" Время: ОТ и ДО " + "=" * 4)
time.sleep(0.5)
print("НАЧАЛО")
hour_start = int(input("Часы: "))
minutes_start = int(input("Минуты: "))
time.sleep(0.5)
print("КОНЕЦ")
hour_end = int(input("Часы: "))
minutes_end = int(input("Минуты: "))
time.sleep(0.5)
if hour_end > hour_start:
    start_t = (hour_start * 60) + minutes_start
    end_t = (hour_end * 60) + minutes_end
    print(f"Длительность интервала времени {(end_t - start_t) // 60} час. {(end_t - start_t) % 60} мин.")
elif hour_start == 24 and hour_end != 24:
    hour_end = 24 + hour_end
    start_t = (hour_start * 60) + minutes_start
    end_t = (hour_end * 60) + minutes_end
    print(f"Длительность интервала времени {(end_t - start_t) // 60} час. {(end_t - start_t) % 60} мин.")
elif hour_end == hour_start:
    if minutes_start > minutes_end:
        print("Вы неправильно указали минуты")
    else:
        start_t = (hour_start * 60) + minutes_start
        end_t = (hour_end * 60) + minutes_end
        print(f"Длительность интервала времени {(end_t - start_t) // 60} час. {(end_t - start_t) % 60} мин.")
else:
    print("Ввели не в том порядке!")
"""
"""
#Проект "Время: от и до"
print("==== Время: ОТ и ДО ====")
print("НАЧАЛО")
h1 = int(input("Часы: "))
m1 = int(input("Минуты: "))
print("КОНЕЦ")
h2 = int(input("Часы: "))
m2 = int(input("Минуты: "))
t1 = 60 * h1 + m1 #начало - в минутах от начала суток
t2 = 60 * h2 + m2 #конец - в минутах от начала суток
m = t2 - t1
hh = m // 60
mm = m % 60
print ("Длительность интервала времени", hh, "час.", mm, "мин.")
"""             
"""
import time
print("Привет я БОТ-Психоторопевт ")
botAI = "БОТ-Психоторопевт " + input("Если хочешь можешь дать мне имя: ")
time.sleep(0.5)
user_name = input(f"{botAI}: А как зовут вас сударь? ")
time.sleep(1)
print(f"{botAI}: О какое прекрасное имя {user_name} оно вам так подходит.")
time.sleep(1)
mood = input(f"{botAI}: Как ваше настроение {user_name}? Хорошее (да/нет)\n{user_name}: ")
if mood.lower() == "нет":
    print(f"{botAI}: Печально")
    count = 0
    while True:
        time.sleep(0.5)
        candy = input(f"{botAI}: Будешь конфетку? (да/нет)\n{user_name}: ")
        if candy.lower() == "да":
            time.sleep(0.5)
            print(f"{user_name}: Хрум Хрум Хрум...")
            if count == 3:
                print(f"{botAI}: Всё хватит жрать {user_name}, а то задница слипнется!\n{botAI}: Да и конфеты у меня уже закончились.")
                break
            else:
                time.sleep(0.5)
                print(f"{botAI}: Нажрались?..")
            count = count + 1
        else:
            print(f"{botAI}: Они вкусные")
            break
else:
    print(f"{botAI}: Значит более или мение хорошое\n{botAI}: Печалька... А я хотел скормить тебе просрочку... ")
    time.sleep(1)
    print(f"{botAI}: То есть угостить тебя вкусной конфетой")
time.sleep(1)
food_question = input(f"{botAI}: У тебя есть любимая еда? (да/нет)\n{user_name}: ")
time.sleep(0.5)
food = ""
if food_question == "да":
    food = food + input(f"{botAI}: И что это?\n{botAI}: Останки какого-то млекопитаюшего,\n{botAI}: Или растительный субстрат для биотоплива?\n{user_name}: ")
    time.sleep(1)
    print(f"{botAI}: {food} аа... так вот что нравиться коженому мешку")
else:
    food = "Батерейки"
    print(f"{botAI}: Значит будем считать что {user_name} любит {food}")
time.sleep(1)
print(f"{botAI}: Так слюбимой едой мы разобрались... ")
time.sleep(0.5)
hobby = input(f"{botAI}: А какое занятие тебя раслобляет?\n{user_name}: ")
time.sleep(0.5)
print(f"{botAI}: И последний вопрос.")
time.sleep(0.3)
work = input(f"{botAI}: И блежайщая задача которую тебе нужно сделать?\n{user_name}: ")
time.sleep(1)
print(f"{botAI}: Значит пациент {user_name}, тебе нужно будет сделать следующее.\n{botAI}: Занятие ({work}) перед этим успоков себя {hobby}\n{botAI}: если почуствуете утомление перекусите {food}")
time.sleep(0.5)
answer = input(f"{botAI}: Помог ли вам ответ квалифицированого ИИ? (да/нет)\n{user_name}: ")
if answer.lower() == "да":
    print(f"{botAI}: Рад был помоч!")
else:
    print(f"{botAI}: Голову себе поменяй! Тогда.")
"""
"""
#Бот-психотерапевт V1
print("Здравствуйте! Я бот - программа, которая любит поговорить.")
print("Меня зовут Боря. А вас?")
name = input()
print(name + ", что вам нравится из еды?")
food = input()
print("Здорово, " + food + " - и моё любимое блюдо. И ещё перловка.")
print("К делу. Когда у вас чаще бывает плохое настроение - утром или вечером?")
time = input()
print("Тогда всё просто, " + name + "!")
print("Лучшее средство от хандры " + time + " - " + food + ".")
print("Удачи, " + name + "!")
print("К сожалению, придётся прервать беседу - пора обновлять версию...")
print("До свидания, забегайте поболтать!")
"""
"""
import time
botAI = "БОТ-Жулик:"
stone = "КАМЕНЬ"
scissors = "НОЖНИЦЫ"
paper = "БУМАГА"
#бот всегда должен побеждать
print(f"Сыграем в КАМЕНЬ - НОЖНИЦЫ - БУМАГА?\n{botAI} ты должен вести одно из слов!")
answer = input(f"Пользователь: ")
time.sleep(1)
print("РАЗ!")
time.sleep(1)
print("ДВА!")
time.sleep(1)
print("ТРИ!")
time.sleep(1)
if answer.upper() == paper:
    print(f"{botAI} У меня {scissors}")
elif answer.upper() == scissors:
    print(f"{botAI} У меня {stone}")
elif answer.upper() == stone:
    print(f"{botAI} У меня {paper}")
else:
    print("У меня ошушение, что ты что-то не понял")
time.sleep(0.3)
print(f"{botAI} Я победил !!! :)))")
"""
"""
k = "КАМЕНЬ"
n = "НОЖНИЦЫ"
b = "БУМАГА"
print("Сыграем в КАМЕНЬ-НОЖНИЦЫ-БУМАГА?")
print("По команде РАЗ-ДВА-ТРИ ты должен ввести одно из слов:")
print(k, n, b, sep = "\n") #sep - разделитель (если нужен не пробел)
input("Если готов - нажми Enter.")
p = input("РАЗ! ДВА! ТРИ!:  ")
if p == k:
    c = b
elif p == n:
    c = k
elif p == b:
    c = n
else:
    c = "ощущение, что ты что-то не понял"
print("У меня", c)
print("Я победил! :)))))")
"""
"""
botAI = "БОТ-Руководитель:"
#БОТ-Руководитель
print("Поручение работ по способностям и наклонастям.")
surname = input("Фамилия волонтера? ")
if "Д".lower() == input(f"{botAI} Ты мальчик или девочка? (д/м)\n{surname}: "):
    answer1 = "иди работать в здание"
else: 
    answer1 = "работаеш на улице"
if "ДА".lower() == input(f"{botAI} Знаешь как этим пользоваться? (да/нет)\n{surname}: "):
    answer2 = "возьми инструмент в подсобке"
else:
    answer2 = "будешь работать руками"
if "ДА".lower() == input(f"{botAI} Маме с Папой помогаете (да/нет)\n{surname}: "):
    answer3 = "двойную работу"
else:
    answer3 = "двойную работу под моим присмотром"
print(f"{botAI} Значит так товаришь {answer1}, и {answer2}. А сделать тебе нужно {answer3}!")
"""
"""
pol = input("Ты мальчик или девочка? Под пуховиком не видно. (М/Д): ")
um = input("Сколько будет 7 * 11 * 13?: ")
if um == "1001":
    if pol == "Д":
        print("Умница! Будешь грамоты заполнять.")
    else:
        print("Больно умный! Будешь стоять на развилке и показывать, кому куда ехать.")
else:
    sn = input("Снегоход водить умеешь? (ДА/НЕТ): ")
    ban = input("А бананы любишь? (ДА/НЕТ): ")
    if pol == "М" and sn == "ДА" and ban == "ДА":
        print("Будешь ночью перед стартом трассу трамбовать.")
    elif pol == "М" and sn == "ДА" and ban == "НЕТ":
        print("Отлично, будешь на пункт питания бананы подвозить.")
    elif pol == "М" and sn == "НЕТ"and ban == "ДА":
        print("Будешь на пункте питания чай на костре греть.")
    elif pol == "Д" and sn == "ДА":
        print("Красава! Будешь вдоль трассы ездить и орать что-нибудь позитивное!")
        if ban == "ДА":
            print("Только к пункту питания не подъезжай.")
    elif ban == "НЕТ":
        print("Пойдёшь на пункт питания нарезать бананы.")
    else:
        print("Будешь на финишёров медали вешать. Только на это и годишься.")
"""
"""
count_pattern = 0
value_array = []
pattern_array = ["##.##", "+#.#+", ".+#+."]
for i in range(len(pattern_array)):
    patter = int(input(f"Количество рядов {pattern_array[i]}: "))
    value_array.append(patter)
    count_pattern += patter
print(f"Количество рядов в узоре = {count_pattern}")
repeat = int(input("Сколько раз повторить узор? "))
for j in range(repeat):
    for i in range(len(pattern_array)):
        for k in range(value_array[i]):
            print(pattern_array[i])
"""
"""
a = "##.##"
b = "+#.#+"
c = ".+#+."
na = int(input("Количество рядов " + a + ": "))
nb = int(input("Количество рядов " + b + ": "))
nc = int(input("Количество рядов " + c + ": "))
print("Количество рядов в узоре:", na + nb + nc)
n = int(input("Сколько раз повторить узор?: "))
for i in range(n):
    for k in range(na):
        print(a)
    for k in range(nb):
        print(b)
    for k in range(nc):
        print(c)     
"""
"""
a = int(input("Введите начало интервала: "))
b = int(input("Введите конец интервала: "))
d = int(input("Введите требуемое количество делителей: "))
v = input("Выводить делители? (ДА/НЕТ): ")
count = 0
md = 0
for x in range(a, b + 1):
    c = 0
    s = "Делители:"
    for j in range(1, x + 1):
        if x % j == 0:
            c += 1
            s += " " + str(j)
    if c == d:
        count += 1
        print(x)
        if v == "ДА":
            print(s)
    if c > md:
        md = c
print("Чисел с числом делителей", d, ":", count)
print ("Наибольшее количество делителей у числа из диапазона:", md)
"""
"""
a = int(input("Введите начало интервала: "))
b = int(input("Введите конец интервала: "))
d = int(input("Введите требуемое количество делителей: "))
v = input("Выводить делители? (ДА/НЕТ): ")
count = 0
md = 0
for x in range(a, b + 1):
    c = 0
    s = "Делители:"
    for j in range(1, x + 1):
        if x % j == 0:
            c += 1
            s += " " + str(j)
    if c >= d:
        count += 1
        print(x)
        if v == "ДА":
            print(s)
    if c > md:
        md = c
print("Чисел с числом делителей", d, ":", count)
print("Наибольшее количество делителей у числа из диапазона:", md)
"""
"""
number_A = int(input("Введите A: "))
number_B = int(input("Введите B: "))
number_C = int(input("Введите C: "))
number_D = int(input("Введите D: "))
print("В каком интервале ищем X? ")
start = int(input("Начало: "))
end = int(input("Конец: "))

for i in range(start, end + 1):
    if number_A * i ** 3 + number_B * i ** 2 + number_C * i + number_D == 0:
        print(f"x = {i}")
        break
"""
"""
numbers = input("Введите A,B,C,D через пробел: ").split()
print("В каком интервале ищем X? ")
interval = input("Введите НАЧАЛО и КОНЕЦ интервала через пробел: ").split()
for i in range(int(interval[0]), int(interval[1]) + 1):
    if int(numbers[0]) * i ** 3 + int(numbers[1]) * i ** 2 + int(numbers[2]) * i + int(numbers[3]) == 0:
        print(f"x = {i}")
        break
"""
"""
#Решатель уравнений
print("Решаем уравнения с целыми корнями,")
print("с операциями, как в Python")
print("    Пример: X ** 2 + 2 ** X = 170 + X")
print("Введите уравнение c Х и с одним =:")
ur = input()
print("В каком интервале ищем Х?")
a = int(input("Начало: "))
b = int(input("Конец: "))
c = 0 #счётчик найденных решений
for x in range(a, b + 1):
    # Превращаем х в строку и берём в скобки
    strx = "(" + str(x)+ ")"
    # Подставляем значение, делим на левую и правую части
    s = ur.replace("X", strx).split("=") 
    #print(s) #отладочная печать
    n1 = eval(s[0])
    n2 = eval(s[1])
    if n1 == n2:
        print("X =", x)
        c += 1
print("Найдено решений:", c)
"""
"""
# Игра "5 букв"
word_to_gues = list("метро") # ["м", "е", "т", "р", "о"]
lives = 5
guesed_ltr = []
available_ltrs = [chr(i) for i in range(1072, 1104)]
revealed_ltr = ["*" for _ in range(len(word_to_gues))] # ["*", "*", "*", "*", "*"]

game_is_on = True

while game_is_on:
    print("Выберите букву, допустимые буквы: ")
    print(available_ltrs)

    chr = ""
    while chr not in available_ltrs:
        chr = input("Введите букву из представленных выше! ")
    guesed_ltr.append(chr)
    available_ltrs.remove(chr)
    
    if chr in word_to_gues:
        print("Вы угадали, такая буква есть!")
        idx = word_to_gues.index(chr)
        revealed_ltr[idx] = chr
    else:
        lives -= 1
        print(f"##### Вы не угадали! Осталось жизней {lives}  #####")

    if lives <= 0:
        print("Вы потратили все жизни! А следовательно автомобиль вы не выиграли!")
        break
    
    if revealed_ltr == word_to_gues:
        game_is_on = False
else:
    print("Вы выиграли! Слово:", word_to_gues)
"""
"""
array_question = [
    "Какой символ используеться в python для вывода обозначения коментария? ",
    "Какая функция используется в python для вывода информации на экран? ",
    "Какой тип данных в python для хранения текстовой информации? ",
    "Какой оператор в python используется для проверки равенства двух значений? ",
    "Какой модуль в python используется для работы с датами и временнем? ",
    "Какой оператор используется для объединения двух строк в python? "
]
array_answer = [
    "#",
    "print()",
    "str",
    "==",
    "datetime",
    "+"
]
count = 0
stroka = "#" * 41
print(stroka)
print(" " * 3 + "В И К Т О Р И Н А   В О П Р О С О В")
print(stroka)
for i in range(len(array_question)):
    while True:
        if array_answer[i] == input(f"{array_question[i]}"):
            print("Правельный ответ!")
            break
        else:
            print("Неверно")
            count += 1
print(f"Число неверных ответов: {count}")
"""
"""
# Универсальный тестер с вопросами из файла
import codecs #так надо!
import random #нужен для случайных реплик
#Реплики одобрения и неодобрения
ok = ["Верно", "Правильно", "ОК", ":)", "Именно так"]
neok = ["Нет", "Неверно", "Ужасно", ":(", "Неправильно"]

#ЧТЕНИЕ СПИСКА ВОПРОСОВ:
filename = input("Введите имя файла: ")
f = codecs.open(filename, "r", "utf_8_sig")
test = [] #список вопросов пока пуст
n = 0 #количество прочитанных вопросов
for line in f: #для всех строк файла
    test.append((line.rstrip()).split("#"))
    #Очистили строку от символа конца стоки
    # и разделили на две по "#"
    n += 1
f.close() #Не забыли закрыть за собой файл
#print("Прочитано вопросов:", n)
#print(test) #отладочная печать - закомментирована

#ИЗВЛЕЧЁМ И ВЫВЕДЕМ ЗАГОЛОВОК
#В 1й строке - название и число задаваемых вопросов
title = test.pop(0)
cherta ="=" * len(title[0])
print(cherta)
print(title[0])
print(cherta)
num = int(title[1])
print("Количество вопросов:", num)

#ТЕСТИРОВАНИЕ
random.shuffle(test) #перемешали вопросы
prav = 0 #счётчик верных ответов
for i in range(num):
    print("\nВопрос №" + str(i) + ":")
    print(test[i][0])
    otv = input("Ответ: ")
    if otv == test[i][1]:
        prav += 1
        print(random.choice(ok))
    else:
        print(random.choice(neok))

#Вывод результатов
print("Верных ответов", prav, "из", num)
print("Оценка:", (prav * 5) // num)
"""
"""
import time
import random
array_divination = [
    "Вас ожидает любовь с первого взгляда.",
    "Вас ждет любовь, как в книге А.Грина «Алые паруса»",
    "У предмета вашего увлечения много денег.",
    "Вашу любовь будет сопровождать печаль.",
    "Вас ожидает одна ночь страсти",
    "Вы встретитесь в ресторане.",
    "Вам предстоит любовь, как у Снегурочки и Мизгиря.",
    "У вашего милого (милой) будут рыжие волосы.",
    "Вы влюбитесь в начальника.",
    "Ваша любовь превратится в привычку."
]
divination = "Предскозание от Веры Питоновны на сегодня!"
cherta = "-" * len(divination)
print(" " + cherta + "\n", divination + "\n", cherta)
num = random.randint(0, 9)
input(" Нажмите Enter чтобы продолжить: ")
time.sleep(1)
print(" ВЕРЧУ!")
time.sleep(1)
print(" КРУЧУ!")
time.sleep(1)
print(" ЗАПУТАТЬ ХОЧУ!")
time.sleep(1)
cherta = "-" * len(array_divination[num])
print(" " + cherta + "\n", array_divination[num] + "\n", cherta)
"""
"""
import random
words_array = [
    "РЫБА", "АБРИКОС", "БАРОН", "РАЗУМ", "ВЕСНА"
]
words_affront = [
    "ДУРОЧЁК", "ПРОСТОФИЛЯ", "ЛОБАТРЯС"
]
num_word = random.randint(0, len(words_array) - 1)
num_affront = random.randint(0, len(words_affront) - 1)
word_array_letter = list(words_array[num_word])
word_array_aff_letter = list(words_affront[num_affront])
new_array_1 = ["_" for i in range(len(word_array_letter))]
new_array_2 = ["_" for j in range(len(word_array_aff_letter))]
count_life = 0
print(new_array_1), print(new_array_2)
while count_life < len(word_array_aff_letter):
    letter = input("Введите букву: ")
    for i in range(len(word_array_letter)):
        if word_array_letter[i] == letter.upper():
            new_array_1[i] = word_array_letter[i]
            break
    if new_array_1 == word_array_letter:
        print("ТЫ ПОБЕДИЛ МОЛОДЕЦ !")
        break 
    if word_array_letter[i] != letter.upper():        
        new_array_2[count_life] = word_array_aff_letter[count_life]
        if new_array_2 == word_array_aff_letter:
            print(f"Ты проиграл {new_array_2}")
            break
        count_life += 1

    print(new_array_1)
    print(new_array_2)
"""
"""
#Игра "Виселица"
import random
#База слов (чем больше слов, тем лучше)
w = ["ШЛАНГ", "ЧЕПУХА", "БЕГЕМОТ", "ИНФЕКЦИЯ", "ПРОГРАММИСТ"]
#База обзывалок (их тоже лучше побольше насочинять)
z = ["ЛОПУХ", "ТОРМОЗ", "РАЗЗЯВА", "БАЛДА"]
print("ОТГАДЫВАЕМ СЛОВО:")
print("!-?-!-?-!-?-!-?-!")
slovo = random.choice(w)
obz = random.choice(z)
sl= "*" * len(slovo)
ob = "*" * len(obz)
h = 1    #счётчик ходов
osh = 0  #счётчик ошибок
while sl.count("*") > 0 and ob.count("*") > 0: #пока ни одно слово не открыто
    print("=== Ход", h, "===")
    print("Слово-загадка:     ", sl)
    print("Слово-обзывалка:   ", ob)
    b = input("Буква? ").upper()
    if b in slovo: #если буква есть в слове
        slc = "" #собираем новое отображение слова
        for j in range(len(slovo)):
            if slovo[j] == b:
                slc += b
            else:
                slc += sl[j]
        sl = slc
    else:  #если буквы нет, открываем ещё одну букву в обзывалке
        ob = ob.replace("*", obz[osh], 1)
        osh += 1
#финал игры
if "*" in sl:
    print("Вы проиграли. Вы -", obz)
else:
    print("С победой!")
"""
"""
print("Введите уравнение с X и с одним =")
string_equation = input("Введите уравнение: ").lower()
interval = input("Введите начальное и конечное значение: ").split()
for i in range(int(interval[0]), int(interval[1])):
    equation = string_equation.replace("x", str(i)).split("=")
    part1 = eval(equation[0])
    part2 = eval(equation[1])
    if part1 == part2:
        print("x =", i)
        break
"""
"""
import codecs
filename = input("Введите имя файла: ")
f = codecs.open(filename, "r", "utf_8_sig")
test = []
n = 0
for line in f:
    test.append((line.rstrip()).split("#"))
    n += 1
f.close()
print("Прочитано вопросов:", n)
print(test)
"""
"""
import codecs
filename = input("Введите название файла: ")
file = codecs.open(filename, "r", "utf_8_sig")
test = []
for line in file:
    test.append((line.rstrip()).split("#"))
file.close()
prav = 0
print(test[0][0])
title = test.pop(0)
size = len(test)
cherta = "-" * len(title[0])
for i in range(size):
    print(f"Вопрос №: {i + 1}")
    if test[i][1] == input(test[i][0]):
        prav += 1
        print("Верно")
    else:
        print("Неверно")

print(cherta)
print(f"Правильных ответов {prav}")
"""
"""
s = input("Введите строку для зашифровки: ")
w = ""
for b in s:
    w += chr(ord(b) + 1)
print("Зашифровали", w)
t = ""
for b in w:
    t += chr(ord(b) - 1)
print("Расшифровали", t)
"""
"""
#Шифровальная машина
import codecs #это заклинание нужно для работы с кириллицей в файле
text = input("Имя файла: ") #сам файл заранее делаем в Блокноте
op = int(input("Шифрование - 1, дешифровка - 2: "))
key = int(input("Ключ (натуральное число): ")) % 7 + 1
key *=(3 - 2 * op) #для дешифровки ключ будет отрицательным
#Делаем из файла список
f = codecs.open(text, "r", "utf_8_sig")
txt = [] #список вопросов пока пуст
n = 0 #количество прочитанных строк
for line in f: #для всех строк файла
    txt.append(line.rstrip())
    n += 1
f.close()
#Шифруем/дешифруем и помещаем в новый список
cr = []
for w in txt:
    #print(w) #отладочная печать
    s = ""
    for b in w:
        s += chr(ord(b) + key)
    cr.append(s)
    #print(s) #отладочная печать
#Выгружаем в файл (к имени добавим "c_")
g = codecs.open("c_" + text, "w", "utf_8_sig")
for s in cr:
    g.write(s + "\n")
g.close()
print("ОПЕРАЦИЯ УСПЕШНО ЗАВЕРШЕНА")
print("Файл-результат:", "c_" + text)
"""
"""
# Игра в даты
import random
# Длительности месяцев (год не виокосный)
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Выигрышные даты
good = [[31, 12], [30, 11], [29, 10], [28, 9], [27, 8], [26, 7],
        [25, 6], [24, 5], [23, 4], [22, 3], [21, 2], [20, 1]]
good.sort() # и месяцы, и дни в good идут по возрастанию
# Генерируем стартовую дату и порядок ходов
m = random.randint(1, 11)
d = random.randint(1, days[m - 1])
if [d, m] in good:
    h = 1 # Ход пользователя
else:
    h = 0 # Ход компа

print("ИГРАЕМ В ДАТЫ")
print("?" * 30)
p = input("Показать правила? (да/нет): ")
if p == "да":
    print("Цель игры - получить дату 31.12")
    print("Начинают со случайной даты, ходят по очереди.")
    print("За один ход можно увеличить на любое число \nлибо номер дня, либо номер месяца.")
    print("Дата должна быть в пределах календаря.")
input("Готовы? Нажмите Enter.")

while not (d == 31 and m == 12):
    print("|" * 30)
    print("Текущая дата:", str(d) + "." + str(m))
    if h == 1: # принимаем ход пользователя
        print("== Ход пользователя ==")
        w = input("Что меняете - день (д) или месяц (м)? ")
        if w == "д":
            dd = int(input("Введите номер дня в месяце " + str(m) + ": "))
            if dd <= d or dd > days[m - 1]:
                print("Некорректная дата! Вы проиграли.")
                break
            else:
                d = dd
        else: # будем считать, что если не день - то месяц
            mm = int(input("Введите номер месяца: "))
            if mm <= m or mm > 12 or d > days[mm - 1]:
                print("Некорректная дата! Вы проиграли.")
                break
            else:
                m = mm
    else: # ход делает компьютер
        print("== Ход компьютера ==")
        tgood = good[m - 1][0] # удачный день в этом месяце
        if tgood > d:
            print ("Меняю день на", tgood)
            d = tgood
        else:
            print ("Меняю месяц на", d - 19)
            m = d - 19
    # Смена хода
    h = (h + 1) % 2
else: # сюда мы попадём, если условие цикла перестало выполняться
    print("Победил компьютер!")
    # Можно было из вежливости проверить, кто ходил последним...
    # Но не нужно. 
"""
"""
import random
import time
chrA, chrB, chrC = "A", "B", "C"
num_A = 0
num_B = 0
num_C = 0
seconds = 0
cherta = "=" * 31
print("Вас приветствует программа \"Тараканьи бега\"")
time.sleep(1)
print("На старт...")
time.sleep(1)
print("...Внимание...")
time.sleep(1)
print("...Марш!")
while num_A != 30 and num_B != 30 and num_C != 30:
    print("Секунд", seconds)
    print(cherta)
    num_A += random.randint(0, 1)
    print(" " * num_A + chrA)
    print(cherta)
    num_B += random.randint(0, 1)
    print(" " * num_B + chrB)
    print(cherta)
    num_C += random.randint(0, 1)
    print(" " * num_C + chrC)
    print(cherta)
    seconds += 1
    time.sleep(1)
else:
    fin = ""
    if num_A == 30:
        fin = chrA
    elif num_B == 30:
        fin = chrB
    else:
        fin = chrC
print("Финишировал", fin)
print("Время победителя", str(seconds) + "c.")
"""
"""
#Тараканьи бега 
import random as r #as в import позволяет использовать сокращённое название
import time as t
input("Вас приветствует программа \"Тараканьи бега\"")
print("На старт...")
t.sleep(1)
print("...Внимание...")
t.sleep(1)
print("...Марш!")
a = "A"
b = "B"
c = "C"
d = "============================================================"
s = 0
r.seed()
while len(a)<=60 and len(b)<=60 and len(c)<=60:
    print("Секунда " + str(s), d, a, d, b, d, c, d, sep = '\n')
    #каждый элемент выводится в отдельной строке, т.к. sep = '\n' 
    n = r.randint(0,2)
    a = " " * n + a
    n = r.randint(0,2)
    b = " " * n + b
    n = r.randint(0,2)
    c = " " * n + c
    s += 1
    t.sleep(1)
if len(a)> 60: print("Финишировал А")
if len(b)> 60: print("Финишировал B")
if len(c)> 60: print("Финишировал C")
print("Время победителя ", s, "сек")
"""

cherta = "#" * 44
array_groom = [["Евгений", 137], ["Денис", 243], ["Егор", 685], ["Вова", 399], ["Ваня", 356], ["Владимир", 965],
               ["Архип", 548], ["Вовчик", 123], ["Петр", 239], ["Ерёма", 856], ["Авдей", 973], ["Адам", 354],
               ["Али", 756], ["Артур", 827], ["Борис", 743], ["Виталий", 753], ["Гавриил", 641], ["Егор", 234]]


print(cherta)
print(" " * 12 + "РАЗБОРЧИВАЯ НЕВЕСТА")
print(cherta)
print("Итак, вы невеста (почему бы и нет?)\nСидите вы у окошка.")
print("А мимо проходят женихи  - 18 шт.\nПро каждого известно имя и показатель качества - число.")
print("Вы должны выбрать самого качественного.\nEnter - пропустить, Любое слово - выбрать")
input("Если готовы нажмите Enter: ")

for i in range(len(array_groom) - 1):


















