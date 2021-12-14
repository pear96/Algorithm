import sys

board = sys.stdin.readline().rstrip()
board_len = len(board)
answer = ''
count = 0

for idx in range(board_len):
    if board[idx] == 'X':
        count += 1
        if count == 4:
            answer += 'A' * 4
            count = 0
        if idx == board_len - 1:
            if count == 2:
                answer += 'B' * 2
                count = 0
            elif count % 2:
                answer = -1
                break
    else:
        if count == 4:
            answer += 'A' * 4
            count = 0
        elif count == 2:
            answer += 'B' * 2
            count = 0
        elif count % 2:
            answer = -1
            break
        answer += '.'

print(answer)

