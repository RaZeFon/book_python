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



























