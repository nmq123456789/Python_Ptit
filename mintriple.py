import re

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    a = re.split("\s", s)
    min1, min2, min3 = 10 ** 20, 10 ** 20, 10 ** 20
    for i in a:
        if int(i) < min1: min1 = int(i)
    for i in a:
        if int(i) < min2 and int(i) > min1: min2 = int(i)
    for i in a:
        if int(i) < min3 and int(i) > min2: min3 = int(i)
    print(min1 + min2 + min3)
    