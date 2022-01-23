# https://codeforces.com/contest/1628/problem/B

import sys
from collections import Counter

input = sys.stdin.readline


# Input functions
def inp():
    return int(input())


def read_str():
    return input().strip()


def solve(words):
    s = set(words)
    for w in s:
        if len(w) == 1 or w == w[::-1] or w[::-1] in s:
            return "YES"

    aux_3 = Counter()
    aux_2 = Counter()
    for w in words:
        if len(w) == 3:
            aux_3[w[1:][::-1]] += 1
        if len(w) == 2:
            aux_2[w[::-1]] += 1

    for w in words:
        if len(w) == 2:
            aux_2[w[::-1]] -= 1
            if w in aux_3 and aux_3[w] > 0:
                return "YES"
        if len(w) == 3:
            aux_3[w[1:][::-1]] -= 1
            aux_w = w[:-1]
            if aux_w in aux_2 and aux_2[aux_w] > 0:
                return "YES"

    return "NO"


if __name__ == "__main__":
    for _ in range(inp()):
        words = []
        for _ in range(inp()):
            words.append(read_str())
        print(solve(words))
