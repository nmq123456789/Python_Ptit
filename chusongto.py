import math
def ngto(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1
t = int(input())
for i in range(t):
    s = input()
    nt = 0
    knt = 0
    for i in range(0, len(s)):
        if ngto(int(s[i])) == 1: nt += 1
        else: knt += 1
    if ngto(len(s)) == 1 and nt > knt: print("YES")
    else: print("NO")

