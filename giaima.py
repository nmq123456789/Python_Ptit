t = int(input())
for i in range(t):
    s = input()
    cnt = ""
    for i in range(0, len(s)):
        if(s[i] > '0' and s[i] <= '9'):
            for j in range(0, int(s[i])):
                cnt += s[i - 1]
    print(cnt)