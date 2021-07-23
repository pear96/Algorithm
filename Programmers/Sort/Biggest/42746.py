"""
가장 큰 수
https://programmers.co.kr/learn/courses/30/lessons/42746

이 문제를 풀기 위해 두 가지의 방법이 있다고 생각한다.
하나는 a,b,c 조합을 구현하는 것이고 다른 하나는 45,4,443의 비교 로직을 구현하는 것이다.
우선 둘 다 도전해 보기로 하자.

2. 비교 로직을 구현해야한다.
length = random.randrange(1, 15)
elements = [0]*length

for index in range(length):
    elements[index] = random.randrange(0, 1001)

"""

elements = [0, 0, 70]

numbers = list(map(str, elements))
numbers.sort(reverse=True)
print(numbers)
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i][0] != numbers[j][0]:
            break
        else:
            if len(numbers[i]) == len(numbers[j]):
                if int(numbers[i]) < int(numbers[j]):
                    numbers[i], numbers[j] = numbers[j], numbers[i]
            elif len(numbers[i]) < len(numbers[j]):
                if numbers[j] == '1000' and numbers[len(numbers)-1] == '0':
                    numbers[j], numbers[len(numbers) -
                                        2] = numbers[len(numbers)-2], numbers[j]
                elif numbers[j] == '1000' and numbers[len(numbers)-1] != '0':
                    numbers[j], numbers[len(numbers) -
                                        1] = numbers[len(numbers)-1], numbers[j]
                elif len(numbers[i]) == 1:
                    if len(numbers[j]) == 2:
                        temp = numbers[i][0]*2
                    elif len(numbers[j]) == 3:
                        temp = numbers[i][0]*3

                    if int(temp) < int(numbers[j]):
                        numbers[i], numbers[j] = numbers[j], numbers[i]
                elif len(numbers[i]) == 2:
                    temp = numbers[i]+numbers[i][0]
                    if int(temp) < int(numbers[j]) or (numbers[i][1] == 0 and numbers[j][0] == 0):
                        numbers[i], numbers[j] = numbers[j], numbers[i]
            else:
                if numbers[i] == '1000' and numbers[len(numbers)-1] == '0':
                    numbers[i], numbers[len(numbers) -
                                        2] = numbers[len(numbers)-2], numbers[i]
                elif numbers[i] == '1000' and numbers[len(numbers)-1] != '0':
                    numbers[i], numbers[len(numbers) -
                                        1] = numbers[len(numbers)-1], numbers[i]
                elif len(numbers[j]) == 1:
                    if len(numbers[i]) == 2:
                        temp = numbers[j][0]*2
                    elif len(numbers[i]) == 3:
                        temp = numbers[j][0]*3

                    if int(temp) > int(numbers[i]):
                        numbers[i], numbers[j] = numbers[j], numbers[i]
                elif len(numbers[j]) == 2:
                    temp = numbers[j]+numbers[j][0]
                    if int(temp) > int(numbers[i]) or (numbers[i][1] == 0 and numbers[j][0] == 0):
                        numbers[i], numbers[j] = numbers[j], numbers[i]


answer = ''.join(numbers)

if int(answer) == 0:
    answer = '0'

print(numbers)
print(answer)
