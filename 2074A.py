#problem completed and submitted
t = int(input())
for i in range(1,t+1):
    l,r,d,u = map(int,input().split())
    if l ==r and r ==d and d == u:
        print("Yes")
    else:
        print("No")