class monthi:
    def __init__(self, ma, ten, hinhthuc):
        self.ma = ma
        self.ten = ten
        self.hinhthuc = hinhthuc
    def out(self):
        return self.ma + ' ' + self.ten + ' ' + self.hinhthuc
n = int(input())
a = []
for i in range(n):
    ma, ten, hinhthuc = input(), input(), input()
    a.append(monthi(ma, ten, hinhthuc))
a = sorted(a, key = lambda x: x.ma)
for i in a:
    i.out()