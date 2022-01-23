# https://codeforces.com/contest/1629/problem/B
import sys

input = sys.stdin.readline


# Input functions
def inp():
    return int(input())


def read_int_list():
    return list(map(int, input().split()))


def solve(l, r, k):
    if l == r:
        return "NO" if l == 1 else "YES"
    diff = (r - l + 1) - (r // 2 - (l - 1) // 2)
    return "YES" if diff <= k else "NO"


if __name__ == "__main__":
    for _ in range(inp()):
        l, r, k = read_int_list()
        print(solve(l, r, k))
