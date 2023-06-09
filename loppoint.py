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
        return "{:.4f}".format(kc)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1