def sum(numbers):
  if not numbers: # [1,2,7,9] --- [2,7,9] --- [7,9] --- [9] --- []
    return 0
  remaining_sum = sum(numbers[1:]) # [2,7,9] --- [7,9] --- [9] --- []
  total = numbers[0] + remaining_sum # 9 + 0 /// 7 + 9 /// 2 + 16 /// 1 + 18
  return total # 9 --- 16 --- 18 --- 19

print(sum([1,2,7,9]))