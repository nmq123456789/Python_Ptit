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
    ans = 0
    for i in range(5, n - 6):
        if nto(i) and nto(i + 6): 
            if(nto(i + 2) or nto(i + 4)):
                ans += 1
    print(ans)
