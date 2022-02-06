# https://codeforces.com/contest/1529/problem/D

import sys

input = sys.stdin.readline
MAX = sys.maxsize

# sys.setrecursionlimit(10 ** 9)


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
X = 998244353


def solve(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            dp[j] += 1

    pref = 1
    for i in range(1, n + 1):
        dp[i] = (dp[i] + pref) % X
        pref = (dp[i] + pref) % X

    return dp[n]


if __name__ == "__main__":
    print(solve(inp()))
