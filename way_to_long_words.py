import sys

input = sys.stdin.readline


def read():
    s = input()
    return list(s[:len(s) - 1])


if __name__ == "__main__":
    val = int(input())

    for i in range(0, val):
        word = read()
        if len(word) <= 10:
            print("".join(word))
        else:
            print(f'{word[0]}{len(word) - 2}{word[len(word) -  1]}')
