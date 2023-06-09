n = int(input())
a = [int(x) for x in input().split()]
dd = [0] * 30002
for i in a:
    dd[i] += 1
for i in range(1, 30002):
    if dd[i] == 0:
        print(i)
        break