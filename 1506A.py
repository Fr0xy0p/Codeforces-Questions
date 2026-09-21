#problem done and submitted
t = int(input())
for i in range(1,t+1):
    n,m,x = map(int,input().split())
    row = 0
    colm = 0

    row = x - (x//n)*n
    colm = x//n +1
    ans = m*(row - 1)+ colm
    if row == 0:
        row = n 
        colm-=1
        ans = m*(row - 1)+ colm
        
    
    print(ans)
    