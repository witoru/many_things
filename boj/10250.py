T = int(input())
arr = []
answer = []
for _ in range(T):
    arr.append(list(map(int, input().split())))
for ar in arr:
    wid = (ar[2] // ar[0]) + 1
    hei = ar[2] % ar[0]
    if hei == 0:
        answer.append(ar[0]*100 + wid - 1)
    else:
        answer.append(hei*100 + wid)
for i in answer:
    print(i)