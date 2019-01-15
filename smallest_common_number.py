def find_least_common_number(a, b, c):
    low_a = 0
    low_b = 0
    low_c = 0
    high_a = len(a) - 1
    high_b = len(b) - 1
    high_c = len(c) - 1
    while (low_a <= high_a) and (low_b <= high_b) and (low_c <= high_c):
        first = a[low_a]
        second = b[low_b]
        third = c[low_c]
        if first == second == third:
            return first
        else:
            if first == min(first, second, third):
                low_a += 1
            elif second == min(first, second, third):
                low_b += 1
            else:
                low_c += 1
    return -1


def main():
    v1 = [1, 6, 10, 14, 50]
    v2 = [-1, 6, 7, 8, 50]
    v3 = [0, 6, 7, 10, 25, 30, 50]
    result = find_least_common_number(v1, v2, v3)
    print("Least common number: " + str(result))


if __name__ == '__main__':
    main()
