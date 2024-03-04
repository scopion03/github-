def luythua( a, bac_cua_a):
    if bac_cua_a == 0:    #nếu bậc của a = 0 thì hàm trả về 1 
        return 1        
    else:
        return a * luythua( a, bac_cua_a - 1)
     # Lần gọi đầu tiên với số cơ sở 2 và số mũ 3=> 2 * luythua(2, 2)
     #Lần gọi thứ hai với số mũ giảm đi 1 => 2 * 2 * luythua(2, 1)
    # Lần gọi thứ ba với số mũ giảm đi 1=> 2 * 2 * 2 * luythu
     # Lần gọi thứ tư với số mũ giảm đi 1=> 2 * 2 * 2 * 1
a = int(input("nhap so a: "))
bac_cua_a = int(input("nhap bac cua a: "))
print(luythua( a, bac_cua_a))