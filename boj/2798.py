N, M = map(int,input().split())
arr = list(map(int, input().split()))
x = 0
y = 1
z = 1
Sum = 0
for i in arr[x:]:
    for j in arr[x+y:]:
        for k in arr[x+y+z:]:
            if ((i+j+k) > Sum) and ((i+j+k) <= M):
                Sum = i+j+k
        y += 1 
    y = 1    
    x += 1
print(Sum)