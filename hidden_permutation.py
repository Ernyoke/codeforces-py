# https://codeforces.com/problemset/problem/1621/C

import sys

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


def flush():
    sys.stdout.flush()


def query(value):
    print(f'? {value}\n')
    flush()
    return inp()


def solve(n):
    p = [-1] * (n + 1)
    for i in range(1, len(p)):
        cycle = []
        current = p[i]
        if current == -1:
            first = query(i)
            cycle.append(first)
            while True:
                nxt = query(i)
                cycle.append(nxt)
                if first == nxt:
                    break
        for idx in range(len(cycle) - 1):
            p[cycle[idx]] = cycle[idx + 1]

    print(f'! ', end='')
    print(*p[1:])
    flush()


if __name__ == "__main__":
    for _ in range(inp()):
        n = inp()
        solve(n)
