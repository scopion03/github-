def powerOfTwo(n):
    if n == 0:   #nếu n = 0
     return 1    #trả về 1
    else:
     power = powerOfTwo(n-1)  #gọi hàm chính với n giảm đi 1đơn vị 
     return power * 2       #nhan giá trị power nhân 2
    # n = 1 => powerOfTwo(1) = 2
    # n = 2 => powerOfTwo(2) = 4  
    # n = 3 => powerOfTwo(2) = 8
     
result = powerOfTwo(3)
print(result) #kết quả là 8