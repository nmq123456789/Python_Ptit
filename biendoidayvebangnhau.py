from posixpath import split


n = int(input())
a = [int(x) for x in input().split()]
vt, ans = -1, 10 ** 20
for i in a:
    t = 0
    for j in a:
        t += abs(i - j)
    if ans > t:
        ans = t
        vt = i
print(ans, vt)