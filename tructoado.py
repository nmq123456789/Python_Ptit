t = int(input())
for i in range(t):
    n = int(input())
    a = [[]] * (n + 1)
    for i in range(n):
        m, n = [int(x) for x in input().split()]
        a[i].append(m)
        a[i].append(n)
    for i in range(n):
        for j in range(2):
            print(a[i][j])