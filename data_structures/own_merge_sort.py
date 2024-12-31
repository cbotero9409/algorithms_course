def merge_sorted(list):
  if len(list) == 1:
    return list
  
  left_list, right_list = split(list)
  left = merge_sorted(left_list)
  right = merge_sorted(right_list)

  return merge(left, right)

def split(list):
  half_point = len(list) // 2
  left_list = list[:half_point]
  right_list = list[half_point:]
  return left_list, right_list

def merge(left, right):
  list = []
  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      list.append(left[i])
      i += 1
    else:
      list.append(right[j])
      j += 1

  while i < len(left):
    list.append(left[i])
    i += 1

  while j < len(right):
    list.append(right[j])
    j += 1

  return list

alist = [34, 20, 13, 8, 90, 37, 40, 65, 23, 10]
print(merge_sorted(alist))

