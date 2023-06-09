t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    dd = [0] * 1000001
    max = 0
    ans = 0
    for i in a:
        dd[i] += 1
    for i in a:
        if dd[i] > max:
            max = dd[i]
            ans = i
    if dd[ans] > int(n / 2): print(ans)
    else: print("NO")
    