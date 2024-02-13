'''  1
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

summa = 0
for i in range(1, 1000 + 1):
    if i % 3 == 0 or i % 5 == 0:
        summa += i
print(summa)
'''

'''  2
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

term1 = 1
term2 = 1
summa = 0
general_sum = 0
while True:
    if term1 + term2 >= 4000000:
        break
    summa = term1 + term2
    if summa % 2 == 0:
        general_sum += summa
    term1 = term2
    term2 = summa
print(summa)
print(general_sum)
'''

"""  3
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?

def Max_Divider(div):
    '''Самый большой делитель'''
    max_divider = 0
    dividend = div
    divider = 1
    for i in range(divider, dividend + 1):
        if dividend % i == 0:
            dividend = dividend / i
            if max_divider < i:
                max_divider = i
                #print(f'''отладочная петчать {max_divider} {dividend}''') 
        if dividend == 1:
                break
    print(max_divider)

Max_Divider(600851475143)
"""
"""  4
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, 
полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

def Palington(str_num):
    size = len(str_num)
    for i in range(0, size):
        print(f"{str_num[i]} сравниваем с {str_num[size-1]}")
        # Отладочная проверка одинаковых значений
        if str_num[i] != str_num[size-1]:
            print("Не палингтон")
            break
        size -= 1
        if i == size-1 or i > size-1:
            print("Палингтон")
            break
 
while True:
    number1 = int(input("Введите первый множитель: "))
    number2 = int(input("Введите второй множитель: "))
    if number1 // 100 != 0 and number2 // 100 != 0:
        if number1 // 100 < 10 and number2 // 100 < 10:
            str_number = str(number1 * number2)
            print(str_number) #отладочная печать
            Palington(str_number)
"""
"""
def Cratnoe(num1, num2):
    count_numbers = num2
    power = True
    while power:
        for i in range(num1, num2 + 1):
            if count_numbers % i != 0:
                count_numbers += 1
                break
            if i == num2:
                print(f"Число {count_numbers} кратно от {num1} до {num2}")
                power = False
                break
            
 
number1 = int(input("Первый делитель: "))
number2 = int(input("Второй делитель: "))
if number1 > number2:
    number_max = number1
    number1 = number2
    number2 = number_max
 
Cratnoe(number1, number2)
"""
"""
def SumCub(num1, num2):
    sum_cub = 0
    for i in range(num1, num2 + 1):
        sum_cub += (i ** 2)
    #print(sum_cub)
    return sum_cub
 
def CubSum(num1, num2):
    cub_sum = 0
    for j in range(num1, num2 + 1):
        cub_sum += j
    cub_sum = cub_sum ** 2
    #print(cub_sum)
    return cub_sum
 
number_start = int(input("Начало интервала: "))
number_end = int(input("Конец интервала: "))
if number_start > number_end: 
    max_number = number_start
    number_start = number_end
    number_end = max_number
 
sum_cub1 = SumCub(number_start, number_end)
cub_sum2 = CubSum(number_start, number_end)
result = abs(sum_cub1 - cub_sum2)
print(f"Разность суммы {result}")
"""
'''
str_number = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
max_value = 0
sequence = int(input("Длина последовательности: "))
for i in range(0, len(str_number), sequence):
    value = ""
    for j in range(i, i + sequence):
        value = value + str_number[j]
        if max_value < int(value):
            max_value = int(value)
print(f"Максимальное значение {max_value}, из последовательности {sequence}")
'''
'''
start_number = 2
end_number = 2000000
sum_result = 0
 
if start_number == 2:
   sum_result += start_number
for num in range(start_number + 1, end_number + 1):
   for i in range(start_number, num):
       if num % i != 0:
           sum_result += num
           break
print(f"Сумма простых чисел {sum_result}")
'''
"""
result_num = 1000
number_A = int(input("Введите число А: "))
number_B = int(input("Введите число В: "))

def Pythagoras(num_A, num_B):
    result = (num_A ** 2) + (num_B ** 2)
    print(f"A(квадрат) = {num_A ** 2} + В(квадрат) = {num_B ** 2} => С = {result}")

def ThreePythagoras(result):
    print("Поиск А, В, С в (квадрате) при результате равном 1000")
    num_A = 2
    num_B = 2
    num_C = 2
    result_cude = 0
    power = True

    while power:
        for num_B in range(num_A):
            for num_C in range(num_A):
                result_cude = num_A ** 2 + num_B ** 2 + num_C ** 2
                if result == result_cude:
                    print(f"A = {num_A}; B = {num_B}; C = {num_C} (крадрат)")
                    power = False
        num_A += 1

Pythagoras(number_A, number_B)
ThreePythagoras(result_num)
"""



















