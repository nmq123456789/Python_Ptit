n = int(input())
a = []
for i in range(n):
    s = input() + " "
    sum = 0
    for i in range(0, len(s)):
        if s[i].isdigit(): sum = sum * 10 + int(s[i])
        else:
            if(s[i - 1].isdigit()):
                a.append(sum)
                sum = 0
for i in sorted(a): print(i)