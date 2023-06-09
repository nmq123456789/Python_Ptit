t = int(input())
for i in range(t):
    x, y, z = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    cnt = []
    ok = 0
    i = 0
    j = 0
    h = 0
    while i < x and j < y and h < z:
        if a[i] == b[j] and b[j] == c[h]:
            cnt.append(a[i])
            i += 1
            j += 1
            h += 1
        elif a[i] < b[j]: i += 1
        elif b[j] < c[h]: j += 1
        else: h += 1
    if len(cnt) == 0: print("NO")
    else:
        for i in cnt: print(i, end = " ")
        print()