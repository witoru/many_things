N, M = map(int, input().split())
arr = []
correctarr1 = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
correctarr2 = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]
for i in range(N):
    arr.append(input())
a = False
count1 = 0
count2 = 0
minimum = 0
for i in range(N-7):
    for j in range(M-7):
        for k in range(8):
            for l in range(8):
                if arr[i+k][j+l] != correctarr1[k][l]:
                    count1 += 1
                if arr[i+k][j+l] != correctarr2[k][l]:
                    count2 += 1
        if a == False:
            a = True
            minimum = count1
        if minimum >= count1:
            minimum = count1
        if minimum >= count2:
            minimum = count2
        count1 = 0
        count2 = 0

print(minimum)
