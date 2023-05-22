def binary_search(collection, item, lo, hi):
    left, right = 0, len(collection) - 1

    while left <= right:
        mid = left + (right - left) // 2
        current_item = collection[mid]
        if item == current_item:
            return mid
        elif item < current_item:
            right = mid - 1
        else:
            left = mid + 1
    return None