#problem done and submitted
n,k = map(int,input().split())
arr = list(map(int,input().split()))
seen = []
for i in range(len(arr)):
    if arr[i] >= arr[k-1] and arr[i] > 0:
        seen.append(arr[i])
    else:
        break
print(len(seen))

        