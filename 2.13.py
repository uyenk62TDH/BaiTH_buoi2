import math

a=int(input("nhap a: "))
b=int(input("nhap b: "))
c=int(input("nhap c: "))
denta=b*b-4*a*c;
if denta>0:
    x1=(-b-math.sqrt(denta))/(2*a)
    x2=(-b+math.sqrt(denta))/(2*a)
    print("phuong trinh co hai nghiem phan biet la")
    print('x1= ',x1)
    print("x2= ",x2)
elif denta==0:
    x=-b/(2*a)
    print('phuong trinh co nghiem duy nhat'&x)
else:
    print("phuong trinh vo nghiem")
