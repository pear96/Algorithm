"""
리스트를 만들어서 정렬하고 set로 만든다(중복제거)
그 set와 range(N)만큼의 인덱스를 enumerate하면
{ -10:0, -9:1, 2:2, 4:3 }
딕셔너리가 나오는데 여기서 value값이 내 앞에 작은 수들의 수와 같다...
"""

import sys
N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
set_nums = sorted(set(nums))
dict_nums = { idx:num for num, idx in enumerate(set_nums)}

for i in range(N):
    print(dict_nums[nums[i]], end=' ')