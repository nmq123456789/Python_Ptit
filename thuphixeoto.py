def GiaVe(xe, ghe):
    if xe == "Xe_con":
        if ghe == '5' : return 10000
        else: return 15000
    if xe == "Xe_khach":
        if ghe == '29' : return 50000
        else: return 70000
    return 20000
n = int(input())
ans = {}
# 30F-123.15 Xe_con 5 OUT 06/11/2021
for i in range(n):
    a = input().split()
    if a[3] == "IN":
        if a[4] not in ans:
            ans[a[4]] = GiaVe(a[1], a[2])
        else:
            ans[a[4]] += GiaVe(a[1], a[2])
for i in ans: print(i + ':', ans[i])