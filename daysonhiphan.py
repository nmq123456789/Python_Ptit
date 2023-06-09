n = int(input())
a = [int(x) for x in input().split()]
ans = 0
for i in range(0, n - 1):
    if a[i] != a[i + 1]: ans += 1
print(ans)