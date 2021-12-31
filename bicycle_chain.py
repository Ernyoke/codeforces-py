import sys

input = sys.stdin.readline


def read():
    return list(map(int, input().strip().split()))


def get_max(a, b):
    max_value = 0
    for b_value in reversed(b):
        for a_value in a:
            if b_value / a_value < max_value:
                continue
            if b_value % a_value == 0:
                max_value =  b_value // a_value
    return max_value


if __name__ == "__main__":
    n = int(input())
    a = read()
    m = int(input())
    b = read()

    max_value = get_max(a, b)
    count = 0
    for b_value in reversed(b):
        for a_value in a:
            if b_value / a_value < max_value:
                continue
            if b_value % a_value == 0 and b_value // a_value == max_value:
                count += 1

    print(count)



