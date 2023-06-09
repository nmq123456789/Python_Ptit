b = [0, 0 , 0, 0]
while 1:
    ans = 0
    a = [int(x) for x in input().split()]
    if a == b: break
    while a[0] != a[1] or a[0]  != a[2] or a[0] != a[3]:
        x = a[0]
        for i in range(0,3):
            a[i] = abs(a[i] - a[i + 1])
        a[3] = abs(a[3] - x)
        ans += 1
    print(ans)
