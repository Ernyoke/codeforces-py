import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


if __name__ == "__main__":
    n = int(input())
    x = set(read()[1:])
    y = set(read()[1:])

    print("I become the guy." if sum(x.union(y)) == n * (n + 1) / 2 else "Oh, my keyboard!")
