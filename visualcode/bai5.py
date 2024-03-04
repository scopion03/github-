def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0,1]:
     return 1
    else:
     return n * factorial(n-1) #nếu k thỏa đk n in [0, 1] thì trả về 3 * factorial(2)
     # gọi factorial(2), không thỏa đk n in [0, 1] => trả về 2 * factorial(1)
     # gọi factorial(1) thỏa điều kiện => trả về 1 

a = factorial(3)
factorial(a)
print(a) # kết quả a = 6