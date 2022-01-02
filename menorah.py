import sys

input = sys.stdin.readline


def read_strs():
    s = input().strip()
    return list(map(int, list(s)))


def solve(a, b):
    x, y, diff = 0, 0, 0
    n = len(a)
    result = n + 1
    for i in range(n):
        x += a[i]
        y += b[i]
        diff += 1 if a[i] != b[i] else 0

    if x == y:
        result = min(diff, result)
    if x == n - y + 1:
        result = min(n - diff, result)

    return result if result < n + 1 else -1


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        m = int(input())
        a = read_strs()
        b = read_strs()
        print(solve(a, b))