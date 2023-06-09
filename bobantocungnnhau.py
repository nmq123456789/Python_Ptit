from math import gcd

x, y = [int(i) for i in input().split()]
for i in range(x, y + 1):
    for j in range(i + 1, y + 1):
        if(gcd(i, j) == 1):
            for k in range(j + 1, y + 1):
                if(gcd(i, k) == 1 and gcd(j, k) == 1):
                    print("(%d, %d, %d)" % (i, j, k))
                    