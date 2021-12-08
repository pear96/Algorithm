S = input()
alphabet = [-1] * 26
# 알파벳 받은거 ord로 숫자화해서 97만큼 빼서 0~25로 알파벳 확인한다.

for idx in range(len(S)):
    char = S[idx] # 현재 보고있는 문자가
    alphabet_idx = ord(char) - 97 # 몇번째 알파벳인지 찾고
    if alphabet[alphabet_idx] == -1: # 한번도 온 적이 없다면
        alphabet[alphabet_idx] = idx # 지금 위치를 저장한다.

print(' '.join(map(str, alphabet)))