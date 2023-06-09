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
    m = n
    ok = 0
    sum = 0
    while(n > 0):
        x = n % 10
        sum += x
        if(nto(x) == 0):
            ok = 1
            break
        n = int(n / 10)
    if ok == 0 and nto(m) == 1 and nto(int(str(m)[::-1])) == 1 and nto(sum) == 1 : print("Yes")
    else: print("No")

    