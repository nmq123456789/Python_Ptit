import math
t = int(input())
for i in range(t):
    N, X, M = [float(x) for x in input().split()]
    ans = math.log(M / N, 1 + (X / 100))
    if ans != int(ans) : ans += 1
    print(int(ans))