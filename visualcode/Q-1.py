def allFib(n): 
    for i in range(n): # Bắt đầu một vòng lặp for, lặp từ 0 đến n-1.
        print(f"{i}: {fib(i)}") # In ra số Fibonacci thứ i và giá trị của nó bằng cách gọi hàm "fib".

def fib(n): # Định nghĩa một hàm tên là "fib" nhận vào một tham số n để tính số Fibonacci thứ n.
    if n <= 0: # Kiểm tra xem giá trị của n có nhỏ hơn hoặc bằng 0 không.
        return 0 # Nếu điều kiện trên đúng, trả về 0.
    elif n == 1: # Nếu điều kiện trước không đúng, kiểm tra xem giá trị của n có bằng 1 không.
        return 1 # Nếu điều kiện trước đúng, trả về 1.
    else: # Nếu cả hai điều kiện trước đó không đúng,
        return fib(n - 1) + fib(n - 2) # Tính và trả về tổng của hai số Fibonacci liền kề phía trước trong dãy Fibonacci (đệ quy).
#Ví dụ
allFib(5)
