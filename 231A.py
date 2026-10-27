#problem done and submitted
t = int(input())
count = 0
for _ in range(t):
    arr = list(map(int,input().split()))
    if sum(arr) >= 2:
        count+=1
print(count)
