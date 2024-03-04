def fibonacci(n):
    assert n >=0 and int(n) == n , 'Fibonacci number cannot be negative number or non integer.'
    if n in [0,1]:
     return n     #nếu fibonacci(n) thỏa n in [0,1] thì trả về n 
    else:
     return fibonacci(n-1) + fibonacci(n-2)
    # gọi fibonacci(3) k thỏa đk => trả về fibonacci(2) + fibonacci(1)
    # gọi fibonacci(2) k thỏa đk => trả về fibonacci(1) + fibonacci(0)
    
a =  fibonacci(3)
print(a)   #kết quả = 2 