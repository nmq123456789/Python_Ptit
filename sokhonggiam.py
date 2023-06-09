t = int(input())
for i in range(t):
    ok = 0
    s = input()
    for i in range(0, len(s) - 1):
        if(int(s[i]) - int(s[i + 1]) > 0): 
            ok = 1
            print("NO")
            break
    if ok == 0: print("YES")