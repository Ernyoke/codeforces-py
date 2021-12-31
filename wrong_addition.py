import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


def compute(a, s):
    res = []
    while True:
        x, s = s % 10, s // 10
        y, a = a % 10, a // 10
        if s == 0 and a != 0:
            return -1
        if x - y >= 0:
            res.append(str((x - y)))
        else:
            carry, s = s % 10, s // 10
            if carry != 1:
                return -1
            x += 10
            res.append(str((x - y)))
        if s == 0 and a == 0:
            return int("".join(res[::-1]))


if __name__ == "__main__":
    n = int(input())
    for i in range(0, n):
        a, s = read()
        print(compute(a, s))

