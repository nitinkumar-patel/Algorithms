"""
Recursion Rules:

1. Identify the base case
2. Identify the recursive case
3. Get closer and closer and returns when needed.
    Usually you have 2 returns.


Factorial

5! = 5 * 4 * 3 * 2 * 1
5! = 5 * 4!
5! = 5 * 4 * 3!
5! = 5 * 4 * 3 * 2!
5! = 5 * 4 * 3 * 2! * 1!

n! = n * (n-1)!
"""


def find_factorial_recursive(number):
    if number < 2:
        return number
    return number * find_factorial_recursive(number - 1)


def find_factorial_iterative(number):
    ans = 1
    for i in range(2, number+1):
        ans *= i
    return ans


if __name__ == '__main__':
    find_factorial_iterative(1)  # 1
    find_factorial_iterative(2)  # 2
    find_factorial_iterative(5)  # 120
    find_factorial_iterative(10)  # 3628800

    find_factorial_recursive(1)  # 1
    find_factorial_recursive(2)  # 2
    find_factorial_recursive(5)  # 120
    find_factorial_recursive(10)  # 3628800
