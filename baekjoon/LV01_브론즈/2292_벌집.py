N = int(input())

idx, end_idx = 0, 0
while True:
    if N == 1:
        print(1)
        break
    if 6 * (end_idx - idx) + 2 <= N <= 6 * end_idx + 1:
        print(idx+1)
        break
    idx += 1
    end_idx += idx
