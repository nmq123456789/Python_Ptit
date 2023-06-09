from decimal import ROUND_HALF_UP, Decimal


class SinhVien:
    def __init__(self, ma, ten, diem):
        self.ma = ma
        self.ten = ten
        self.diem = diem
    def out(self):
        print(self.ma, self.ten, self.diem, end = ' ')

n = int(input())
a = []
for i in range(n):
    ma = 'SV{:02d}'.format(i + 1)
    s = input().strip().split()
    ten = ''
    for i in s: ten += i.title() + ' '
    lthd, c, tin = Decimal(input()), Decimal(input()), Decimal(input())
    dtb = (lthd * 3 + c * 3 + tin * 2) / 8
    tb = dtb.quantize(Decimal('0.01'), ROUND_HALF_UP)
    a.append(SinhVien(ma, ten, tb))
a = sorted(a, key = lambda x: (-x.diem, x.ma))
a[0].out()
print(1)
stt = 1
for i in range(1, len(a)):
    a[i].out()
    if a[i].diem == a[i - 1].diem: 
        print(stt)
        stt = i
    else:
        print(i + 1)
    