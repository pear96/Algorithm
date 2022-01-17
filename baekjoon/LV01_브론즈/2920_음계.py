nums = list(map(int, input().split()))

asc, desc, mix = 0, 0, 0

for idx in range(7):
    if nums[idx] < nums[idx+1]:
        asc += 1
    else:
        desc += 1

if asc == 7:
    print('ascending')
elif desc == 7:
    print('descending')
else:
    print('mixed')