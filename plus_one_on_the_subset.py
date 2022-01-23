import sys

input = sys.stdin.readline


# Input functions
def inp():
    return int(input())


def read_int_list():
    return list(map(int, input().split()))


# Solution
def solve(numbers):
    return max(numbers) - min(numbers)


if __name__ == "__main__":
    for _ in range(inp()):
        n = inp()
        numbers = read_int_list()
        print(solve(numbers))