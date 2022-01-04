import sys

input = sys.stdin.readline


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        for i in range(n):
            print(f'{i + 2} ', end='')
        print()
