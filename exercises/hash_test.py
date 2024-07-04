nums = [2, 7, 11, 15]
target = 4

numMap = {}
n = len(nums)

# Build the hash table
for i in range(n):
    numMap[nums[i]] = i

# Find the complement
for i in range(n):
    complement = target - nums[i]
    if complement in numMap and numMap[complement] != i:
        print([i, numMap[complement]])
        break
