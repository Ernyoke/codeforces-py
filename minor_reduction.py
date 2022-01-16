# https://codeforces.com/contest/1626/problem/B

import sys

input = sys.stdin.readline


def read_int_list():
    return list(map(int, list(input().strip())))


def solve(a):
    pos = len(a) - 1
    for i in range(len(a) - 1, 0, -1):
        pos = i
        if a[i] + a[i - 1] > 9:
            break
    print(f'{"".join(map(str, a[:pos - 1]))}{a[pos] + a[pos - 1]}{"".join(map(str, a[pos + 1:]))}')


if __name__ == "__main__":
    for _ in range(int(input())):
        a = read_int_list()
        solve(a)
