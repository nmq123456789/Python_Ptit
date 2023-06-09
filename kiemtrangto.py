import math
def ngto(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1
n, m = [int(x) for x in input().split()]
a =[[]] * n * m
for i in range(n):
    a[i] = [int(x) for x in input().split()]
for i in range(n):
    for j in range(m):
        if ngto(a[i][j]) == 1: a[i][j] = 1
        else: a[i][j] = 0
for i in range(n):
    for j in range(m):
        print(a[i][j], end = " ")
    print()

