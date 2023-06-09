class Name:
    def __init__(self, s) -> None:
        tmp, a = s.split(), ''
        self.ten = tmp[-1]
        self.ho = tmp[0]
        for i in s[1 : len(tmp) - 1]:
            a +=  i + ' '
        self.dem = a.strip()
        self.fullname = s.strip()

    def __str__(self) -> str:
        return self.fullname

a, ans = [], []
with open ('DANHSACH.in') as file:
    for i in file:
        a.append(i.strip())
for i in a:
    s = i.split()
    x = ''
    for i in s:
        x += i.title() + ' '
    ans.append(Name(x.strip()))
ans = sorted(ans, key = lambda x : (x.ten, x.ho, x.dem))
for i in ans: print(i)