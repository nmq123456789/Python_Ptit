import math
def ngto(n):
    if n < 2: return 0
    for i  in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return 0
    return 1
t = int(input())
for i in range(t):
    s = input()
    dau = s[0 : 3]
    cuoi = s[len(s) - 3 : len(s)]
    if(ngto(int(dau)) == 1 and ngto(int(cuoi)) == 1):
        print("YES")
    else:
        print("NO")