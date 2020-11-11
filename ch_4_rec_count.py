def rec_count(arr):
    """Returns count of all elements of an array in a recursive manner"""
    if not bool(arr):
        return 0

    return 1 + rec_count(arr[1:])


print(rec_count([2, 6, 8, 5]))
