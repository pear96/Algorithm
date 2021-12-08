import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
visited = [0] * N
num_set = []

def dfs(count, N, M):
    if count == M:
        print(''.join(map(str, num_set)))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            num_set.append(nums[i])
            dfs(count+1, N, M)
            num_set.pop()
            visited[i] = 0


dfs(0, N, M)