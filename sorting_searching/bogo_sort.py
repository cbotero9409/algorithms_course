import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

print(numbers)

def is_sorted(values):
  for index in range(len(values) - 1):
    if values[index] > values[index + 1]:
      return False
  return True

def bogo_sort(values):
  attempts = 0
  while not is_sorted(values):
    random.shuffle(values)
    attempts += 1
  print(attempts)
  return values

print(bogo_sort(numbers))