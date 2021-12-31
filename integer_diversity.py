import sys
from collections import Counter

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


def solve(a):
    unique = set()
    for value in a:
        if value == 0:
            unique.add(value)
        elif value not in unique:
            unique.add(value)
        else:
            unique.add(-value)
    return len(unique)


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        m = int(input())
        a = read()
        print(solve(a))
