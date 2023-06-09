import math
def ngto(x):
    if(x < 2): return 0
    for i in range(2, int(math.sqrt(x) + 1)):    
        if(x % i == 0): return 0
    return 1
n = int(input())
a = [int(x) for x in input().split()]
dd = [0] * 1000002
for i in a:    dd[i] += 1
for i in a:
    if dd[i] > 0:
        if ngto(i):
            print(i, dd[i])
            dd[i] = 0
    
