from linked_list import LinkedList

def merge_sort(linked_list):
  if linked_list.size() == 1 or linked_list.head is None:
    return linked_list
  
  left_half, right_half = split(linked_list)
  left = merge_sort(left_half)
  right = merge_sort(right_half)

  return merge(left, right)

def split(linked_list):
  if linked_list == None or linked_list.head is None:
    left_half = linked_list
    right_half = None
  else:
    half = linked_list.size() // 2
    half_node = linked_list.node_at_index(half-1)
    left_half = linked_list
    right_half = LinkedList()
    right_half.head = half_node.next_node
    half_node.next_node = None

  return left_half, right_half

def merge(left, right):
  merged = LinkedList()
  merged.add(0)
  current = merged.head
  left_head = left.head
  right_head = right.head

  while left_head or right_head:
    if left_head is None:
      current.next_node = right_head
      right_head = right_head.next_node
    elif right_head is None:
      current.next_node = left_head
      left_head = left_head.next_node
    else:
      if left_head.data < right_head.data:
        current.next_node = left_head
        left_head = left_head.next_node
      else:
        current.next_node = right_head
        right_head = right_head.next_node
    current = current.next_node
    
  merged.head = merged.head.next_node
  
  return merged

l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)