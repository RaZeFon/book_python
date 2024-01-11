"""
print("Привет, мир")
"""
"""
print(8 * 3.57)
"""
"""
print(10 * 365), print(3650 + 20)
"""
"""
print(3 * 52), print(3670 - 156)
"""
"""
print(5 + 30 * 20), print((5 + 30) * 20)
"""
"""
print(((5 +30) * 20) / 10), print(5 + 30 * 20 / 10)
"""
"""
fred = 100
print(fred)
fred = 200
print(fred)
"""
"""
fred = 200
john = fred
print(john)
"""
"""
number_of_coins = 200
print(number_of_coins)
"""
"""
print(20 + 10 * 365)
print(3 * 52)
print(3670 - 156)

print(20 + 10 * 365 - 3 * 52)
"""
"""
found_coins = 20
magic_coins = 10
stolen_coins = 3
print(found_coins + magic_coins * 365 - stolen_coins * 52)

stolen_coins = 2
print(found_coins + magic_coins * 365 - stolen_coins * 52)

magic_coins = 13
print(found_coins + magic_coins * 365 - stolen_coins * 52)
"""
"""
fred = "Почему у горил большие ноздри? Потому что у горил толстые пальцы!"
print(fred)
fred = "Что это розовое пушистое? Розовый пушистик!"
print(fred)
fred = '''Это едят на полдник динозавры?
ТиРекс-кекс!'''
print(fred)
"""
"""
silly_string = '"Здесь что-то не так, не будь я д\'Артаньян" - подумал он.'
print(silly_string)
silly_string = "\"Здесь что-то не так, не будь я д'Артаньян\" - подумал он."
print(silly_string)
silly_string = '''"Здесь что-то не так, не будь я д'Артаньян" - подумал он.'''
print(silly_string)
"""
"""
myscore = 1000
message = 'Мой счет: %s очков'
print(message % myscore)
"""
"""
joke_text = "%s: приспособление для поиста мебели в темноте"
bodypart1 = 'Коленка'
bodypart2 = 'Лодышка'
print(joke_text % bodypart1)
print(joke_text % bodypart2)
"""
"""
nums = "Что сказало число %s числу %s? Славный поясок!"
print(nums % (0, 8))
"""
"""
print(10 * "a")
"""
"""
spaces = " " * 25
print("%s Задний переулок 12" % spaces)
print("%s Трясогузочья пустошь" % spaces)
print("%s Западный скрапшир" % spaces)
print()
print()
print("уважаемый Сэр,")
print()
print('Хочу сообщитьвам, что кое-где на крыше уборной')
print("недостает кусочков черепицы.")
print("Думаю прошлой ночью их сдуло внезапным порывом ветра.")
print()
print("С почтением")
print("Мальком Конфузли")
"""
"""
print(1000 * "слякоть")
"""
"""
wizard_list = "паучьи лапки, жабий палец, глаз тритона, крыло летучий мыши, жир слизня, перхоть змей"
print(wizard_list)

wizard_list = ["паучьи лапки", "жабий палец", "глаз тритона", "крыло летучий мыши", "жир слизня", "перхоть змей"]
print(wizard_list)
print(wizard_list[2])

wizard_list[2] = "язык улитки"
print(wizard_list)

print(wizard_list[2:5])
"""
"""
some_numbers = [1, 2, 5, 10, 20]
print(some_numbers)
some_strings = ["нож", "отточен", "тожен", "очень"]
print(some_strings)
numbers_and_strings = [7, "раз", "отпей", 1, "раз", "отешь"]
print(numbers_and_strings)
"""
"""
numbers = [1, 2, 3, 4, 5]
strings = ["хватит", "циферки", "считать"]
mylist = [numbers, strings]
print(mylist)
"""
"""
wizard_list = ["паучьи лапки", "жабий палец", "глаз тритона", "крыло летучий мыши", "жир слизня", "перхоть змей"]
wizard_list.append("медвежий коготь")
print(wizard_list)

wizard_list.append("мандрагора")
wizard_list.append("болиголов")
wizard_list.append("болотный глаз")
print(wizard_list)

del wizard_list[5]
print(wizard_list)

del wizard_list[8]
del wizard_list[7]
del wizard_list[6]
print(wizard_list)
"""
"""
list1 = [1, 2, 3, 4, 5]
list2 = ["я", "забрался", "под", "кровать"]
print(list1 + list2)
"""
"""
list1 = [1, 2, 3, 4]
list2 = ["я", "мечтаю", "о", "пломбире"]
list3 = list1 + list2
print(list3)
"""
"""
fibs = (0, 1, 1, 2, 3)
print(fibs[3])
"""
"""
favorite_sports = ["Ральф Уильямс, Футбол",
                   "Майкл Типпетт, Баскетбол",
                   "Эдвард Элгар, Бейсбол",
                   "Ребека Кларк, Нетбол",
                   "Этель Смит, Банбинтон",
                   "Френк Бридж, Регби"]
print(favorite_sports)
"""
"""
favorite_sports = {'Ральф Уильямс': 'Футбол',
                   'Майкл Типпетт': 'Баскетбол',
                   'Эдвард Элгар': 'Бейсбол',
                   'Ребека Кларк': 'Нетбол',
                   'Этель Смит': 'Банбинтон',
                   'Френк Бридж': 'Регби'}
print(favorite_sports['Ребека Кларк'])

del favorite_sports['Этель Смит']
print(favorite_sports)

favorite_sports['Ральф Уильямс'] = 'Хокей на льду'
print(favorite_sports)
"""
"""
#1 Любимые вещи
games = ["программирование", "компьюторные игры", "чтение книг"]
foods = ["халва", "мороженое", "шаурма", "молоко", "колбаса"]
favorites = games + foods
print(favorites)
"""
"""
#2 Подсчет войнов
house = 3
tunnel = 2
ninja = 25
samurai = 40
wars = (house * ninja) + (tunnel * samurai)
print("Войнов: %s" % wars)
"""
"""
name = "Евгений"
surname = "Голиченков"
text = 'Привет, %s %s!'
print(text % (name, surname))
"""
"""
import turtle
t = turtle.Pen()
t.forward(50) #сдвинуться в перед на 50 пикселей
t.left(90) #повернуть на 90 градусов в лево
t.forward(50) 
t.left(90)
t.forward(50) 
t.left(90)
t.forward(50) 
t.left(90)
#нарисовали квадрат

t.reset()
t.clear()

t.reset()
t.backward(100)
t.up()
t.right(90)
t.forward(20)
t.left(90)
t.down()
t.forward(100)
"""
"""
# Прямоугольник
import turtle
cursor = turtle.Pen()
#cursor.reset() #Если нужно очистить холст
cursor.forward(100)
cursor.right(90)
cursor.forward(40)
cursor.right(90)
cursor.forward(100)
cursor.right(90)
cursor.forward(40)
cursor.right(90)
"""
"""
#Треугольник
import turtle
cursor = turtle.Pen()
#cursor.reset() #Если нужно очистить холст
cursor.left(60)
cursor.forward(100)
cursor.right(120)
cursor.forward(100)
cursor.right(120)
cursor.forward(100)
"""
"""
#Рамка квадрата без углов
import turtle
cursor = turtle.Pen()
#cursor.reset() #Если нужно очистить холст
cursor.forward(100)
cursor.up()
cursor.forward(20)
cursor.right(90)
cursor.forward(20)
cursor.down()
cursor.forward(100)
cursor.up()
cursor.forward(20)
cursor.right(90)
cursor.forward(20)
cursor.down()
cursor.forward(100)
cursor.up()
cursor.forward(20)
cursor.right(90)
cursor.forward(20)
cursor.down()
cursor.forward(100)
"""
"""
age = 25 
if age > 20:
    print("Как-то вы староваты!")
    print("Что вы здесь делаете?")
    print("Почему не стрижете газон или не перекладываете бумажки?")
"""
"""
age = 10
if age >= 10:
    print("Вы слишком стары для моих шуток!")
"""
"""
age = 10
if age == 10:
    print("Что нельзя съесть на завтрак? Обед и ужин!")
"""
"""
print("Хотите услышить грязную шутку?")
age = 12 
if age == 12:
    print("Свинья шлёпнулась в грязь!")
else:
    print("Тсс! Это секрет.")
"""
"""
print("Хотите услышить грязную шутку?")
age = 8 
if age == 12:
    print("Свинья шлёпнулась в грязь!")
else:
    print("Тсс! Это секрет.")
"""
"""
age = 12
if age == 10:
    print("Что будет если клюква наденит штаны?")
    print("Брюква")
elif age == 11:
    print("Что сказала зелёная виноградена синей виноградине?")
    print("Дыши! Дыши!")
elif age == 12:
    print("Что сказало чило 0 числу 8?")
    print("Привет, ребята!")
elif age == 13:
    print("Что такое: на полочке сидит и хохочет?")
    print("Муха-хохотуха!")
else:
    print("Что-что?")
"""
"""
age = 10
if age == 10 or age == 11 or age == 12 or age == 13:
    print("13 + 49 + 155 + 97: что получиться? Головная боль!")
else:
    print("Что-что?")
"""
"""
age = 10
if age >= 10 and age <= 13:
    print("13 + 49 + 155 + 97: что получиться? Головная боль!")
else:
    print("Что-что?")
"""
"""
myval = None
if myval == None:
    print("В переменой myval ничего нет!")
"""
'''
age = 10
if age == 10:
    print("Как лучше всего общаться с монстром?")
    print("Издалека!")
'''
"""
age = "10"
converted_age = int(age)
print(converted_age, type(converted_age))

age = 10
converted_age = str(age)
print(converted_age, type(converted_age))
"""
"""
age = '10'
converted_age = int(age)
if converted_age == 10:
    print("Как лучше всего общаться с монстром?")
    print("Издалека!")
"""
"""
age = "10.5"
converted_age = float(age)
print(converted_age)
print(int(converted_age))
"""
"""
#1 Вы богаты?
money = 2000
if money > 1000:
    print("Я богат!")
else:
    print("Я не богат!")
    print("Может, когда-нибудь потом...")
"""
"""
#2 Бисквитики!
twinkies = 540
if twinkies < 100 or twinkies > 500:
    print("Слишком мало или слишком много")
"""
"""
#3 Подходящая сумма
money = 103
if (money >= 100 and money <= 500) or (money >= 1000 and money <= 5000):
    print("Сумма %s соответствует заданному диапозону." % money)
"""
"""
#4 Я одолею этих нинзя!
ninjas = 45
if ninjas < 10:
    print("Я одолею этих нинзя!")
elif ninjas < 30:
    print("Будет непросто, но я сними разделаюсь.")
elif ninjas < 50:
    print("Их слишком много!")
else:
    print("Это самоубийство!")
"""
"""
print("Привет!")
print("Привет!")
print("Привет!")
print("Привет!")
print("Привет!")
"""
"""
for x in range(0, 5):
    print("Привет!")
"""
"""
for x in range(0, 5):
    print("Привет №%s" % (x + 1))
"""
"""
x = 0
print("Привет №%s" % (x + 1))
x = 1
print("Привет №%s" % (x + 1))
x = 2
print("Привет №%s" % (x + 1))
x = 3
print("Привет №%s" % (x + 1))
x = 4
print("Привет №%s" % (x + 1))
"""
"""
wizard_list = ['паучьи лапки', 'жабий палец', 'язык улитки',
               'крыло летучей мыши', 'жир слизня', 'медвежий коготь']
for x in wizard_list:
    print(x)
"""
"""
wizard_list = ['паучьи лапки', 'жабий палец', 'язык улитки',
               'крыло летучей мыши', 'жир слизня', 'медвежий коготь']
print(wizard_list[0])
print(wizard_list[1])
print(wizard_list[2])
print(wizard_list[3])
print(wizard_list[4])
print(wizard_list[5])
"""
"""
hugehairypants = ['огромные', 'волосатые', 'штаны']
for i in hugehairypants:
    print(i)
    print(i)
"""
"""
hugehairypants = ['огромные', 'волосатые', 'штаны']
for i in hugehairypants:
    print(i)
    for j in hugehairypants:
        print(j)
"""
"""
magic_coins = 10
found_coins = 20
stolen_coins = 3
for i in range(0, 52):
    for j in range(0, 7):
        found_coins += magic_coins
    found_coins -= stolen_coins
    print("%s Неделя денег получино: %s" % (i+1, found_coins))
"""
"""
found_coins = 20
magic_coins = 70
stolen_coins = 3
coint = found_coins
for week in range(1, 53):
    coint = coint + magic_coins - stolen_coins
    print('Неделя %s = %s' % (week, coint))
"""
"""
for step in range(0, 20):
    print(step)
"""
"""
tired = 0
badweathet = 0
step = 0
while step < 10000:
    print(step)
    if tired == True:
        break
    elif badweathet == True:
        break
    else:
        step = step + 1
"""
"""
x = 45
y = 80
while x < 50 and y < 100:
    x = x + 1
    y = y + 1
    print(x, y)
"""
"""
some_value = 0
while True:
    #текст кода
    #текст кода
    #текст кода
    if some_value == True:
        break
"""
"""
# 1. Цикл с приветом
for x in range(0, 20):
    print("Привет %s" % x)
    if x > 9:
        break
"""
'''
# 2. Четные числа
age = 35
for i in range(1, age + 1):
    if age % 2 != 0:
        print(i)
'''
"""
# 3. Пять любимых ингридиентов
ingredients = ['слизни', 'пиявки', 'катышки из пупка гориллы',
               'бровки гусеницы', 'пальци многоножки']
num = 1
for i in ingredients:
    print(f"{num}: {i}")
    num += 1

ingredients = ['слизни', 'пиявки', 'катышки из пупка гориллы',
               'бровки гусеницы', 'пальци многоножки']
num = 1
for i in ingredients:
    print(str(num) + ": %s" % i)
    num += 1
"""
"""
# 4. Ваш лунный вес
weight = 61
for i in range(0, 15 + 1):
    moon_weight = (weight + i) * 0.165
    print(i+1, "год", moon_weight, "вес")
"""
'''
a = list(range(0, 5))
print(a)

b = list(range(0, 1000))
print(b)
'''
'''
def testfunc(myname):
    print("Привет %s" % myname)
testfunc("Евгений")
'''
'''
def testfunc(fname, lname):
    print("Привет, %s %s" % (fname, lname))
testfunc("Мери", "Смит")

firstname = "Джо"
lastname = "Робетсон"
testfunc(firstname, lastname)
'''
'''
def savings(pocket_money, paper_rounte, spending):
    return pocket_money + paper_rounte - spending
print(savings(10, 15, 5))
'''
'''
def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable
print(variable_test())
'''
'''
another_variable = 100
def variable_test2():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable * another_variable
print(variable_test2())
'''
'''
def spaceship_building(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print('Неделя %s, банок: %s' % (week, total_cans))

spaceship_building(2)
'''
'''
import time
print(time.asctime())
'''
'''
import sys
print(sys.stdin.readline())
'''
'''
age = 9
if age >= 10 and age <= 13:
    print('13 + 49 + 84 + 155 + 97: что получится? Головная боль!')
else:
    print('Что-что?')

def silly_age_joke(age):
    if age >= 10 and age <= 13:
        print('13 + 49 + 84 + 155 + 97: что получиться? Головная боль!')
    else:
        print('Что-что?')

silly_age_joke(12)
'''
'''
import sys
def silly_age_joke():
    print('Сколько вам лет?')
    age = int(sys.stdin.readline())
    if age >= 10 and age <= 13:
        print('13 + 49 + 84 + 155 + 97: что получится? Головная боль!')
    else:
        print('Что-что?')
silly_age_joke()
'''







































