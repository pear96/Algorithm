N = int(input())


def check_number(num):
    remainder = []
    while num > 0:
        remainder.append(num % 10)
        num //= 10

    diff = remainder[0] - remainder[1]
    for idx in range(1, len(remainder)-1):
        if remainder[idx] - remainder[idx + 1] != diff:
            return False
    return True

hansu_cnt = 0
for number in range(1, N+1):
    if number < 10:
        hansu_cnt += 1
    else:
        if check_number(number):
            hansu_cnt += 1


print(hansu_cnt)
