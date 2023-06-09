import math
def ngto(x):
    if(x < 2): return 0
    for i in range(2, int(math.sqrt(x) + 1)):    
        if(x % i == 0): return 0
    return 1
t = int(input())
for i in range(t):
    s = input()
    ok = 0
    for i in range(0, len(s)):
        if(ngto(i) == 1):
            if(ngto(int(s[i])) == 0):
                ok = 1
        if(ngto(i) == 0):
            if(ngto(int(s[i])) == 1):
                ok = 1
    if(ok == 0): print("YES")
    else: print("NO")
        