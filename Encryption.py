import math

def encryption(s):
  col = math.ceil(math.sqrt(len(s)))
  enc_message = ""
  for i in range(col):
    enc_message += s.replace(" ", "")[i:len(s):col] + ' '
  return enc_message

encryption("feed the dog")