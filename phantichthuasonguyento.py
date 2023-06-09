import math
t = int(input())
for i in range(t):
    n = int(input())
    print(1, end = " ")
    print("* ", end = "")
    for i in range(2,int(math.sqrt(n)) + 1):
        if(n % i == 0):
            dem = 0
            while(n % i == 0):
                n /= i
                dem += 1
            print(i, end = "")
            print("^", end = "")
            print(dem, end = "")
            if n > 1: print(" * ",end = "")
    if n > 1:
        print(int(n), end = "^1")
        print() 
    else:
        print()       