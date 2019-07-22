"""
骆昊 版：

import time
import math

for num in range(1, 10000):
    sum = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num / factor != factor:
                sum += num / factor
    if sum == num:
        print(num)

Jerry-Bang:
for 循环的写法比while 要简洁一些。
因为，
   1. y 要进行初始化
   2. 避免多次计算，引入mid的变量
"""

import math


def is_perfect(x):

    mid = int(math.sqrt(x))
    y = 1
    sum_of_factor = 0
    while y <= mid:
        if x % y == 0:
            sum_of_factor += y
            if 1 < y != x // y:
                sum_of_factor += x // y
        y += 1

    if sum_of_factor == x:
        return True
    else:
        return False


def find_perfect_number(lower=1, upper=0xffff):

    rlt = []
    elm = lower
    while elm <= upper:
        if is_perfect(elm):
            rlt.append(elm)
        elm += 1

    return rlt


if __name__ == "__main__":
    rlt = find_perfect_number()
    for elm in rlt:
        print(elm)
