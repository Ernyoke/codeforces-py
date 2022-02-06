import sys

input = sys.stdin.readline
MAX = sys.maxsize

sys.setrecursionlimit(10 ** 9)


# Input functions
def inp():
    return int(input())


def read_int_list():
    return list(map(int, input().split()))


def read_list():
    s = input()
    return list(s[:len(s) - 1])


def read_int_map():
    return map(int, input().split())


# Solution
def solve(a):
    ans = 0
    if len(a) == 1:
        return ans

    n = len(a) - 1
    i = n - 1
    while i >= 0:
        if a[i] == a[n]:
            i -= 1
        else:
            ans += 1
            i -= (n - i)

    return ans


if __name__ == "__main__":
    for _ in range(inp()):
        print(solve(read_int_list()))
