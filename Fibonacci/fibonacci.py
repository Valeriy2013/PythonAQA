"""
Fibonacci library.
"""


def generateFibonacci(n):
    result = [1]
    if n == 0:
        return 1
    elif n == 1:
        return result
    a = 0
    b = 1
    for i in range(0, n - 1):
        b = a + b
        a = b - a
        result.append(b)
    return result


def main():
    print(generateFibonacci(5))
    print(generateFibonacci(9))


print(main())
