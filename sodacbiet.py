mod = 1e9 + 7
# t = int(input())
a = [1]
while a[len(a) - 1] < mod:
    a.append(a[len(a) - 1] * 3)
dd = [0] * 1000000007
dd[0] = 1
for i in range(0, len(a) - 1):
    for j in range(a[i + 1], 0, -1):
        if dd[j] == 0 and dd[j - a[i]] == 1: a.append(j % mod)
print(a)
# for i in range(t):
#     n, k = [int(x) for x in input().split()]
