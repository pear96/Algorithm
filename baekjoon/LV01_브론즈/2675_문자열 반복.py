T = int(input())

for tc in range(T):
    R, S = input().split()
    result = ''

    for char in S:
        result += char * int(R)

    print(result)