import sys

N = int(sys.stdin.readline().rstrip())

stars = [[' '] * N for _ in range(N)]


def star(num):
    if num == 3:
        stars[0][:3] = stars[2][:3] = '*'*3
        stars[1][:3] = '* *'
        return

    now = num//3
    star(now)

    for row in range(3):
        for col in range(3):
            # 중앙은 비워둠
            if row == 1 and col == 1:
                continue
            for k in range(now):
                # 왼쪽 줄의 3칸씩 복사해옴
                stars[now*row+k][now*col:now*(col+1)] = stars[k][:now]


star(N)

for i in range(N):
    for j in range(N):
        # 다 만들고 나서 출력함
        print(stars[i][j], end='')
    print()