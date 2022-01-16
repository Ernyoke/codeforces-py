# https://codeforces.com/contest/1626/problem/A

import sys

input = sys.stdin.readline


if __name__ == "__main__":
    for _ in range(int(input())):
        print("".join(sorted(input().strip())))