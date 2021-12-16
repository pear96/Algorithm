import sys

T = int(sys.stdin.readline().rstrip())

for tc in range(T):
    sentence = sys.stdin.readline().rstrip()
    result = 0
    answer = ''

    for char in sentence:
        if char == '(':
            result += 1
        else:
            if result <= 0:
                # 이미 여는 괄호가 없는데 또 닫는 괄호가 나온다면 답이 아니다.
                result = -1
                break
            result -= 1

    if result:
        print('NO')
    else:
        print('YES')