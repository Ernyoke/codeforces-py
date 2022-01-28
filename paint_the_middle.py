# https://codeforces.com/contest/1630/problem/C

import sys
from collections import defaultdict

input = sys.stdin.readline
MAX = sys.maxsize

sys.setrecursionlimit(10 ** 9)


# Input functions
def inp():
    return int(input())


def read_int_list():
    return list(map(int, input().split()))


def read_list():
    s = input()
    return list(s[:len(s) - 1])


def read_int_map():
    return map(int, input().split())


# Solution
def solve(colors):
    idx_map = defaultdict(list)
    for idx, color in enumerate(colors):
        idx_map[color].append(idx)

    segments = []
    for key, value in idx_map.items():
        if len(value) >= 2:
            segments.append((value[0], value[-1]))

    segments.sort()

    i = 0
    groups = []
    while i < len(segments):
        s = segments[i]
        j = i + 1
        group = []
        next_s = s
        while j < len(segments):
            next_s = segments[j]
            if s[0] == next_s[0]:
                if next_s[1] > s[1]:
                    s = next_s
            elif s[0] < next_s[0] < s[1] < next_s[1]:
                group.append(s)
                s = next_s
            elif s[1] < next_s[0]:
                break
            j += 1
        group.append(s)
        if j == len(segments):
            group.append(next_s)
        groups.append(group)
        i = j

    res = 0
    for g in groups:
        if len(g) == 1:
            s = g[0]
            res += max(0, s[1] - s[0] - 1)
        else:
            s1 = g[0]
            s2 = g[-1]
            res += max(0, s2[1] - s1[0] - 1)

    return res


if __name__ == "__main__":
    inp()
    c = read_int_list()
    print(solve(c))
