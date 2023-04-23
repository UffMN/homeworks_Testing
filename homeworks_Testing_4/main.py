'''
n = int(input('кол-во элементов первого множества: '))
m = int(input('кол-во элементов второго множества: '))
listN = []
listM = []
for i in range (n):
    listN.append (int(input(f"Введите {i+1} значение: ")))
for i in range (m):
    listM.append (int(input(f"Введите {i+1} значение: ")))

print(listN, listM)

result=list(set(listN) & set(listM))
result.sort()
print(result)
'''

n = int(input())
arr = list()
for i in range (n):
    x = int(input())
    arr.append(x)

arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i-1] + arr[i] + arr[i+1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count))