import sys

input = sys.stdin.readline


def read_ints():
    return list(map(int, input().strip().split()))


def read_strs():
    s = input()
    return list(s[:len(s) - 1])


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        m = int(input())
        numbers = read_ints()
        colors = read_strs()

        zipped = list(sorted(zip(colors, numbers)))

        res = True
        for index, (color, number) in enumerate(zipped):
            if color == 'B' and number < index + 1:
                res = False
                break
            elif color == 'R' and number > index + 1:
                res = False
                break

        print("YES" if res else "NO")