import sys

T = int(sys.stdin.readline().rstrip())

for tc in range(T):
    alphabet = [[] for _ in range(26)]
    W = sys.stdin.readline().rstrip()
    K = int(sys.stdin.readline().rstrip())
    sentences = []

    for idx in range(len(W)):
        alphabet[ord(W[idx]) - ord('a')].append(idx)


    # 짧은 문자열 찾기
    min_len = 987654321
    max_len = 0
    # 문자열 자체도 찾아야 하는 줄 알았어..
    # min_idx_start, min_idx_end = 0, 0
    # max_idx_start, max_idx_end = 0, 0
    no_exist = True

    for char in alphabet:
        # 해당 알파벳이 K개 이상 나왔는지 본다.
        if len(char) >= K:
            # -1을 출력할 필요는 없다.
            no_exist = False
            # 가장 짧은, 가장 긴 문자열을 찾아야한다. (2개씩 짝지어서 비교)
            # 등호를 빼면 틀린다....
            for idx in range(len(char) - K + 1):
                if char[idx + K - 1] - char[idx] < min_len:
                    min_len = char[idx + K - 1] - char[idx]
                if char[idx + K - 1] - char[idx] > max_len:
                    max_len = char[idx + K - 1] - char[idx]

    if no_exist:
        print(-1)
    else:
        print(min_len + 1, max_len + 1)
