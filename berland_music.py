import sys

input = sys.stdin.readline


def read_ints():
    return list(map(int, input().strip().split()))


def read_strs():
    s = input().strip()
    return list(map(int, list(s)))


def solve(p, s):
    lower = [rating for index, rating in enumerate(p) if s[index] == 0]
    upper = [rating for index, rating in enumerate(p) if s[index] == 1]
    index_map = {}
    for index, rating in enumerate(p):
        index_map[rating] = index
    lower.sort()
    upper.sort()
    combined = lower + upper
    result = [0 for _ in p]
    for index, rating in enumerate(combined):
        result[index_map[rating]] = index + 1
    return result


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        m = int(input())
        p = read_ints()
        s = read_strs()
        print(*solve(p, s))
