def binary_search(collection, item):
    left, right = 0, len(collection) - 1
    while left <= right:
        mid = left + (right - left) // 2
        cur_item = collection[mid]
        if cur_item == item:
            return mid
        elif cur_item > item:
            right = mid - 1
        else:
            left = mid + 1
    return None