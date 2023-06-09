def ucln (a,b):
    if b == 0: return a
    return ucln(b, a % b)
t = int(input())
for i in range(t):
    n = input()
    x = int(n)
    y = int(n[::-1])
    # print(x, y)
    if(ucln(x, y) == 1): print("YES")
    else: print("NO")

