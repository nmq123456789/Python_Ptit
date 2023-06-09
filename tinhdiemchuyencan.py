class SinhVien:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        
class ChuyenCan:
    chuyenCan = 0
    def __init__(self, SinhVien, sum):
        self.SinhVien = SinhVien
        self.sum = sum
    
    def ma(self):
        return self.SinhVien.ma

    def out(self):
        print(self.SinhVien.ma, self.SinhVien.ten, self.SinhVien.lop, self.sum, end = '')
        if self.sum == 0: print(' KDDK')
        else: print()

n = int(input())
sinhvien = []
for i in range(n):
    sinhvien.append(SinhVien(input(), input(), input()))
dihoc = []
for i in range(n):
    sum = 10
    msv, chuyencan = [x for(x) in input().split()]
    for i in chuyencan: 
        if i == 'm': sum -= 1
        if i == 'v': sum -= 2
    if sum < 0: sum = 0
    for sv in sinhvien:
        if sv.ma == msv:
            dihoc.append(ChuyenCan(sv, sum))
for i in sinhvien:
    for j in dihoc:
        if i.ma == j.ma():
            j.out()


