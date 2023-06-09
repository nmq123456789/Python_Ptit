t = int(input())
for i in range(t):
    ok, sum = 0, 0
    for j in input():
        if j != '0' and j != '1' and j != '2' and j != '3' and j != '4':
            ok = 1
            break
        sum += int(j)
    if ok == 0 and sum == 5: print('YES')
    else: print('NO')
    