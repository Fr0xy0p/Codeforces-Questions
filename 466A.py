#problem done and submitted
n,m,a,b = map(int,input().split())
if m * a > b:
    fees = (n//m)*b + min((n%m)*a,b) 
else:
    fees = n*a
print(fees)
