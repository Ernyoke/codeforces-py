import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


def floor(a, b):
    res = a // b
    while res * b > a:
        res -= 1
    return res


if __name__ == "__main__":

    n = int(input())
    for i in range(n):
        m, k = read()
        a = list(sorted(read()))
        s = sum(a)
        pS = [0]
        for j, a_i in enumerate(a):
            pS.append(pS[j] + a_i)

        min_steps = 1e18
        for y in range(0, m):
            x = a[0] - floor(k - pS[m - y] + a[0], y + 1)
            min_steps = min(min_steps, y + max(0, x))

        print(min_steps)





