class NhanVien:
    def __init__(self, ma, ten, diem, xeploai):
        self.ma = ma
        self.ten = ten
        self.diem = diem
        self.xeploai = xeploai

    def out(self):
        print('{} {} {:.2f} {}'.format(self.ma, self.ten, self.diem, self.xeploai))
        
n = int(input())
a = []
for i in range(n):
    ma = 'TS0' + str(i+1)
    ten = input()
    diem1 = float(input())
    diem2 = float(input())
    while diem1 > 10: diem1 /= 10
    while diem2 > 10: diem2 /= 10
    xeploai = ''
    diemtb = (diem1 + diem2) / 2
    if diemtb < 5: xeploai = 'TRUOT'
    elif diemtb < 8: xeploai = 'CAN NHAC'
    elif diemtb <= 9.5: xeploai = 'DAT'
    else: xeploai = 'XUAT SAC'
    a.append(NhanVien(ma, ten, diemtb, xeploai))
a = sorted(a, key = lambda x: -x.diem)
for i in a:
    i.out()
