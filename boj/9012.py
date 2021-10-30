N = int(input())
arr = []
count = 0
ans = []
boo = True

for _ in range(N):
    arr.append(input())

for str in arr:
    for ch in str:
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1
        if count < 0:
            ans.append("NO")
            boo = False 
            break
    if boo == True:
        if count == 0:
            ans.append("YES")
        else:
            ans.append("NO")
    boo = True
    count = 0

for s in ans:
    print(s)