n = int(input())
a = [[]] * n
ans = 0
for i in range(n):    a[i] = input()
for i in range(n):
    cnt = 0
    for j in range(n):
        if a[i][j] == 'C': cnt += 1
    ans = ans + cnt * ((cnt - 1) / 2)
for i in range(n):
    cnt = 0
    for j in range(n):
        if a[j][i] == 'C': cnt += 1
    ans = ans + cnt * ((cnt - 1) / 2)
print(int(ans))