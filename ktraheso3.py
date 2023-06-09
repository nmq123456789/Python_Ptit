t = int(input())
for i in range(t):
    s = input()
    ok = 0
    for i in range(0, len(s)):
        if(s[i] != '1' and s[i] != '0' and s[i] != '2'):
            ok = 1
            print("NO")
            break
    if(ok == 0): print("YES")