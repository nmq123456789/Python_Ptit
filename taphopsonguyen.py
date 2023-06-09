n, m = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()])
b = sorted([int(x) for x in input().split()])
st = set(a)
se = set(b)
a = sorted(st)
b = sorted(se)
for i in a:
    if (i in b): print(i, end = " ")
print()
for i in a:
    if not(i in b): print(i, end = " ")
print()
for i in b:
    if not(i in a): print(i, end = " ")
