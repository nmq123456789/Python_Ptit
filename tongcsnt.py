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
    sum = 0
    for j in range(0, len(s)):
        sum += int(s[j])
    if ngto(sum) == 1: print("YES")
    else: print("NO")