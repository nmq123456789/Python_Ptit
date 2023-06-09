t = int(input())
for i in range(t):
    n = int(input())
    sum = 0
    ok = 0
    while(n > 10):
        sum += n % 10
        if(abs(n % 10 - (int(n / 10) % 10)) != 2):
            ok = 1
            break
        n = int(n / 10)
    sum += n % 10
    if(ok == 0 and sum % 10 == 0): print("YES")
    else: print("NO")