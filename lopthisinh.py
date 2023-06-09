class ThiSinh:
    def __init__(self, name, dob, d1, d2, d3):
        self.name = name
        self.dob = dob
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    def out(self):
        print(self.name, self.dob, "{:.1f}".format(self.d1 + self.d2 + self.d3) )
a = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
a.out()
