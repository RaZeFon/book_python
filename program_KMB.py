"""
arrey_fastening = ["Болт", "Гровер", "Ось", "Крючёк", "Шайба", "Шплинт"]

print(arrey_fastening)
print(""Введите нужный элемент из списка выше,
или 0 что-бы выйти из программы"")
name_fastening_search = ""
while name_fastening_search.lower() != "0":
    name_fastening_search = input(">>> ")
"""

print("Для того чтобы найти интересующий вас БОЛТ, ШПИЛЬКУ\n")
print("пример: 'Болт 10х60 >>> b10x60' или 'Шпилька 00 мм >>> ch00'")
arrey_fastening = [["Болт 10х60", "b10x60", "A001"], ["Болт 12х50", "b12x50", "A002"],
                    ["Болт 6х55", "b6x55", "A003"]]

name_fastening_search = ""
while name_fastening_search.lower() != "0":
    name_fastening_search = input(">>> ")
    if name_fastening_search == "1":
        print("Полный список крепежа:")
        for i in range(len(arrey_fastening)):
            print(arrey_fastening[i][0])








