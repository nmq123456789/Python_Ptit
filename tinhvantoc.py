from datetime import datetime
from decimal import ROUND_UP

class VanToc:
    def __init__(self, ma, ten, donvi, vantoc, time):
        self.ma = ma
        self.ten = ten
        self.donvi = donvi
        self.vantoc = vantoc
        self.time = time
    def out(self):
        print(self.ma, self.ten, self.donvi, self.vantoc, 'Km/h')
a = []
n = int(input())
for i in range(n):
    ten, diachi = input(), input()
    tmp = diachi.split() + ten.split()
    ma = ''
    for i in tmp: ma += i[0]
    time = input()
    d1 = datetime.strptime(time, '%H:%M')
    d2 = datetime.strptime('6:00', '%H:%M')
    distance = d1 - d2
    giay = distance.seconds
    vantoc = round(120 / giay * 3600)
    a.append(VanToc(ma, ten, diachi, vantoc, time))
a = sorted(a, key = lambda x: x.time)
for i in a:
    i.out()
