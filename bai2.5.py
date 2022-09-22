a=float(input("nhap a"))
b=float(input("nhap b"))
c=float(input("nhap c"))
denta = b * b - 4 * a * c;
if denta > 0:
    x1 = -b - math.sqrt(denta) / 2 * a
    x2 = -b + math.sqrt(denta) / 2 * a
    print("phuong trinh co hai nghiem phan biet la")
    print('x1= ',x1)
    print("x2= ",x2)
else denta == 0:
    x = -b / 2 * a
    print('phuong trinh co nghiem duy nhat'&x)
else denta < 0:
    print("phuong trinh vo nghiem")
    
