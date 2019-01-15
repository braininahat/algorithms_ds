def rotated_search(arr, val):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == val:
            return mid
        if (arr[low] <= arr[mid]):
            if(arr[low] <= val and val < arr[mid]):
                high = mid - 1
            else:
                low = low + 1
        else:
            if(arr[mid] < val and val <= arr[high]):
                low = mid + 1
            else:
                high = mid - 1
    return -1


def main():
    arr = [6, 7, 1, 2, 3, 4, 5]
    print(arr)
    val = int(input("Enter the search key\n"))
    out = rotated_search(arr, val)
    if out != -1:
        print("The index is: ", out)
    else:
        print("Not found.")


if __name__ == '__main__':
    main()
