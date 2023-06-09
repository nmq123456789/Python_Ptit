t = int(input())
for i in range(t):
    s = input()
    sum = 0
    ans = ""
    for i in range(0, len(s)):
        if(s[i] < '0' or s[i] > '9'): ans += s[i]
        else: 
            sum += int(s[i])
    ans = sorted(ans)
    for i in range(0, len(ans)):
        print(ans[i], end = "")
    print(sum)