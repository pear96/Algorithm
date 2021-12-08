num1, num2 = input().split()
reverse_num1, reverse_num2 = '', ''
for i in range(3):
    reverse_num1 = num1[i] + reverse_num1
    reverse_num2 = num2[i] + reverse_num2

if int(reverse_num1) > int(reverse_num2):
    print(reverse_num1)
else:
    print(reverse_num2)