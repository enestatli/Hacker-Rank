import math

def missingNumbers(arr, brr):
  for number in arr:
    brr.remove(number)
  return sorted(set(brr))

arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

missingNumbers(arr,brr)