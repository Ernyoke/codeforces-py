import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


def solve(dmg, points):
    max_value = 1e18
    periods = []
    for i in range(1, len(points)):
        period = points[i] - points[i - 1]
        periods.append(period)

    min_value = 1
    while min_value <= max_value:
        curr_dmg = min_value + int((max_value - min_value) // 2)
        curr_sum = curr_dmg + sum(min(curr_dmg, period) for period in periods)
        if curr_sum < dmg:
            min_value = curr_dmg + 1
        else:
            max_value = curr_dmg - 1
    return min_value


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print(solve(read()[1], read()))