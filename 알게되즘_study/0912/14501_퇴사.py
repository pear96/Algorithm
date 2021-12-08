import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
works = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_pay = 0

def dfs(day):
    global max_pay
    global pay_sum
    if day >= N:
        if max_pay < pay_sum:
            max_pay = pay_sum
    for i in range(day, N):
        next_day = day + works[i][0]
        if next_day + works[next_day][0] >= N:
            continue
        pay_sum += works[next_day][1]
        dfs(next_day)


for day in range(N):
    pay_sum = works[day][1]
    print(dfs(day))