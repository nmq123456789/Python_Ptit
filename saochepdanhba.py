class ThongTin:
    def __init__(self, ten, sdt, ngay):
        self.ten = ten
        self.dem = self.ten.split()[-1]
        self.sdt = sdt
        self.ngay = ngay

    def out(self):
        print(self.ten + ': ', self.sdt, self.ngay)
text = []
with open ('SOTAY.txt') as file:
    for i in file:
        text.append(i.rstrip().strip())

i, ans, ngay = 0, [], ''
while i < len(text):
    if(text[i].split()[0] == 'Ngay'):
        ngay = text[i].split()[1]
        ten = text[i + 1]
        dt = text[i + 2]
        i += 3
    else:
        ten = text[i]
        dt = text[i + 1]
        i += 2
    ans.append(ThongTin(ten, dt, ngay))
ans = sorted(ans, key = lambda x: (x.dem, x.ten))
for i in ans: i.out()