import sys
sys.stdin = open('input.txt')

def dfs(days=0, profits=0):
    global max_pay
    if days > N:
        return
    if profits > max_pay:
        max_pay = profits

    if days < N:
        dfs(days+works[days][0], profits+works[days][1])
    dfs(days+1, profits)

N = int(sys.stdin.readline())
works = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_pay = 0
dfs()
print(max_pay)
