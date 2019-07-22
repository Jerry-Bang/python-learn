
"""
骆昊版：

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

"""


def find_armstrong_number(lower=100, upper=999):

    rlt = []
    elm = lower
    while elm <= upper:
        high = elm // 100
        middle = (elm % 100)//10
        low = elm % 10
        if high**3 + middle**3 + low**3 == elm:
            rlt.append(elm)
        elm += 1

    return rlt

