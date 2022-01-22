# https://codeforces.com/contest/1621/problem/B

import sys

input = sys.stdin.readline
MAX = sys.maxsize


# Input functions
def inp():
    return int(input())


def read_int_list():
    return list(map(int, input().split()))


def solve(segments):
    first, last = MAX, -1
    first_cost, last_cost = MAX, MAX
    tmp = MAX
    for s in segments:
        (l, r), c = s
        if first > l:
            tmp = MAX
            first = l
            first_cost = c
        elif first == l and first_cost > c:
            first_cost = c

        if last < r:
            tmp = MAX
            last = r
            last_cost = c
        elif last == r and last_cost > c:
            last_cost = c

        if first == l and last == r:
            tmp = min(tmp, c)

        print(min(first_cost + last_cost, tmp))


if __name__ == "__main__":
    for _ in range(inp()):
        s = list()
        for _ in range(inp()):
            l, r, c = read_int_list()
            s.append(((l, r), c))
        solve(s)
