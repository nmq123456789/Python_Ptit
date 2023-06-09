t = int(input())
while(t > 0):
    s = input()
    cnt = 0
    for i in range(0, len(s)):
        if(s[i] != '4' and s[i] != '7'): 
            cnt = 1
            break
    if(cnt == 0): print("YES")
    else: print("NO")
    t = t - 1