import json

with open ('flights.json') as file:
    data = json.load(file)

# print(data)
t = int(input())
for i in range(t):
    nam, thang = [x for x in input().split()]
    sum = 0
    for i in data['flights']:
        if int(i['year']) == int(nam) and i['month'] == thang:
            sum += int(i['passengers'])
    if sum == 0: print('Invalid')
    else: print(sum)