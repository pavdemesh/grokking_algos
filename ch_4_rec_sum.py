def rec_sum(arr):
    """Returns sum of all elements of an array in a recursive manner"""
    if len(arr) == 0:
        return 0

    return arr[0] + rec_sum(arr[1:])


print(rec_sum([5, 6, 8]))
