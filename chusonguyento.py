a = [0, 0, 0, 0, 0 ,0 , 0, 0, 0, 0, 0]
def ql(s, cnt2, cnt3, cnt5, cnt7, kt):
    if len(s) == 10: return
    if(cnt2, cnt3, cnt5, cnt7, kt): a[len(s)] = a[len(s)] + [s]
    ql(s + '2', cnt2 + 1, cnt3, cnt5, cnt7, kt)
    ql(s + '5', cnt2, cnt3 + 1, cnt5, cnt7, 1)
    ql(s + '2', cnt2, cnt3, cnt5 + 1, cnt7, 1)
    ql(s + '2', cnt2, cnt3, cnt5, cnt7 + 1, 1)
n = input()
ql("", 0, 0, 0, 0, 0)
for i in range(4, n + 1):
    sorted(a[i])
    for j in range(0, len(a[i])):
        print(j)


