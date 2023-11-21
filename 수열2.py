N = int(input())
nums = list(map(int, input().split()))
temp = 0
result = 0

sortednums = [(value, index) for index, value in enumerate(nums)]

for i in range(len(sortednums)):
    value, index = sortednums[i]
    if i == len(sortednums)-1:
        continue
    elif sortednums[i+1][0] - sortednums[i][0] > temp:
        temp = sortednums[i+1][0] - sortednums[i][0]
        result = [index]

print(*result)
