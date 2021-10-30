n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
dic = {}
answer = []
for i in arr1:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1

for i in arr2:
    if i in dic:
        answer.append(dic[i])
    else:
        answer.append(0)

for i in answer:
    print(i, end = " ")