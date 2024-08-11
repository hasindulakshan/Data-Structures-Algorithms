def merge_sort(array):
  """Sorts a list using the merge sort algorithm."""
  if len(array) <= 1:
    return array

  middle = len(array) // 2
  left_half = array[:middle]
  right_half = array[middle:]

  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)

  return merge(left_half, right_half)

def merge(left, right):
  """Merges two sorted lists into a single sorted list."""
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])
  return result

# Example usage:
my_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(my_list)
print(sorted_list)
