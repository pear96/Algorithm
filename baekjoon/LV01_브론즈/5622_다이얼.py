word = input()
answer = 0

for char in word:
    if ord('P') <= ord(char) <= ord('S'):
        number = 8
    elif ord('T') <= ord(char) <= ord('V'):
        number = 9
    elif ord('W') <= ord(char) <= ord('Z'):
        number = 10
    else:
        number = ((ord(char) - 65) // 3) + 3
    answer += number

print(answer)