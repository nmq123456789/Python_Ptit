import math
n = int(input())
a = sorted([int(x) for x in input().split()])
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if math.gcd(a[i], a[j]) == 1:
            print(a[i], a[j])