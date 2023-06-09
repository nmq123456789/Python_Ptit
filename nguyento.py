import math
def ucln(x, y):
    if(y == 0): return x
    return ucln(y, x % y)

def ngto(x):
    if(x < 2): return 0
    for i in range(2, int(math.sqrt(x) + 1)):    
        if(x % i == 0): return 0
    return 1

t = int(input())
while(t > 0):
    x = int(input())
    cnt = int(0)
    for i in range(1, x):
        if(ucln(x, i) == 1) : cnt = cnt + 1
    if(ngto(cnt)): 
        print("YES")
    else: 
        print("NO")
    t = t - 1

