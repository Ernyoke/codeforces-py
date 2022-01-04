import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().split()))


def solve(n, a, b):
    if abs(a - b) > 1 or n - a - b < 2:
        return [-1]
    res = [i for i in range(1, n + 1)]
    if a > b:
        for i in range(0, 2 * a, 2):
            res[n - i - 1], res[n - i - 2] = res[n - i - 2], res[n - i - 1]
    elif b > a:
        for i in range(0, 2 * b, 2):
            res[i], res[i + 1] = res[i + 1], res[i]
    elif a == b:
        for i in range(0, 2 * a, 2):
            res[i + 1], res[i + 2] = res[i + 2], res[i + 1]
    return res


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, a, b = read()
        print(*solve(n, a, b))
