def chuyensothapphansangnhiphan(so_thap_phan):
    if so_thap_phan == 1:
        print(1, end="")
    else:
         chuyensothapphansangnhiphan(int(so_thap_phan / 2))
         print(so_thap_phan % 2, end="")
         # ví dụ lần gọi đầu tiên với số thập phân 13 chuyensotthapphansangnhiphan(6) 
         # Lần gọi thứ hai với một nửa của số hiện tại chuyensotthapphansangnhiphan(3) 
         # Lần gọi thứ ba với một nửa của số hiện tại chuyensotthapphansangnhiphan(1) 
         # Lần gọi thứ tư với một nửa của số hiện tại 1
         # In ra từ lần gọi thứ tư vì số bằng 1 1 
         # In ra phần dư của số hiện tại chia cho 2 từ lần gọi thứ ba 0 
         # In ra phần dư của số hiện tại chia cho 2 từ lần gọi thứ hai 1 
         # In ra phần dư của số hiện tại chia cho 2 từ lần gọi đầu tiên

so_thap_phan = int(input("nhap so thap phan: "))
chuyensothapphansangnhiphan(so_thap_phan)