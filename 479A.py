a = int(input())
b = int(input())
c = int(input())
ans = 0
p = a+b*c
q = a*(b+c)
r = a*b*c
s = (a+b)*c
t = a+b+c
ans = max(p,q,r,s,t)
print(ans)