dem = 0
ans = 0
dd = [0] * 42
while 1:
    a = [int(x) for x in input().split()]
    dem += len(a)
    for i in a:
        dd[i % 42] = 1
    if dem == 10:
        break
for i in dd:
    if i > 0: ans += 1
print(ans)