a = int(input("Masukan angka pertama : "))
b = int(input("Masukan angka kedua : "))
c = int(input("Masukan angka ketiga : "))

if a > b and a > c :
    print(f"{a} adalah bilangan yang terbesar")
elif b > a and b > c:
    print(f"{b} adalah bilangan yang terbesar")
elif c > a and c > b:
    print(f"{c} adalah bilangan yang terbesar")

elif a == b and a > c:
    print(f"{a} sama dengan {b} dan lebih besar dari {c}")
elif b == c and b > a:
    print(f"{b} sama dengan {c} dan lebih besar dari {a}")
elif c == a and c > b:
    print(f"{c} sama dengan {a} dan lebih besar dari {b}")

else:
    print(f"Semua bilangan tersebut sama besar")