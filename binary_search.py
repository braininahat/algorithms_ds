import random


def search(arr, val):
    low = 0
    high = len(arr) - 1
    mid = low + ((high - low) // 2)
    while low <= high:
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            low = mid + 1
            mid = low + ((high - low) // 2)
        elif arr[mid] > val:
            high = mid - 1
            mid = low + ((high - low) // 2)
    return -1


def main():
    arr_size = 10
    arr = sorted([random.randint(0, arr_size * 3)
                  for _ in range(arr_size)])
    print(arr)
    val = int(input("Enter the search key\n"))
    out = search(arr, val)
    if out != -1:
        print("The index is: ", search(arr, val))
    else:
        print("Not found.")


if __name__ == '__main__':
    main()
