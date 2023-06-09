t = int(input())
for i in range(t):
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    if sum % 9 == 0: print('YES')
    else: print('NO')