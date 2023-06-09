import math
def ucln(a, b):
    if b == 0: return a
    return ucln(b, a % b)

def nto(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0: return 0
    return 1

t = int(input())    
while(t > 0):
    a, b = [int(x) for x in input().split()]
    sum = 0
    c = ucln(a ,b)
    while(c > 0):
        sum += c % 10
        c = int(c / 10)
    print("YES") if nto(sum) else print("NO")
    t = t - 1