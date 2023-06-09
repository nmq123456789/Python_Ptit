x = [0, 0, 0, 2.5, 2.5, 3.0, 3.0, 3.5, 3.5, 3.5, 4.0, 4.0, 4.0, 4.5, 4.5, 4.5, 5.0 , 5.0, 5.0, 5.0, 5.5, 5.5, 5.5, 6.0, 6.0, 6.0, 6.0, 6.5, 6.5, 6.5, 7.0, 7.0, 7.0, 7.5, 7.5, 8.0, 8.0, 8.5, 8.5, 9.0, 9.0 ]
# for i in range(0, len(x)):
#     print(x[i],i)
t = int(input())
for i in range(t):
    a, b, c, d = [float(x) for x in input().split()]
    a = int(a)
    b = int(b)
    sum = x[a] + x[b] + c + d
    sum /= 4
    ans1 = int(sum)
    sum *= 100
    ans2 = int(sum)
    ans2 %= 100
    sum /= 100
    if ans2 >= 25 and ans2 < 75:
        sum = ans1 + 0.5 
    if ans2 >= 75:
        sum = ans1 + 1
    if ans2 < 25:
        sum = ans1 + 0.0
    print("%.1f"  % sum)