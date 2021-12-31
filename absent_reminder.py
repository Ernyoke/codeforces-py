import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


def solve(lst):
    count = 0
    min_value = min(lst)
    for x in lst:
        if x == min_value:
            continue
        if count < len(lst) // 2:
            count += 1
            print(x, min_value)
        else:
            break


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        m = int(input())
        a = read()
        solve(a)