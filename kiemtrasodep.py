def check(n):
    for i in range(0, len(s)):
        if i < len(n) - 1:
            if n[i] == n[i + 1]: return 0
        if s[i] != s[0] and s[i] != s[1]:  return 0
    return 1
t = int(input())
for i in range(t):
    s = input()
    if(check(s) == 1): print("YES")
    else: print("NO")