a = int(input("Masukan angka pertama : "))
b = int(input("Masukan angka kedua : "))
c = int(input("Masukan angka ketiga : "))

if a < b and a < c:
    print(f"Bilangan {a} adalah bilangan yang lebih kecil")
elif b < a and b < c:
    print(f"Bilangan {b} adalah bilangan yang lebih kecil")
else:
    print(f"Bilangan {c} adalah bilangan yang lebih kecil")