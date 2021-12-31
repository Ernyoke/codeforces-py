import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


if __name__ == "__main__":
    n = int(input())
    stack = read()
    order = read()

    seen = set()

    result = []
    index = 0
    for i in order:
        count = 0
        if i not in seen:
            while index < len(stack):
                seen.add(stack[index])
                count += 1
                index += 1
                if stack[index - 1] == i:
                    break
        result.append(count)

    print(" ".join([str(i) for i in result]))


