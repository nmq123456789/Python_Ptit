n = int(input())
a = []
dd = [0] * 500 
cnt = 0
ok = 0
maX = -1
while 1:
    a = [int(x) for x in input().split()]
    for i in a: dd[i] += 1
    if max(a) > maX: maX = max(a)
    cnt += len(a)
    if(cnt >= n): break
for i in range(1, maX):
    if dd[i] == 0:
        print(i)
        ok = 1
if ok == 0: print("Excellent!")
