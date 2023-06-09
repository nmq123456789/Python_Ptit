n = int(input())
a = [int(x) for x in input().split()]
ans = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if a[i] > a[j]: ans += 1
print(ans)