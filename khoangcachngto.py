import math
def nt(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return 0
    return 1
n, x = [int(x) for x in input().split()]
nto = []
d = 2
while len(nto) < n:
    if nt(d): nto = nto + [d]
    d += 1
print(x, end = " ")
for i in nto:
    x = x + i
    print(x, end = " ")
print()