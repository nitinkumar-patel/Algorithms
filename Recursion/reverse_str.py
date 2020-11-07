"""
Time complexity : O(n)
Space : O(1)
"""


def recursive_reverse(s, i=0):
    n = len(s)
    if i == n // 2:
        return

    s[i], s[n - i - 1] = s[n - i - 1], s[i]
    recursive_reverse(s, i + 1)


if __name__ == "__main__":
    s = "Nitin Patel"

    # converting string to list
    # because strings do not support
    # item assignment
    s = list(s)
    recursive_reverse(s)

    # converting list to string
    s = ''.join(s)
    print(s)
