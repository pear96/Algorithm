nums = []

for _ in range(9):
    num = int(input())
    nums.append(num)

max_idx = 0

for i in range(9):
    if nums[max_idx] < nums[i]:
        max_idx = i

print(nums[max_idx])
print(max_idx+1)

