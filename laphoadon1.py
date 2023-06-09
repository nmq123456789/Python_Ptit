class hoadon:
    tien = 0
    def __init__(self, ma, ten, cu, moi):
        self.ma = ma
        self.ten = ten
        self.cu = cu
        self.moi = moi
        sum = moi - cu
        if sum <= 50:
            sum *= 100
            sum += sum * 0.02
        elif sum <= 100:
            sum = 50 * 100 + (sum - 50) * 150
            sum += sum * 0.03
        else:
            sum = 50 * 100 + 50 * 150 + (sum - 100) * 200
            sum += sum * 0.05
        self.tien = round(sum)
        
    def out(self):
        return self.ma + ' ' + self.ten + ' ' + str(self.tien)


n = int(input())
a = []
for i in range(n):
    ten, cu, moi = input(), int(input()), int(input())
    ma = "KH{:02d}".format(i + 1)
    a.append(hoadon(ma, ten, cu, moi))
a = sorted(a, key = lambda x: -x.tien)
for i in a: print(i.out())