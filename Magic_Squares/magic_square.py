import numpy as np


def get_input():

    N = int(input())

    if (N < 0 or N % 2 == 0):
        print("Error: N is invalid.")
        return - 1
    else:
        return N


def calculate_next_position(i, j, N, square):

    if (i > 0):
        k = i - 1
    else:
        k = N - 1

    if (j > 0):
        l = j - 1
    else:
        l = N - 1

    if square[k-1, l-1] != 0:
        k = i + 1
        l = j
    return k, l


def generate_magic_square(N):
    square = np.zeros((N, N))

    key = 1

    k, j = 1, int((N+1)/2)

    square[k-1, j-1] = key

    key = key + 1

    for i in range(key, N**2+1):
        k, j = calculate_next_position(k, j, N, square)
        square[k-1, j-1] = i

    return square


def main():
    N = get_input()
    while N == - 1:
        N = get_input()

    magic_square = generate_magic_square(N)
    print(magic_square)


if __name__ == "__main__":
    main()
