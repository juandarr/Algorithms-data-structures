def count_values_lte(sorted_list, target):
    """
    Returns the number of values in the sorted list that are less than or equal to
    """
    left = 0
    right = len(sorted_list) - 1
    count = 0

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] <= target:
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return count


def triplets(a, b, c):
    a = list(set(a))
    c = list(set(c))
    a_s = sorted(a)
    c_s = sorted(c)
    b_r = {}
    count = 0
    for j in b:
        if j in b_r:
            continue
        else:
            b_r[j] = 1
        v1 = count_values_lte(a_s, j)
        v2 = count_values_lte(c_s, j)
        count += v1 * v2
    return count


print(triplets([1, 3, 5], [2, 3], [1, 2, 3]))
