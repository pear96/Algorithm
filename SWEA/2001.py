"""
2001: 파리퇴치
"""
from pprint import pprint
import sys
sys.stdin = open('2001_input.txt')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    # print(test_case, n, m)
    array = [input().split() for _ in range(n)]
    m_sums = []
    # pprint(array)

    for n_horizon in range(n-m+1):
        for n_vertical in range(n-m+1):
            m_set = 0
            for m_horizon in range(n_horizon, m + n_horizon):
                for m_vertical in range(n_vertical, m + n_vertical):
                    m_set += int(array[m_horizon][m_vertical])
            m_sums.append(m_set)
    print('#{} {}'.format(test_case, max(m_sums)))
