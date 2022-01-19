import sys

N, M = map(int, sys.stdin.readline().split())
un_seen = set()
un_heard = set()
un_seen_heard = list()

for _ in range(N):
    un_seen.add(sys.stdin.readline().rstrip())

for _ in range(M):
    un_heard.add(sys.stdin.readline().rstrip())

for _ in range(N):
    person = un_seen.pop()
    if person in un_heard:
        un_seen_heard.append(person)

print(len(un_seen_heard))
un_seen_heard.sort()

for person in un_seen_heard:
    print(person)