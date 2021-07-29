"""
주식가격
https://programmers.co.kr/learn/courses/30/lessons/42584

'나'보다 뒤에 작은애가
1. 있다 => 거기까지의 거리차
2. 없다 => 끝까지의 거리차

이건 스택도 큐도 아닌 것 같은데 뭐지? 뭘 놓치고 있는거지?

"""


def solution(prices):
    answer = []

    for i in range(len(prices)):
        if i == len(prices)-1:
            answer.append(0)
            break

        for j in range(i+1, len(prices)):
            rests = prices[j:]
            if prices[i] < min(rests):
                answer.append(len(prices)-1-i)
                break

            if prices[i] > prices[j] or j == (len(prices)-1):
                answer.append(j-i)
                break

    return answer


prices = [1, 2, 3, 2, 3, 1]
solution(prices)
