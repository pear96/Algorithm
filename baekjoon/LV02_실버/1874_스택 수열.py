import sys

N = int(sys.stdin.readline().rstrip())

idx = 0
stack = []
result = []
possible = True

for i in range(0, N):
    goal = int(sys.stdin.readline().rstrip())

    while idx < goal:
        idx += 1
        stack.append(idx)
        result.append('+')

    # 애초에 위에서부터 다시 비교할 필요가 없었네
    # 한 숫자를 보고있으면 걔랑 되나 안되나만 증가시키면서 보는거야.
    # exit(0)로 빠져나오려고했는데 틀리더라
    if stack[-1] == goal:
        # pop을 먼저 하고 그 숫자와 goal을 비교했는데 거기서부터 문제였을지도...
        stack.pop()
        result.append('-')
    else:
        possible = False
        break


if possible:
    for answer in result:
        print(answer)
else:
    print('NO')