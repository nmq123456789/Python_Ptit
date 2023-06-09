a, K, N = [int(x) for x in input().split()]
ok = 0 
x = int(N / K) + 1
for i in range(x):
    s = (i * K) - a
    if(s > 0):
        print(s, end = ' ')
        ok = 1
if ok == 0: 
    print("-1")
