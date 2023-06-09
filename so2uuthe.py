def ql(s, cnt2):
    if len(s) == 10: return
    if cnt2 != 0 and cnt2 > len(s) / 2 and s[0] != '0' : ans.append(int(s))
    ql(s + '2', cnt2 + 1)
    ql(s + '1', cnt2)
    ql(s + '0', cnt2)

t = int(input())
for i in range(t):
    ans = []
    n = int(input())
    ql('', 0)
    ans = sorted(ans)
    for i in range(n): print(ans[i], end = " ")
    print()