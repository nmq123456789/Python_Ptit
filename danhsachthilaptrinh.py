class Team:
    def __init__(self, mateam, ten, truong):
        self.mateam = mateam
        self.ten = ten
        self.truong = truong

class ThiSinh:
    def __init__(self, Team, mts, hoten):
        self.Team = Team
        self.mts = mts
        self.hoten = hoten
    
    def out(self):
        print('{} {} {} {}'.format(self.mts, self.hoten, self.Team.ten, self.Team.truong))

t1 = int(input())
team = []
for i in range(t1):
    ma = 'Team{:02d}'.format(i + 1)
    team.append(Team(ma, input(), input()))

t2 = int(input())
thisinh = []
for i in range(t2):
    ma = 'C{:03d}'.format(i + 1)
    hoten, mateam = input(), input()
    for x in team:
        if x.mateam == mateam:
            thisinh.append(ThiSinh(x, ma, hoten))
            break
thisinh = sorted(thisinh, key = lambda x: x.hoten)
for x in thisinh: x.out()
