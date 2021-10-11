# https://www.acmicpc.net/problem/10809
S = input()
count = 0
alpha = 'abcdefghijklmnopqrstuvwxyz'
pr = [-1 for i in range(26)]
for i in S:
    for j in range(26):
        if i == alpha[j]:
            if pr[j] == -1:
                pr[j] = count
    count += 1
for i in pr:
    print(i, end = ' ')