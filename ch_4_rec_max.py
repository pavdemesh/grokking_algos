def rec_max(arr):
    """Returns max num from an array in a recursive manner"""
    if len(arr) == 1:
        return arr[0]

    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = rec_max(arr[1:])

    if sub_max > arr[0]:
        return sub_max
    else:
        return arr[0]


print(rec_max([2, 4, 8, 16]))
print(rec_max([85, 16, 9, 48, 15]))
print(rec_max([5]))
