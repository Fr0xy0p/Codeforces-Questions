#problem done and submitted
import math
t = int(input())
for i in range(1,t+1):
    n = int(input())
    a = list(map(int,input().split()))

    print(math.gcd(a[0],a[-1]))