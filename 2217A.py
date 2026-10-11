#problem done and submitted
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    total_sum = sum(arr)
    if total_sum % 2 !=0 or (n*k)%2 == 0:
        print("YES")
    else:
        print("NO")
        