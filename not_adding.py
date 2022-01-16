# https://codeforces.com/contest/1627/problem/D

import sys

input = sys.stdin.readline


def read_int_list():
    return list(map(int, input().split()))


def solve(a):
    max_value = max(a)
    present = [False] * (max_value + 1)
    for value in a:
        present[value] = True
    count = 0
    for i in range(max_value, 0, -1):
        first = -1
        second = -1
        if present[i]:
            continue
        for j in range(2 * i, max_value + 1, i):
            if present[j]:
                if first == -1:
                    first = j
                else:
                    if j % first != 0:
                        second = j
                        break
        if first != -1 and second != -1:
            count += 1
            present[i] = True
    return count


if __name__ == "__main__":
    n = int(input())
    a = read_int_list()
    print(solve(a))
