import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


if __name__ == "__main__":
    n = int(input())
    for i in range(0, n):
        m = int(input())
        buildings = read()
        print(0 if sum(buildings) % len(buildings) == 0 else 1)

