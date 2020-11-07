"""
The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers,
starting with 0, and 1.
The Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
"""


def fibonacci_iterative(n):  # O(n)
    l = [0, 1]
    for i in range(2, n+1):
        l.append(l[i-1] + l[i-2])
    return l[n]


def fibonacci_recursive(n):  # O(2^n)
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


if __name__=='__main__':
    print(fibonacci_iterative(0))  # 0
    print(fibonacci_iterative(2))  # 1
    print(fibonacci_iterative(8))  # 21

    print(fibonacci_recursive(0))  # 0
    print(fibonacci_recursive(2))  # 1
    print(fibonacci_recursive(8))  # 21
