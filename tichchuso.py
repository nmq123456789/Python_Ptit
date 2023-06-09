t = int(input())
for i in range(t):
    s = input()
    sum = 1
    for i in range(0, len(s)):
        if(s[i] != '0'):
            sum *= int(s[i])
    print(sum)