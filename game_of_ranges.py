import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


def solve(rg):
    range_sets = {}
    for a, b in rg:
        s = set()
        for i in range(a, b + 1):
            s.add(i)
        range_sets[(a, b)] = s
    while range_sets:
        last = -1
        for (a, b), values in range_sets.items():
            if len(values) == 1:
                last = values.pop()
                print(f'{a} {b} {last}')
                range_sets.pop((a, b))
                break
        for values in range_sets.values():
            if last in values:
                values.remove(last)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        rg = []
        for i in range(n):
            rg.append(read())
        solve(rg)
        print()

