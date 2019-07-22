
"""
骆昊 版本： 很简洁，nice
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
"""


def fibonacci(number_n):
    if number_n == 1:
        return 1
    elif number_n == 2:
        return 1
    else:
        return fibonacci(number_n-1) + fibonacci(number_n-2)


def fibonacci_list(num):
    if num == 1:
        return [1, ]
    elif num == 2:
        return [1, 1, ]
    else:
        rlt = fibonacci_list(num-1)
        rlt.append(rlt[-1] + rlt[-2])
        return rlt


if __name__ == "__main__":
    rlt = fibonacci_list(20)
    for elm in rlt:
        print(elm, end=" ")



