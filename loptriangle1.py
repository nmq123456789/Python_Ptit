from math import sqrt
from decimal import Decimal

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, a):
        ox = self.x - a.x
        oy = self.y - a.y
        kc = sqrt(ox * ox + oy * oy)
        return kc
    def chuvi(self, a, b):
        d1 = self.distance(a)
        d2 = self.distance(b)
        d3 = a.distance(b)
        if d1 + d2 > d3 and d2 + d3 > d1 and d1 + d3 > d2:
            return '{:.2f}'.format(1 / 4 * sqrt((d1 + d2 + d3) * (d1 + d2 - d3) * (d1 - d2 + d3) * (-d1 + d2 + d3)))
        return 'INVALID'
t = int(input())
arr = []
for i in range(t):
    arr += [float(x) for x in input().split()]
for i in range(t):
    p1 = Point(arr[0 + i * 6], arr[1 + i * 6])
    p2 = Point(arr[2 + i * 6], arr[3 + i * 6])
    p3 = Point(arr[4 + i * 6], arr[5 + i * 6])
    for i in arr:
        if abs(i) > 1000:   print("INVALID")
    else:
        print(p1.chuvi(p2, p3))
    