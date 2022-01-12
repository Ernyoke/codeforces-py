import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


def gauss(n):
    return n * (n + 1) // 2


def solve(nodes, edges, k):
    if edges < nodes - 1:
        return "NO"
    g = gauss(nodes - 1)
    if edges > g:
        return "NO" \

    if nodes == 1:
        return "YES" if k > 1 else "NO"

    # fully connected graph
    if edges == g:
        return "YES" if k > 2 else "NO"
    return "YES" if k > 3 else "NO"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, k = read()
        print(solve(n, m, k))

    # a = 0
    # b = 2
    # for y in range(550):
    #     print(f'1 {a} {b}')
    #     b += 1
    #     if b == 4:
    #         b = 2
    #         a += 1