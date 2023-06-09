import math
def nto(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1
t = int(input())
for i in range(t):
    n = int(input())
    for i in range(10, n):
        if nto(i) == 1 and nto(int(str(i)[::-1])) == 1 and str(i) !=  str(i)[::-1] and int(str(i)[::-1]) < n and i < int(str(i)[::-1]):
            print(i, str(i)[::-1], end = " ")
    print()
