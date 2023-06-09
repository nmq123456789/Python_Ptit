from itertools import combinations

x, y = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
st = set(a)
ans = combinations(sorted(st), y)
for i in ans:
    print(*i)
