words = input()

while words != '.':
    answer = 'yes'
    stack = []
    for char in words:
        if char == ')':
            if len(stack) > 0:
                pre = stack.pop()
                if pre != '(':
                    answer = 'no'
                    break
            else:
                answer = 'no'
                break
        elif char == ']':
            if len(stack) > 0:
                pre = stack.pop()
                if pre != '[':
                    answer = 'no'
                    break
            else:
                answer = 'no'
                break
        elif char == '(' or char == '[':
            stack.append(char)
        elif char == '.':
            if len(stack):
                answer = 'no'

    print(answer)
    words = input()