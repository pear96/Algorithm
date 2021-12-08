string = input()
# A = 65, Z = 90, a = 97, z = 122
# 매번 ord하려다가 혹시 시간초과 날까봐...

# 등장횟수 저장 배열. 대소문자 구분 X
alphabet = [0] * 26

for char in string:  # 문자열의 한 글자씩 보면서
    index = ord(char)  # 글자의 숫자 index 찾기
    if 65 <= index <= 90:  # 대문자라면 -A
        alphabet[index - 65] += 1
    elif 97 <= index <= 122:  # 소문자라면 -a
        alphabet[index - 97] += 1

max_appear = 0  # 가장 많이 등장한 횟수
answer = ''  # 출력할 대문자
multi_max = False  # 혹시 가장 많이 등장한게 여러개인지

for idx in range(26):
    if max_appear < alphabet[idx]:  # 더 많이 등장한게 있다면
        max_appear = alphabet[idx]  # 최대값 바꾸고
        answer = chr(idx + 65)  # 대문자 출력이라
        multi_max = False  # 최대값 바뀌었으니까 최대값 여러개 아님
    elif max_appear == alphabet[idx]:  # 이미 있다면
        multi_max = True  # 최대값 여러개임

if multi_max:
    print('?')
else:
    print(answer)