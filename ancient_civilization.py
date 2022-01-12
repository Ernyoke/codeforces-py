import sys
from collections import Counter

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


def solve(x):
    binaries = [list(format(b, '#063b')) for b in x]
    res = []
    for i in range(63):
        counter = Counter()
        for b in binaries:
            counter[b[i]] += 1
        res.append(str(counter.most_common(1)[0][0]))
    return int("".join(res), 2)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, l = read()
        x = read()
        print(solve(x))