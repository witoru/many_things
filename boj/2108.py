N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

avg = 0

for i in arr:
    avg += i

avg = round(avg / N)

mid = arr[N//2]

count = 1

freq = [1, []]

for i in range(N-1):
    if arr[i] != arr[i+1]:
        if count > freq[0]:
            freq[0] = count
            freq[1] = [arr[i]]
        elif count == freq[0]:
            freq[1].append(arr[i])
        count = 1
    else:
        count += 1

if count > freq[0]:
    freq[0] = count
    freq[1] = [arr[len(arr) - 1]]

elif freq[0] == count:
    freq[1].append(arr[len(arr)-1])

if len(freq[1]) > 1:
    freq[1] = [sorted(freq[1])[1]]

ran = max(arr) - min(arr)

print(avg)
print(mid)
print(freq[1][0])
print(ran)