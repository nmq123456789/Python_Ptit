n = int(input())
count, ans, cnt = 0, [], []
for i in range(n):
    s = input().split()
    if len(cnt) == 0 and len(s) == 6: ans.append(1)
    cnt.append(s)
    if len(cnt) > 1 and len(s) == 6 and len(cnt[-2]) == 7: ans.append(1)
    if len(s) == 7: count += 1
    if count == 4:
        ans.append(2)
        count = 0
print(len(ans))
for i in ans: print(i)