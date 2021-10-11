# OX퀴즈
t = int(input())
arr = []
score = [0 for i in range(t)]
for i in range(t):
    arr.append(input())
    arr[i] = list(arr[i])

for i in range(t):
    for j in range(len(arr[i])):
        if arr[i][j] == 'O':
            if j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i][j-1] + 1
        
        elif arr[i][j] == 'X':
            arr[i][j] = 0
    
    for j in arr[i]:
        score[i] += j

for i in score:
    print(i)