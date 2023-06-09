t = int(input())
for i in range(t):
    x, y = [x for x in input().split()]
    s1 = input().strip()
    if(s1.count(' ')) : s1, s2 = s1.split()
    else : s2 = input()
    a = min(x, y)
    b = max(x, y)
    print(int(s1.replace(b, a)) + int(s2.replace(b, a)), int(s1.replace(a, b)) + int(s2.replace(a, b)))