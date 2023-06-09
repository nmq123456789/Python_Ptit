import csv

a = []
with open ('iris.csv') as file:
    data = csv.reader(file)
    a = [x for x in data]

t = int(input())
for i in range(t):
    ten, canh = [x for x in input().split()]
    tong = []
    for i in a[1:]:
        if ten == i[4] and canh == i[2]:
            tong.append(float(i[0]))
    if len(tong) == 0: print('Invalid')
    else:
        print('{:.4f}'.format(min(tong) / len(tong)))