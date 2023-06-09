t = int(input())
for i in range(t):
    n =int(input())
    if n % 2 == 1:
        sum = 0
        for i in range(0, int(n/2) + 1):
            sum += 1/(2 * i + 1)
        print('%.6f' % sum)
    else:
        sum = 0
        for i in range(1, int(n/2) + 1):
            sum += 1/(2 * i)
        print('%.6f' % sum)