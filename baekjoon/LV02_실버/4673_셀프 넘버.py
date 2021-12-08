def generate(number):
    generated_number = number
    while number > 0:
        generated_number += number % 10
        number //= 10
    return generated_number


generated = [False] * 20000

num = 0
while num < 10001:
    num += 1
    if not generated[num]:
        print(num)
    not_self_number = generate(num)
    if not_self_number > 10001:
        continue
    generated[not_self_number] = True