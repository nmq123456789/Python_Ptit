import csv

def tinh(lst, dk):
    if dk == 'sum': return sum(lst)
    if dk == 'avg': return format(sum(lst) / len(lst), ".2f")
    if dk == 'max': return max(lst)
    if dk == 'min': return min(lst)

a = []
with open ('iris.csv') as file:
    data = [csv.reader(file)]
    # a = [x for x in data]

t = int(input())
for i in range(t):
    # ten, chieudai, yeucau = [x for x in input().split()]
    ten = input()
    sepal_length, sepal_width, petal_length, petal_width, kt = [], [], [], [], 0
    for i in a[1:]:
        if ten == i[4]:
            kt = 1
            sepal_length.append(float(i[0]))
            sepal_width.append(float(i[1]))
            petal_length.append(float(i[2]))
            petal_width.append(float(i[3]))
    if kt == 0: print('Invalid')
    else:
        chieudai = input()
        yeucau = input()
        if chieudai == 'sepal_length': print(tinh(sepal_length, yeucau))
        if chieudai == 'sepal_width': print(tinh(sepal_width, yeucau))
        if chieudai == 'petal_length': print(tinh(petal_length, yeucau))
        if chieudai == 'petal_width': print(tinh(petal_width, yeucau))
        