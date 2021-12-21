def s(a):
    r = []
    if a == 1:
        return '*'
    else:
        a = s(a//3).split('\n')
        r = []
        for i in a:
            r.append(i*3)
        for i in a:
            r.append(i+' '*len(a)+i)
        for i in a:
            r.append(i*3)
        return '\n'.join(r)
n = int(input())
print(s(n))
"""
뭐임 이해 안가...
"""