#problem done and submitted
n = int(input())
for x in range(1, n + 1):
    a, b, c = map(int, input().split())
    m = max(a, b, c)
    ansa = 0
    ansb = 0
    ansc = 0

    if m == a:
        if m == b:
            ansa = 1
            ansb = 1
        else:
            ansb = a - b + 1
            
        if m == c:
            ansa = 1
            ansc = 1
        else:
            ansc = a - c + 1
            
    elif m == b:
        ansa = b - a + 1
        if c == m:
            ansc = 1
            ansb = 1 # FIXED: Tied with c, so b also needs 1 extra vote
        else:
             ansc = b - c + 1
             ansb = 0 # Strict max, b needs 0
            
    else:
        ansc = 0
        ansb = c - b + 1 # FIXED: Reversed to avoid negative numbers
        ansa = c - a + 1

    print(ansa, ansb, ansc)