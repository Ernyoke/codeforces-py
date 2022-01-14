import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


def solve(L, a, periods):
    if len(periods) == 0:
        return L // a

    breaks = 0
    first_period = periods[0]
    if first_period[0] >= a:
        breaks += (first_period[0] // a)

    for i in range(1, len(periods)):
        prev = periods[i - 1]
        current = periods[i]
        free_time = current[0] - (prev[0] + prev[1])
        if free_time >= a:
            breaks += (free_time // a)

    last_period = periods[len(periods) - 1]
    if L - (last_period[0] + last_period[1]) >= a:
        breaks += ((L - (last_period[0] + last_period[1])) // a)

    return breaks


if __name__ == "__main__":
    n, L, a = read()
    periods = []
    for _ in range(n):
        periods.append(read())

    print(solve(L, a, periods))
