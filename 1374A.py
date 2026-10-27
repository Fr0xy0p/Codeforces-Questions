#problem done and submitted
t = int(input())
for _ in range(t):
    x,y,n = map(int,input().split())
    rem = n%x
    if rem>=y:
        ans = n-(rem-y)
    else:
        ans = n - (rem-y+x)
    print(ans)