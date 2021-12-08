L, C = map(int, input().split())
chars = list(input().split())
chars.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
last_index = C - L + 1
starts = chars[:last_index]


def dfs(string, vowel, consonant):
    # 기저조건
    if len(string) == L:
        if vowel > 0 and consonant > 1 :
            print(string)
        return

    # 다음 문자를 추가할지 말지 결정하기
    now = string[-1]
    for index in range(vowel+consonant,C):
        next = chars[index]
        # 1. 알파벳 순서를 확인한다.
        if ord(now) >= ord(next):
            continue
        # 2. 얘부터 4문자를 만들 수 없으면 끝내버려
        if len(string)+len(chars[index:]) < L:
            return
        # 다음 문자 추가하기
        if next in vowels:
            dfs(string+next, vowel+1, consonant)
        else:
            dfs(string+next, vowel, consonant+1)


for start in starts:
    if start in vowels:
        dfs(start, 1, 0)
    else:
        dfs(start, 0, 1)