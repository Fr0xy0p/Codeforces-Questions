#problem done and submitted
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2,35):
        factor = (2**i-1)
        if factor > n:
            break
        if n% factor == 0:
            print(n//factor)
            break
        
