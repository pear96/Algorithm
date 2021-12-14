"""
밑의 주석이 내가 원래 만들었던 코드인데
KMP로 안풀고 리스트로 푼건 잘 했는데
한번에 넘어가려고 했던게 오히려 너무 많이 조회해서
더 시간을 많이 잡아먹었던 것 같아.
1. 여러개를 넘어가려면 우선 in 에서 bomb_len만큼 조회하고
2. 아니면 또 bomb_len 만큼 조회하면서 몇개를 넘어갈지 조회하고

결과에 하나씩 더해가는건 괜찮은 생각이었는데 초반에 떠올리고
별로인가 싶어서 넘어간게 아쉽다.
"""


import sys
words = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
answer = []

for i in range(len(words)):
    answer.append(words[i])

    if len(answer) >= len(bomb):
        sentence = ''.join(answer[-len(bomb):])
        if sentence == bomb:
            cnt = 0
            while cnt < len(bomb):
                answer.pop()
                cnt += 1
if len(answer):
    print(''.join(answer))
else:
    print('FRULA')



# import sys
# words = list(sys.stdin.readline().rstrip())
# bomb = sys.stdin.readline().rstrip()
# bomb_len = len(bomb)
#
# while bomb in ''.join(words):
#     idx = 0
#     while idx + bomb_len <= len(words):
#         jump_idx = 0
#         if bomb[0] in words[idx:idx+bomb_len]:
#             bomb_idx = 0
#             for words_idx in range(bomb_len):
#                 if bomb[bomb_idx] == words[idx + words_idx]:
#                     bomb_idx += 1
#                 else:
#                     jump_idx += 1
#             if jump_idx == 0:
#                 words[idx:idx+bomb_len] = ''
#         else:
#             jump_idx = bomb_len
#         idx += jump_idx
#
# answer = ''.join(words)
# if len(answer):
#     print(answer)
# else:
#     print('FRULA')