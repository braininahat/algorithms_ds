def rotate(self, arr, n):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    length_arr = len(arr)

    # Let's normalize rotations
    # if n > array size or n is negative.
    n = n % length_arr
    if n < 0:
        # calculate the positive rotations needed.
        n = n + length_arr

    temp = []
    for i in range (0, n):
        temp.append(0)

    # copy last N elements of array into temp
    for i in range(0, n):
        temp[i] = arr[length_arr - n + i]

    # shift original array
    for i in range(length_arr - 1, n - 1, -1):
        arr[i] = arr[i - n]

    # copy temp into original array
    for i in range(0, n):
        arr[i] = temp[i]
