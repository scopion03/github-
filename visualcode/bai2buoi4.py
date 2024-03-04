
def is_palindrome(string):
    string = string.lower().replace(" ", "")
    reversed_string = string[::-1]
   
    if string == reversed_string:
        return True
    else:
        return False

string = input("Nhập chuỗi: ")
if is_palindrome(string):
    print("Chuỗi", string, "là palindrome")
else:
    print("Chuỗi", string, "không phải là palindrome")
