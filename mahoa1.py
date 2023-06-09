t = int(input())
for i in range(t):
    s = input()
    s += " "
    dem = 1
    for i in range(0, len(s) - 1):
        if(s[i] == s[i + 1]): dem = dem + 1
        else:
            print(dem, end = "")
            print(s[i], end = "")
            dem = 1
    print()
