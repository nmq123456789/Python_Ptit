t = int(input())
for test in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    cnt  = max(a)
    am = []
    duong = []
    for i in range(n):
        if a[i] == cnt:
            a.insert(i, k)
            break
    for i in a:
        if i < 0: am.append(i)
        else: duong.append(i)
    for i in am: print(i, end = " ")
    for i in duong: print(i, end = " ")
    print()

