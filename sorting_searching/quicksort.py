import sys
from load import load_numbers

# numbers = load_numbers(sys.argv[1])

def quicksort(values):
  if len(values) <= 1:
    return values
  
  # Get initial pivot (first element)
  pivot = values[0]
  # Divide list in 2 sublists (elements lesser and greater)
  lesser, greater = get_sublists(values[1:], pivot) 
  # Recursive call function with new sublist until 1 element
  less = quicksort(lesser)
  great = quicksort(greater)
  # Sort list
  return less + [pivot] + great 

def get_sublists(values, pivot):
  lesser = []
  greater = []

  for i in range(0, len(values)):
    if values[i] <= pivot:
      lesser.append(values[i])
    else:
      greater.append(values[i])

  return lesser, greater

print(quicksort([4,6,3,2,9,7,3,5]))