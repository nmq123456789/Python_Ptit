s1 = input().lower()
s2 = input().lower()
s2 = s2.split(" ")
s1 = s1.split(" ")
ans = set(s1)
ans.update(s2)
ans = sorted(ans)
cnt = []
for i in ans: print(i, end = " ")
print()
for i in s1:
    if i in s2: cnt = cnt + [i]
cnt2 = set(cnt)
cnt2 = sorted(cnt2)
for i in cnt2: print(i, end = " ")