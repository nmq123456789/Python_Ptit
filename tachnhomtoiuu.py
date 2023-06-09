n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()
ans = 0
for i in range(0, len(a) - 1):
    if a[i + 1] - a[i] > k: ans += 1
print(ans + 1)