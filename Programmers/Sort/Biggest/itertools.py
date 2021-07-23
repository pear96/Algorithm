# 이 문제를 풀기 위해 두 가지의 방법이 있다고 생각한다.
# 하나는 a,b,c 조합을 구현하는 것이고 다른 하나는 45,4,443의 비교 로직을 구현하는 것이다.
# 우선 둘 다 도전해 보기로 하자.

# 1. a,b,c 조합 구현하기 시간초과 당함 ㅅㅂ
import itertools


numbers = [3, 30, 34, 5, 9]


str_numbers = list(map(str, numbers))
num_comb = list(map(''.join, itertools.permutations(str_numbers)))

num_comb.sort()

print(num_comb[len(num_comb)-1])
