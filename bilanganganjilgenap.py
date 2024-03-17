a = 1

if a > 0 and a %2 == 1:
    print(f"{a} adalah bilangan positif dan ganjil")
elif a > 0 and a %2 == 0:
    print(f"{a} adalah bilangan positif dan genap")
elif a < 0 and a %2 ==1:
    print(f"{a} adalah bilangan negatif dan ganjil")
elif a < 0 and a %2 == 0:
    print(f"{a} adalah bilangan negatif dan genap")
else:
    print(F"{a} adalah bilangan yang netral")