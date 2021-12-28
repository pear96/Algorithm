import sys

while True:
    num = sys.stdin.readline().rstrip()
    if num == '0':
        break
    length = len(num)

    palindrome = True
    for idx in range(length//2):
        if num[idx] != num[length-1-idx]:
            palindrome = False
            break

    if palindrome:
        print('yes')
    else:
        print('no')