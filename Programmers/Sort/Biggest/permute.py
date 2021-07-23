# 1. a,b,c 조합 구현하기 = 순열구하는 함수 있어서 개빡치지만... 일단 함수 구현 연습하자.

numbers = [3, 30, 34, 5, 9]
str_nums = list(map(str, numbers))

"""
def permute(arr):
    result = [arr[:]]
    print(f'result : {result}')
    c = [0] * len(arr)
    print(f'c : {c}')
    i = 0
    while i < len(arr):
        print(f'c[i] :{c[i]} , i : {i}')
        if c[i] < i:
            if i % 2 == 0:
                print(f'i : {i}, arr[0] : {arr[0]} , arr[i] : {arr[i]}')
                arr[0], arr[i] = arr[i], arr[0]
            else:
                print(f'i : {i} , arr[c[i]] : {arr[c[i]]}, arr[i] :  {arr[i]}')
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            print(f'result : {result}')
            c[i] += 1
            print(f'c[i] : {c[i]}')
            i = 0
        else:
            c[i] = 0
            i += 1
            print(f'i : {i}')
    return result
"""


def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result


print(permute(str_nums))
