from datetime import datetime

# date_time_str = '18/09/19'

# date_time_obj = datetime.strptime(input(), '%d/%m/%Y')


# print ("The type of the date is now",  type(date_time_obj))
# print ("The date is", date_time_obj)
# d1 = datetime.strptime(input(), '%d/%m/%Y')
# d2 = datetime.strptime(input(), '%d/%m/%Y')
# ngayo = d2 - d1
# print(ngayo.days)
d=0
s = set()
while 1:
    l=[int(x) % 42 for x in input().split()]
    d += len(l)
    for c in l:
        s.update(l)
    if(d == 10):
        break
print(len(s))
