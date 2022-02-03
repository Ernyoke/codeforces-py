# https://codeforces.com/contest/1633/problem/C

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
def compute_number_hits(dmg, armor):
    return int(ceil(armor / dmg))


def is_dead(hc, dc, hm, dm):
    die = compute_number_hits(dm, hc)
    hits = compute_number_hits(dc, hm)
    return hits <= die


def solve(hc, dc, hm, dm, coins, weapon, armor):
    if is_dead(hc, dc, hm, dm):
        return "YES"

    for spent in range(coins):
        if is_dead(hc + (coins - spent) * armor, dc + spent * weapon, hm, dm):
            return "YES"

        if is_dead(hc + spent * armor, dc + (coins - spent) * weapon, hm, dm):
            return "YES"

    return "NO"


if __name__ == "__main__":
    for _ in range(inp()):
        hc, dc = read_int_list()
        hm, dm = read_int_list()
        k, w, a = read_int_list()
        print(solve(hc, dc, hm, dm, k, w, a))
