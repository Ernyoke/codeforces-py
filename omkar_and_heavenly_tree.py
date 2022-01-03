import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().split()))


def solve(n, restrictions):
    mid = 0
    b = set(b for (_, b, _) in restrictions)
    for i in range(1, n + 1):
        if i not in b:
            mid = i
            break
    for i in range(1, n + 1):
        if i != mid:
            print(i, mid)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = read()
        restrictions = []
        for _ in range(m):
            restrictions.append(tuple(read()))
        solve(n, restrictions)
