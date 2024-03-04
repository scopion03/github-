def uocchunglonnhat(a, b):
    if a >= b:
        if b == 0:
            return a
        else:
            return uocchunglonnhat(b, int(a % b))
    else:
        if a == 0:
            return b
        else:
            return  uocchunglonnhat( a, int(b % a))
        
a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))
print( uocchunglonnhat(a , b))