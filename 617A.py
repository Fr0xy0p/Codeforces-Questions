#problem completed and submitted
x = int(input())
ans = 0 
if x%5 == 0:
    ans = x//5
else:
    ans = x//5 + 1
print(ans)