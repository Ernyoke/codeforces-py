# https://codeforces.com/problemset/problem/1612/C

import sys

input = sys.stdin.readline


def read_int_list():
    return list(map(int, input().split()))


def bin_search(x, n):
    low, up = 0, 2 * x - 1
    while low < up:
        mid = (up - low) // 2 + low
        if mid > x:
            res = x * (x + 1) - x - (x - 1 - mid + x) * (2 * x - mid) // 2
        else:
            res = mid * (mid + 1) // 2
        if res >= n:
            up = mid
        else:
            low = mid + 1
    return up


if __name__ == "__main__":
    for _ in range(int(input())):
        print(bin_search(*read_int_list()))
