#problem done and submitted
t = int(input())
for i in range(1,t+1):
    n = int(input())
    a = list(map(int,input().split())) 
    odds = 0
    even1 = 0
    even2 = 0
    for num in a:
        if num % 2 == 1:
            odds += 1
        elif num % 4 == 0:
            even1 += 1
        else:
            even2 += 1
    print(max(odds,even1,even2))  

