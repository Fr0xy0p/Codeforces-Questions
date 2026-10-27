#problem done and submitted
t = int(input())
for _ in range(t):
    n,m,d = map(int,input().split())
    x = d//m
    y = n//(x+1)
    z = n%(x+1)
    if z > 0:
        ans = y + 1
        print(ans)
    else:
        ans = y
        print(ans)
