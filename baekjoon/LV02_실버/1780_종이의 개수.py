import sys

N = int(sys.stdin.readline().rstrip())
MAP = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
ans = [0, 0, 0]


def check(size, row_s, row_e, col_s, col_e):
    cnt0, cnt1, cnt_1 = 0, 0, 0

    for row in range(row_s, row_e):
        for col in range(col_s, col_e):
            if MAP[row][col] == 0:
                cnt0 += 1
            elif MAP[row][col] == 1:
                cnt1 += 1
            else:
                cnt_1 += 1

    if cnt0 == size * size:
        ans[0] += 1
    elif cnt1 == size * size:
        ans[1] += 1
    elif cnt_1 == size * size:
        ans[-1] += 1
    else:
        # 3 * 3인데 한 장을 못 만들었으면 어짜피 9개씩 나눠서 한장씩 봐야하고 그건 지금의 cnt를 저장하는거랑 같은 행위
        if size == 3:
            ans[-1] += cnt_1
            ans[0] += cnt0
            ans[1] += cnt1
            return
        size_3 = size // 3
        for r_step in range(row_s, row_e, size_3):
            for c_step in range(col_s, col_e, size_3):
                check(size_3, r_step, r_step + size_3, c_step, c_step + size_3)



check(N, 0, N, 0, N)
print(ans[-1])
print(ans[0])
print(ans[1])