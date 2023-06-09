import math
def ngto(x):
    if(x < 2): return 0
    for i in range(2, int(math.sqrt(x) + 1)):    
        if(x % i == 0): return 0
    return 1
t = int(input())
for i in range(t):
    s = input()
    sum = 0
    ok = 0
    for i in range(0, len(s)):
        sum += int(s[i])
        if(i % 2 == 0):
            if(int(s[i]) % 2 == 1):
                ok = 1
        if(i % 2 == 1):
            if(int(s[i]) % 2 == 0):
                ok = 1
    if ngto(sum) == 1 and ok == 0:
        print("YES")
    else:
        print("NO")