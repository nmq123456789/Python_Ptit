t = int(input())
for i in range(t):
    n , d = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    for i  in range(d, len(a)): print(a[i], end = " ")
    for i  in range(0, d): print(a[i],end = " ")
    print()