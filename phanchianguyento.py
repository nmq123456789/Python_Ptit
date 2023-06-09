import math
def nto(n) :
    if n < 2 : return 0
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return 0
    return 1
n = int(input())
a = [int(x) for x in input().split()]
b = {}
for i in a: b[i] = 1
a = list(b)
for i in range(1, len(a)): a[i] = a[i] + a[i - 1]
ok = 0
for i in range(0, len(a)):
    if(nto(a[i]) and nto(a[len(a) - 1] - a[i])):
        ok = 1
        print(i)
        break
if ok == 0: print("NOT FOUND")
