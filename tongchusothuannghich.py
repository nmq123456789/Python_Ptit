from xml.etree.ElementTree import tostring


t = int(input())
for i in range(t):
    s = input()
    sum = 0
    for j in range(0, len(s)):
        sum += int(s[j])
    ans = str(sum)
    cnt = ans[::-1]
    if ans == cnt and len(ans) > 1: print("YES")
    else: print("NO")