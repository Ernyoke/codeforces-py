import sys
from math import gcd

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


def solve(a):
    gcd_a = [a[0], a[1]]
    for i in range(2, len(a)):
        gcd_a[i % 2] = gcd(gcd_a[i % 2], a[i])

    res = [True, True]
    for i in range(len(a)):
        j = 1 if i % 2 == 0 else 0
        if a[i] % gcd_a[j] == 0:
            res[j] = False

    for i, r in enumerate(res):
        if r:
            return gcd_a[i]
    return 0


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        m = int(input())
        lst = read()
        print(solve(lst))