import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercase1 = chr(random.randint(65,90))
uppercase2 = chr(random.randint(65,90))
lowercase1 = chr(random.randint(97,122))
lowercase2 = chr(random.randint(97,122))
digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
punctuation1 = chr(random.randint(33,152))
punctuation2 = chr(random.randint(33,152))

password = uppercase1 + uppercase2 + lowercase1 + lowercase2 + digit1 + digit2 + punctuation1 + punctuation2
password = shuffle(password)

print(password)