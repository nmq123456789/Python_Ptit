t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    Max = max(a)
    Min = min(a)
    for i in range(Min, Max + 1):
        if not(i in a): ans += 1
    print(ans)