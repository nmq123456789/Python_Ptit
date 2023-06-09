def tn(s):
    if s == s[::-1]: return 1
    return 0

a = []
cnt = dict()    
dai = -1
with open('VANBAN.in') as file:
    for i in file:
        a.append(i.rstrip().strip())
for i in a:
    tmp = [x for(x) in i.split()]
    for i in tmp:
        if tn(i):
            if len(i) >= dai:
                dai = len(i)
            if i in cnt:
                cnt.update({i : cnt[i] + 1})
            else: cnt.update({i : 1})
ans = dict()
for i in cnt.keys():
    if len(i) == dai: ans.update({i : cnt[i]})
for i in ans.keys():
    print(i, ans[i])

