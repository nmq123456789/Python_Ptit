n, k = [int(x) for x in input().split()]
cnt = {}
for i in  range(n):
    s = ''
    for j in input().lower() + ' ':
        if (j >= 'a' and j <= 'z') or (j >= '0' and j <= '9') : s += j
        else:
            if s != '':
                if s in cnt: cnt[s] += 1
                else: cnt[s] = 1
                s = ''
cnt = sorted(cnt.items(), key = lambda x: (-x[1], x[0]))
for i in cnt: 
    if i[1] >= k:
        print(*i, sep = ' ')
