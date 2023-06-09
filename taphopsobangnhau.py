n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
s1 = sorted(set(a))
s2 = sorted(set(b))
if s1 == s2: print("YES")
else: print("NO")
