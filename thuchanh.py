from math import gcd

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def cong(self, a):
        x = self.tu * a.mau + self.mau * a.tu
        y = self.mau * a.mau
        return PhanSo(x, y)

    def out(self):
        print('{:.0f}/{:.0f}'.format(self.tu / gcd(self.tu, self.mau), self.mau / gcd(self.tu, self.mau)))
tu1, mau1, tu2, mau2 = [int(x) for x in input().split()]
a = PhanSo(tu1, mau1)
b = PhanSo(tu2, mau2)
c = a.cong(b)
c.output()   