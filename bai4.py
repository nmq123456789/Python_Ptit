t = int(input())
for i in range(t):
    s1, s2 = input().lower().strip().split(), input().strip().split()
    for i in s2:
        if i.lower() in s1:
            print(i, end = ' ')
    print()