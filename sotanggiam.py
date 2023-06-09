t = int(input())
for i in range(t):
    s = input()
    vt1 = -1
    vt2 = -1
    for i in range(0, len(s) - 1):
        if(ord(s[i]) >= ord(s[i + 1])):
            vt1 = i
            break
    m = s[::-1]
    for i in range(0, len(m) - 1):
        if(ord(m[i]) >= ord(m[i + 1])):
            vt2 = i
            break
    if vt1 == len(m) - vt2 - 1: print("YES")
    else: print("NO")