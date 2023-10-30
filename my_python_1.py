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







