t = int(input())
for i in range(t):
    n = input()
    sum = 0
    tich = 1
    ok = 0
    for i in range(0, len(n)):
        if i % 2 == 1:
            sum += int(n[i])
        else:
            if n[i] != '0': 
                ok = 1
                tich *= int(n[i])
    if ok == 0:
        print(0, sum)
    else:
        print(tich, sum)
            
