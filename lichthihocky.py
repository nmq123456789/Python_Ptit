class MonHoc:
    def __init__(self, ma, ten) -> None:
        self.ma = ma
        self.ten = ten
    
class LichThi:
    def __init__(self, macathi, MonHoc, ngaythi, giothi, nhomthi) -> None:
        self.macathi = macathi
        self.MonHoc = MonHoc
        self.ngaythi = ngaythi
        self.giothi = giothi
        self.date = ngaythi[6:] + ngaythi[3 : 6] + ngaythi[0 : 2] 
        self.nhomthi = nhomthi
    def __str__(self) -> str:
        return self.macathi + ' ' + self.MonHoc.ma + ' ' + self.MonHoc.ten + ' ' + self.ngaythi + ' ' + self.giothi + ' ' + self.nhomthi
    
list1 = []
t1, t2 = [int(x) for x in input().split()]
for i in range(t1):
    list1.append(MonHoc(input(), input()))

list2 = []
for i in range(t2):
    macathi = 'T{:03d}'.format(i + 1)
    a = input().split()
    for j in list1:
        if j.ma == a[0]: 
            list2.append(LichThi(macathi, j, a[1], a[2], a[3]))
list2 = sorted(list2, key = lambda x : (x.date, x.giothi, x.MonHoc.ma))
for i in list2:
    print(i)