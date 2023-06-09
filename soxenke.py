t = int(input())
for i in range(t):
    s = input()
    ok = 1
    for i in range(0, len(s)):
        if(i % 2 == 0):
            if(s[i] != s[0]):
                ok = 0
                break
    if(len(s) % 2 == 1 and s[0] != s[1] and ok == 1):
        print("YES")
    else:
        print("NO")