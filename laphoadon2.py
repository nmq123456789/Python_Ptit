from datetime import datetime

class hoadon:
    thanhtien = 0
    def __init__(self, ma, ten, sophong, ngayo, gia, phatsinh):
        self.ma = ma
        self.ten = ten
        self.sophong  = sophong
        self.ngayo = ngayo
        self.gia = gia
        self.thanhtien = gia * ngayo + phatsinh
    def out(self):
        print(self.ma, self.ten, self.sophong, self.ngayo, self.thanhtien)

n = int(input())
a = []
for i in range(n):
    ma = 'KH{:02d}'.format(i + 1)
    ten = input()
    sophong = input()
    d1 = datetime.strptime(input(), '%d/%m/%Y')
    d2 = datetime.strptime(input(), '%d/%m/%Y')
    phatsinh = int(input())
    tmp = d2 - d1
    ngayo = tmp.days + 1
    if sophong[0] == '1': 
        gia = 25
    if sophong[0] == '2': 
        gia = 34
    if sophong[0] == '3': 
        gia = 50
    if sophong[0] == '4': 
        gia = 80
    a.append(hoadon(ma, ten, sophong, ngayo, gia, phatsinh))
a = sorted(a, key = lambda x: -x.thanhtien)
for i in a:
    i.out()

