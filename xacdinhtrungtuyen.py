class GiaoVien:
    def __init__(self, ma, ten, mon, diem, ketqua):
        self.ma = ma
        self.ten = ten
        self.mon = mon
        self.diem = diem
        self.ketqua = ketqua

    def out(self):
        print('{} {} {} {:.1f} {}'.format(self.ma, self.ten, self.mon, self.diem, self.ketqua))

t = int(input())
a = []
for i in range(t):
    mgv = 'GV{:02d}'.format(i + 1)
    ten, ma, tin, chuyenmon, ketqua, mon = input(), input(), float(input()), float(input()), '', ''
    if ma[:1] == 'A': mon = 'TOAN'
    elif ma[:1] == 'B': mon = 'LY'
    else: mon = 'HOA'
    if ma[1:] == '1': tin += chuyenmon + 2 + tin
    elif ma[1:] == '2': tin += chuyenmon + 1.5 + tin
    elif ma[1:] == '3': tin += chuyenmon + 1 + tin
    else: tin += chuyenmon + tin
    if tin >= 18: ketqua = 'TRUNG TUYEN'
    else: ketqua = 'LOAI'
    a.append(GiaoVien(mgv, ten, mon, tin, ketqua))
a = sorted(a, key = lambda x: -x.diem)
for i in a: i.out()
