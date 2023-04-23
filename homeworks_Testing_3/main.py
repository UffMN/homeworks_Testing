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



# test = 1
# count = {'1': 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т', '2': 'D, G, Д, К, Л, М, П, У', '3': 'B, C, M, P, Б, Г, Ё, Ь, Я', '4': 'F, H, V, W, Y, Й, Ы', '5': 'K, Ж, З, Х, Ц, Ч', '8': 'J, X, Ш, Э, Ю', '10': 'Q, Z, Ф, Щ, Ъ'}
# list = input("Введите слово: ")
# for i in range (len(count['1'])):
#     for j in range (len(list)):

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