from math import sqrt

def demuoc(n):
    ans = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ans += 1
            k = int(n / i)
            if k != sqrt(n) and n % k == 0: ans += 1
    return ans
t = int(input())
for i in range(t):
    n = int(input())
    print(demuoc(n))