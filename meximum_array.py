# https://codeforces.com/contest/1628/problem/A

import sys

input = sys.stdin.readline
MAX = sys.maxsize

sys.setrecursionlimit(10 ** 9)


# Input functions
def inp():
    return int(input())


def read_int_list():
    return list(map(int, input().split()))


def find_mex(freq):
    for index, f in enumerate(freq):
        if f == 0:
            return index


def solve(a):
    freq = [0] * (len(a) + 1)
    for value in a:
        freq[value] += 1

    mex = find_mex(freq)

    res = [mex]
    i = 0
    while i < len(a):
        to_remove = 1 if mex == 0 else mex
        touched = set()
        while to_remove > 0 and i < len(a):
            value = a[i]
            freq[value] -= 1
            if value < mex and value not in touched:
                touched.add(value)
                to_remove -= 1
            i += 1
            if mex == 0:
                break

        if i < len(a):
            mex = find_mex(freq)
            res.append(mex)

    print(len(res))
    print(*res)





if __name__ == "__main__":
    for _ in range(inp()):
        _ = inp()
        a = read_int_list()
        solve(a)