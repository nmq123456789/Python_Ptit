t = int(input())
for i in range(t):
    n = int(input())
    m = n
    sum = 0
    while(n > 0):
        x = n % 10
        tich = 1
        for i in range(2, x + 1):    tich *= i
        sum += tich
        n = int(n / 10)
    if sum == m: print("Yes")
    else: print("No")

        
