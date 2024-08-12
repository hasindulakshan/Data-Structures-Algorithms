def binarySearch(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binarySearch(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
