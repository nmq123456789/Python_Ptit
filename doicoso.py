cs = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = int(input())
for i in range(t):
    n, b = [int(x) for x in input().split()]
    ans = ""
    while n > 0:
        x = n % b
        ans = cs[x] + ans
        n = int(n / b)
    print(ans)