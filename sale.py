import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


if __name__ == "__main__":
    n, m = read()
    prices = sorted(read())

    res = 0
    for i in range(0, m):
        if prices[i] < 0:
            res += prices[i]

    print(-res)

