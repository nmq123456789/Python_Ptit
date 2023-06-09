from decimal import ROUND_HALF_UP, Decimal

stt = 1
class BangDiem:
    maHS = 'HS'
    dtb = 0
    xeploai = ''
    def __init__(self, name, bd):
        global stt
        self.name = name
        self.bd = bd
        self.maHS += '{:02d}'.format(stt)
        stt += 1
        x = bd[0] * 2 + bd[1] * 2
        for i in range(2, 10): x += bd[i]
        x /= 12
        if x < 5 : self.xeploai = 'YEU'
        elif x < 7 : self.xeploai = 'TB'
        elif x < 8 : self.xeploai = 'KHA'
        elif x < 9 : self.xeploai = 'GIOI'
        else : self.xeploai = 'XUAT SAC'
        self.dtb = x.quantize(Decimal('0.1'), ROUND_HALF_UP)
    def out(self):
        print(self.maHS, self.name, self.dtb, self.xeploai)

n = int(input())
a = []
for i in range(n) :
    b = input()
    c = [Decimal(x) for x in input().split()]
    a.append(BangDiem(b, c))

a = sorted(a, key = lambda x : (- x.dtb, x.maHS))
for i in a :
    i.out()
