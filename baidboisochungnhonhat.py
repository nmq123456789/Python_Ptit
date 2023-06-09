mod = 10e9 + 7
from math import sqrt

def tohop(n, k):
    if k == 0 or  k == n: return 1
    else: return tohop(n - 1, k) + tohop(n - 1, k - 1)

t = int(input())
for i in range(t):
    a, b = [int(x) for x in input().split()]
    
    sum, count = 1, 2
    for i in range(a, b + 1): sum = sum * i
    for i in range(a, int(sqrt(b)) + 1): 
        if sum % i == 0: 
            count += 1
    