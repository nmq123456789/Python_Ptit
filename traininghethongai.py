test = int(input())
for t in range(test):
    p = 1
    n, u = int(input()), float(input())
    a = [float(x) for x in input().split()]
    a.sort()
    for i in range(1, n):
        k = min(a[i] - a[i - 1], u / i)
        u -= k * i
        for j in range(0, i):
            a[j] += k
    if u > 0:    u /= n 
    for i in range(n):
        a[i] += u 
        p *= a[i]
    print("{:.6f}".format(p))