t = int(input())
for i in range(t):
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    ans = 0
    for i in range(0, n):
        if a[i] > b[i]: 
            ans = 1
            break
    if ans == 0: print("YES")
    else: print("NO")