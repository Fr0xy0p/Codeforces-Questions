n,m,a,b = map(int,input().split())

if m *b <= n*a:
    ans = (n//m)*b + (n%m)*a

else:
    ans = n*a

print(ans)