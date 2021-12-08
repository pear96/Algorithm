# replace 활용가능

T = int(input())

for tc in range(T):
    words = input()
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    cnt = 0  # 총 알파벳의 개수
    croatia_exist = 0  # 크로아티아가 있다면 한 글자씩 계산하지 않으려고

    while len(words) >= 2:  # 크로아티아 문자는 전부 2글자 이상이므로 1글자라면 검사할 이유가 없다.
        check = words[:2]  # 우선 두 글자만 잘라내본다.
        for alphabet in croatia:
            if check == 'dz':  # 유일한 3자리인 dz를 특수하게 검사하기 위함이다.
                if len(words) >= 3 and words[:3] == 'dz=':
                    words = words[3:]
                    cnt += 1
                    croatia_exist = 1
                break  # dz이긴 한데 dz=가 아니라면 alphabet 순회를 끝내버린다.
            elif check == alphabet:  # 그 외의 2글자 크로아티아 알파벳인 경우
                words = words[2:]
                cnt += 1
                croatia_exist = 1
                break  # 한번 맞았으면 됐다
        if not croatia_exist:  # 만약 2글자가 크로아티아 문자가 아니었을 경우
            words = words[1:]  # 한 글자씩 자른다.
            cnt += 1
        croatia_exist = 0  # 다음에 또 한글자인 경우를 위해 크로아티아 문자의 존재 유무를 초기화한다.

    if len(words) == 1:
        cnt += 1
    print(cnt)