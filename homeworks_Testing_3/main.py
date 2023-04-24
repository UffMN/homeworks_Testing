# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3
# -> 2

"""
import random
list = []
n = int(input("Введите количество чисел: "))
count = 0
for i in range (n):
    list.append(random.randint(0, 9))
print(list)

x = int(input("Введите число которое необходимо посчитать: "))

for i in range (n):
    if list[i] == x: count+=1
print(f"Количество чисел {x} в списке {count}")
"""

# Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
# -> 9

"""
import random
list = []
n = int(input("Введите количество чисел: "))

for i in range (n):
    list.append(random.randint(0, 9))
print(list)

x = int(input("Введите число которое необходимо посчитать: "))
for i in range (n):
    if list[i] <= x:
        max = list[i]
        break
print(max)
for i in range (n):
    if list[i] <= x and list[i] >= max: max = list[i]
print(max)
"""



# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские,
# либо только русские буквы.


# Решение через словарь
"""
scrabble = {'1': 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т', '2': 'D, G, Д, К, Л, М, П, У', '3': 'B, C, M, P, Б, Г, Ё, Ь, Я', '4': 'F, H, V, W, Y, Й, Ы', '5': 'K, Ж, З, Х, Ц, Ч', '8': 'J, X, Ш, Э, Ю', '10': 'Q, Z, Ф, Щ, Ъ'}
count = [*scrabble]
list = input("Введите слово: ").upper()
sum = 0

for i in range (len(list)):
    for j in range (len(scrabble[count[0]])):
        if (scrabble[count[0]])[j] == list[i]: sum += int(count[0])
    for j in range (len(scrabble[count[1]])):
        if (scrabble[count[1]])[j] == list[i]: sum += int(count[1])
    for j in range (len(scrabble[count[2]])):
        if (scrabble[count[2]])[j] == list[i]: sum += int(count[2])
    for j in range (len(scrabble[count[3]])):
        if (scrabble[count[3]])[j] == list[i]: sum += int(count[3])
    for j in range (len(scrabble[count[4]])):
        if (scrabble[count[4]])[j] == list[i]: sum += int(count[4])
    for j in range (len(scrabble[count[5]])):
        if (scrabble[count[5]])[j] == list[i]: sum += int(count[5])
    for j in range (len(scrabble[count[6]])):
        if (scrabble[count[6]])[j] == list[i]: sum += int(count[6])
print(sum)
"""

# Решение через списки
"""
list1 = 'AEIOULNSTRАВЕИНОРСТ'
list2 = 'DGДКЛМПУ'
list3 = 'BCMPБГЁЬЯ'
list4 = 'FHVWYЙЫ'
list5 = 'KЖЗХЦЧ'
list8 = 'JXШЭЮ'
list10 = 'QZФЩЪ'

sum = 0
list = input("Введите слово: ").upper()
for i in range (len(list)):
    for j in range (len(list1)):
        if list1[j] == list[i]: sum +=1
    for j in range (len(list2)):
        if list2[j] == list[i]: sum +=2
    for j in range (len(list3)):
        if list3[j] == list[i]: sum +=3
    for j in range (len(list4)):
        if list4[j] == list[i]: sum +=4
    for j in range (len(list5)):
        if list5[j] == list[i]: sum +=5
    for j in range (len(list8)):
        if list8[j] == list[i]: sum +=8
    for j in range (len(list10)):
        if list10[j] == list[i]: sum +=10
print(sum)
"""

dictionaryScrabble = {1: 'AEIOULNSTRАВЕИНОРСТ', # dictionary = {Key : Value}
            2: 'DGДКЛМПУ',
            3: 'BCMPБГЁЬЯ',
            4: 'FHVWYЙЫ',
            5: 'KЖЗХЦЧ',
            8: 'JXШЭЮ',
            10: 'QZФЩЪ'}
word = input("Введите слово: ").upper()

# input() -> qwerty
# key: 1, 2, 3, 4, 5, 8, 10
# value: AEIOULNSTRАВЕИНОРСТ, DGДКЛМПУ, ..., etc
# letter Q, W, E, R, T, Y from input
print(sum([key for letter in word for key, value in dictionaryScrabble.items() if letter in value]))