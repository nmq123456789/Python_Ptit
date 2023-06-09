from itertools import permutations
t = int(input())
for i in range(t):
    n = int(input())
    a = []
    for i in range(1, n + 1): a.append (i)
    hv = permutations(a)
    hv = sorted(hv, reverse = True)
    print(len(hv))
    for i in hv:
        print(*i, sep = '', end = " ")
    print()