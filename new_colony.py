# https://codeforces.com/problemset/problem/1481/B
import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().split()))


def solve(k, heights):
    max_item = max(heights)
    s = 0
    for h in heights:
        s += max_item - h
    if s < k:
        return -1

    last_height = -1
    for i in range(k):
        for h_index in range(1, len(heights)):
            if heights[h_index - 1] >= heights[h_index]:
                if h_index == len(heights) - 1:
                    return -1
            else:
                heights[h_index - 1] += 1
                last_height = h_index
                break
    return last_height


if __name__ == "__main__":
    for _ in range(int(input())):
        n, k = read()
        h = read()
        print(solve(k, h))
