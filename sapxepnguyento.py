import math
def nt(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return 0
    return 1
n = int(input())
a = [int(x) for x in input().split()]
b = []
for i in a:
    if nt(i): b.append(i)
b = sorted(b)
cnt = 0
for i in a:
    if nt(i):
        print(b[cnt], end = " ")
        cnt += 1
    else:
        print(i, end = " ")