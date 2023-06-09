t = int(input())
for i in range(t):
    n = int(input())
    stack = []
    a = [int(x) for x in input().split()]
    for i in range(0, len(a)):
        while(len(stack) > 0 and a[stack[-1]] <= a[i]): stack.pop()
        if len(stack) == 0: print(i + 1, end = " ")
        else: print(i - stack[-1], end = " ")
        stack.append(i)
    print()

