import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


steps = [
    lambda x: 0,
    lambda x: x,
    lambda x: -1,
    lambda x: -x - 1
]

if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        x, m = read()
        d = steps[m % 4](m)
        print(x - d if x % 2 == 0 else x + d)

