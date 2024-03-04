def reverse_number(num):
 
  if num < 10:
    return num
 
  else:
    return (num % 10) * (10 ** (len(str(num)) - 1)) + reverse_number(num // 10)

print(reverse_number(1234))
