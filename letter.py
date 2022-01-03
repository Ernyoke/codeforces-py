import sys

input = sys.stdin.readline


def read_ints():
    return list(map(int, input().strip().split()))


def read_strs():
    s = input()
    return list(s[:len(s) - 1])


if __name__ == "__main__":
    n, m = read_ints()
    drawing = []
    for _ in range(n):
        drawing.append(read_strs())

    min_x, min_y, max_x, max_y = 100, 100, 0, 0
    for i, line in enumerate(drawing):
        for j, char in enumerate(line):
            if char == '*':
                min_x = min(min_x, i)
                max_x = max(max_x, i)
                min_y = min(min_y, j)
                max_y = max(max_y, j)

    for i in range(min_x, max_x + 1):
        print("".join(drawing[i][min_y:max_y + 1]))
