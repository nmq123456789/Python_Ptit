s = input()
k = int(input())
a = []
dd = [0] * 1000
if len(s) % 2 == 1: s = s[0 : len(s) - 1]
for i in range(0,len(s) - 1, 2):
    x = int(s[i : i + 2])
    if dd[x] == 0: a.append(x)
    dd[x] += 1
if max(dd) < k: print("NOT FOUND")
else:
    a.sort()
    for i in a:
        if dd[i] >= k:
            print(i, dd[i])