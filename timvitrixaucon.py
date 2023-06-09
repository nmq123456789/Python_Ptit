a, index = [], 1
file = open('STRING.in')
for i in file:
    a.append(i.strip())

t = int(a[0])
for i in range(t):
    vt = 0
    s1, s2 = a[index], a[index + 1]
    while 1:
        x = s1.find(s2, vt)
        if x == -1: break
        else:
            print(x + 1, end = ' ')
            vt = x + 1
    index += 2
    print()

    