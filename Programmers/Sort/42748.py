"""
K번째 수
https://programmers.co.kr/learn/courses/30/lessons/42748

"""

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []

index = commands[0][0:2]
temp = array[index[0]-1:index[1]]
temp.sort()
answer.append(temp[commands[0][2]-1])

print(answer)
