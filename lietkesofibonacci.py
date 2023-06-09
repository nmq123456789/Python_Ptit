t = int(input())
for i in range(t):
    a, b = [int(x) for x in input().split()]
    fibo = [0, 1]
    x = 0
    y = 1
    for i in range(2, 93):
        k = x + y
        fibo.append(k)
        x = y
        y = k
    for i in range(a, b + 1): print(fibo[i], end = " ")
    print()