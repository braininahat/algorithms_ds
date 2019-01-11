from collections import deque
import random


def max_sw(arr, window_size):
    if window_size > len(arr):
        return -1

    window = deque()

    # initialize window
    for _ in range(window_size):
        while window and arr[_] >= arr[window[-1]]:
            window.pop()
        window.append(_)

    print(arr[window[0]])

    for _ in range(window_size, len(arr)):
        while window and arr[_] >= arr[window[-1]]:
            window.pop()
        if window and (window[0] <= _ - window_size):
            window.popleft()
        window.append(_)
        print(arr[window[0]])


def main():
    arr_size = 10
    arr = [random.randint(0, arr_size * 3) for _ in range(arr_size)]
    print(arr)
    max_sw(arr, 3)


if __name__ == '__main__':
    main()
