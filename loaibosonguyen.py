import sys
a, ans = [], []

# with open('DATA.txt') as file:
file = open('DATA.txt')
for i in file:
    a.append(i.strip())

for i in a:
    tmp = i.split()
    for j in tmp:
        if not j.isdigit(): ans.append(j)
        elif len(j) > 9: ans.append(j)
ans = sorted(ans)
print(*ans)          
                