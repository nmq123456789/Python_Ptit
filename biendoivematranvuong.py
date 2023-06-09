n, m = [int(x) for x in input().split()]
a = [[]] * n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
if n == m:
    for i in range(n):
        print(*a[i], sep = ' ', end = "\n")
if n > m:
    dd = n
    for i in range(n):
        if i % 2 == 0 and dd != m:
            dd -= 1
            continue
        for j in range(m):
            print(a[i][j], end = " ")
        print()
if n < m:
    for i in range(n):
        dd = m
        for j in range(m):
            if j % 2 == 1 and dd != n: 
                dd -= 1
                continue
            print(a[i][j], end = " ")
        print()