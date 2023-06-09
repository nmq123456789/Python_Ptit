t = int(input())
for i in range(t):
    n = int(input())
    dd = [0] * 1001
    max = 0
    ans = 0
    for i in range(n):
        dd[int(input())] += 1
    for i in range(1, 1001):
        if dd[i] > max:
            max = dd[i]
            ans = i
    print(ans)
    