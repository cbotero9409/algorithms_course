import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def selection_sort(values):
  sorted = []
  for i in range(0, len(values)):
    min_index = search_min_index(values)
    sorted.append(values.pop(min_index))

  return sorted

def search_min_index(values):
  min = 0
  for i in range(0, len(values)):
    if values[i] < values[min]:
      min = i
      
  return min

print(selection_sort(numbers))