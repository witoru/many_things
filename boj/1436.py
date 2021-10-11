N = int(input())
i = 0
arr1 = [666] 
count = False

while i < N:
    for j in range(len(str(arr1[i]))-2):
        if str(arr1[i])[j] == str(arr1[i])[j+1] == str(arr1[i])[j+2] == '6':
            count = True
            break
    if count == True:
        arr1.append(arr1[i])
        i += 1
        arr1[i] += 1
        count = False
    else:
        arr1[i] += 1

print(arr1[i-1])