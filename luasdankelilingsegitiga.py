import math
a = float(input("Masukan angka untuk sisi a :"))
b = float(input("Masukan angka untuk sisi b :"))
c = float(input("Masukan angka untuk sisi c :"))

s = (a+b+c)/2
luas = math.sqrt (s * (s-a)*(s-b)*(s-c))
Keliling = a + b + c

print ("semi-parimeter adalah ", s)
print ("luas segitiga adalah ", luas)
print ("keliling segitiga adalah ", Keliling)
