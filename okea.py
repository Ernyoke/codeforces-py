# https://codeforces.com/problemset/problem/1634/C

import sys
from math import ceil

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
def solve(n, k):
    x = 1
    ans = []
    is_ans = True
    for i in range(0, n):
        if not is_ans:
            break
        x = 2 if int(ceil(n / 2)) == i else x
        ans.append([])
        for j in range(0, k):
            ans[i].append(x)
            if x > n * k:
                is_ans = False
                break
            x += 2

    print("YES" if is_ans else "NO")
    if is_ans:
        for line in ans:
            print(*line)


if __name__ == "__main__":
    for _ in range(inp()):
        solve(*read_int_list())
