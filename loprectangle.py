class Rectangle:
    def __init__(self, dai, rong, color):
        self.dai = dai
        self.rong = rong
        self.color = color.title()

    def check(self) :
        if self.dai <= 0 or self.rong <=0 : return 0
        return 1
    
    def output(self) :
        if self.check() == 1 : print((self.dai + self.rong) * 2, self.dai * self.rong, self.color, sep = ' ')
        else : print('INVALID')
    
a = input().split()
rec = Rectangle(int(a[0]), int(a[1]), (a[2]))
rec.output()