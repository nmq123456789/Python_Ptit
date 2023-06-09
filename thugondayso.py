n = int(input())
a = [int(x) for x in input().split()]
ans = []
for i in a:
    if len(ans) == 0: ans = ans + [i]
    else:
        if (ans[-1] + i) % 2 == 0: 
            ans.pop()
        else:
            ans = ans + [i]
print(len(ans))