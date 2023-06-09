n, k = [int(x) for x in input().split()]
a =  [int(x) for x in input().split()]
b = [0] * 100
max1 = 0
max2 = 0
vt = -1
for i in a: b[i] += 1
max1 = max(b)
for i in range(0, len(b)):
    if b[i] > max2 and b[i] < max1:
        vt = i
        max2 = b[i]
if vt != -1: print(vt)
else: print("NONE")