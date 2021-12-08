import sys
N, M = map(int, sys.stdin.readline().split())
book_num = {}
book_str = {}

for i in range(1, N+1):
    book_num[i] = sys.stdin.readline().rstrip()
    book_str[book_num.get(i)] = i

for _ in range(M):
    quiz = sys.stdin.readline().rstrip()
    if quiz[0].isupper():
        print(book_str.get(quiz))
    else:
        print(book_num.get(int(quiz)))