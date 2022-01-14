import sys
from collections import Counter

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


def solve(counter):
    a = 0
    b = counter[1]
    for i in range(2, max(counter.keys()) + 1):
        a, b = b, max(b, counter[i] + a)

    return b


if __name__ == "__main__":
    input()
    counter = Counter()
    for i in read():
        counter[i] += i
    print(solve(counter))

