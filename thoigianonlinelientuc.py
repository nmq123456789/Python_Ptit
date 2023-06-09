from datetime import datetime

class Online:
    def __init__(self, ten, time):
        self.ten = ten
        self.time = time
    
    def __str__(self) -> str:
        return self.ten + ' ' + str(int(self.time / 60))

a, index = [], 1
file = open('a.in')
for i in file:
    a.append(i.strip())

ans = []
t = int(a[0])
for i in range(t):
    ten, d1, d2 = a[index], a[index + 1], a[index + 2]
    day1 = datetime.strptime(d1, '%d/%m/%Y %H:%M:%S')
    day2 = datetime.strptime(d2, '%d/%m/%Y %H:%M:%S')
    distance = day2 - day1
    ans.append(Online(ten, distance.seconds + distance.days * 60 * 24 * 60))
    index += 3
ans = sorted(ans, key = lambda x: (-x.time, x.ten))
for i in ans: print(i)

    
