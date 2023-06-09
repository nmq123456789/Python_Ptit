from operator import xor
t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in a:
        ans = xor(ans, i)
    print(ans)
