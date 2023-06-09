def kt(canh, dau, cuoi, diem, n):
    st, dd = [dau], [0] * (n + 1)
    dd[dau] = 1
    while len(st) > 0:
        x = st.pop()
        if x == cuoi: return False
        for i in canh[x]:
            if dd[i] == 0 and x != diem:
                st.append(i)
                dd[i] = 1
    return True

t = int(input())
for i in range(t):
    N, M , u , v = [int(x) for x in input().split()]
    canh = {x:[] for x in range(1, N + 1)}
    for j in range(M):
        x, y = [int(x) for x in input().split()]
        canh[x].append(y)
    cnt = 0
    for i in range(N + 1):
        if i != u and i != v:
            if kt(canh, u, v, i, N): cnt += 1
    print(cnt)
