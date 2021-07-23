"""
H-Index
https://programmers.co.kr/learn/courses/30/lessons/42747

"""


citations = [10, 9]
citations.sort(reverse=True)
answer = 0
count = 0
index = 0

print(citations)


for index in range(citations[0], 0, -1):
    if count <= index:
        print(f'{index} 차례 , count 초기화')
        count = 0
        print(f'{index}보다 모인 갯수 {count}가 적다.')
        for i in range(len(citations)):
            print(f'비교대상 : {citations[i]}, count : {count}')
            if index <= citations[i]:  # 비교값과 현재 값이 같다.
                print(f'{index}과 {citations[i]}이 같거나 크다.')
                count += 1  # 갯수 늘림.
                print(f'count : {count}')
                if count == index:  # 10의 값과 같은게 10개가 되었다.
                    print(
                        f'count : {count}와 현재 값 : {index}이 같다. H index를 찾았다.')
                    answer = index  # 지금 값이 h 인덱스가 됨
                    break
            else:
                print(
                    f'{index}보다 비교대상 {citations[i]}이 적다.j반복 탈출.')
                break
    else:
        break


print(answer)
