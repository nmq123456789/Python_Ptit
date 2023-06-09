from functools import cmp_to_key


def tich(a):
    n = str(a)
    ans = 1
    for i in range(len(n)):
        if i % 2 == 0 and n[i] != '0':
            ans *= int(n[i])
    return ans

def cmp(a, b):
    ticha = tich(a)
    tichb = tich(b)
    if ticha < tichb: return -1
    elif ticha > tichb: return 1
    else:
        if int(a) < int(b): return -1
        elif int(a) > int(b): return 1
    return 0

t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    a = sorted(a, key = cmp_to_key(cmp))
    for i in a: print(i, end = ' ')
    print()