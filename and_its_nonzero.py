import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))
    pre = [[0] * 18 for _ in range(0, 2 * 10 ** 5 + 1)]
    for i in range(1, 2 * 10 ** 5 + 1):
        for j in range(0, 18):
            pre[i][j] = pre[i - 1][j] + (i >> j & 1)

    for n in range(int(input())):
        a, b = read()

        max_value = 0
        for i in range(0, 18):
            max_value = max(max_value, pre[b][i] - pre[a - 1][i])
        print(b - a + 1 - max_value)
