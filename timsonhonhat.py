t = int(input())
for i in range(t):
    s = input()
    ans =  10 ** 20
    sum = 0
    s += 'a'
    for i in range(0, len(s)):
        if s[i].isalpha():
            if i != 0 and s[i - 1].isdigit():
                ans = min(sum, ans)
                sum = 0
        else: sum = sum * 10 + int(s[i])
    print(ans)