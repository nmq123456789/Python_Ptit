from math import log

cd = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
t = int(input())
for i in range(t):
    x = int(input())
    s = input()
    x = int(log(x)/log(2))
    while len(s) % x != 0 : s = '0' + s
    for i in range(0, len(s), x):
        ans = 0
        for j in range(i, i + x):
            if s[j] == '1': 
                ans += pow(2, x - j + i - 1)
        print(cd[ans], end = "")
    print()


