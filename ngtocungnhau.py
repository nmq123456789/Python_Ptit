def ucln (a,b):
    if b == 0: return a
    return ucln(b, a % b)
x , y = [int(i) for i in input().split()]
d = 0
for i in range(10 ** (y - 1), 10 ** y):
    if(ucln(x, i) == 1): 
        d += 1
        print(i, end = " ")
    if(d !=0 and d % 10 == 0):
        d -= 10
        print()
