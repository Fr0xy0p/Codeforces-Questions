#problem done and submitted
n,m,a = map(int,input().split())
if n%a!=0 and m%a == 0:
    b = n//a +1
    c = m//a
    d = b*c
elif n%a ==0 and m%a!=0:
    b = n//a
    c = m//a +1
    d = b*c
elif n%a ==0 and m%a == 0:
    b = n//a
    c = m//a 
    d = b*c 
else:
    b= n//a +1
    c = m//a +1
    d = b*c
print(d)