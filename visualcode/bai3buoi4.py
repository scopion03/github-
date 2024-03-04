# Nhập hai chuỗi từ bàn phím
s1 = input("Nhập chuỗi thứ nhất: ")
s2 = input("Nhập chuỗi thứ hai: ")

# Chuyển đổi cả hai chuỗi thành chữ thường
s1 = s1.lower()
s2 = s2.lower()

# Kiểm tra xem độ dài có bằng nhau hay không
if len(s1) == len(s2):
    # Sắp xếp các ký tự của mỗi chuỗi
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    # Nếu các mảng ký tự đã sắp xếp bằng nhau
    if sorted_s1 == sorted_s2:
        print(s1 + " và " + s2 + " là anagram.")
    else:
        print(s1 + " và " + s2 + " không phải là anagram.")
else:
    print(s1 + " và " + s2 + " không phải là anagram.")
