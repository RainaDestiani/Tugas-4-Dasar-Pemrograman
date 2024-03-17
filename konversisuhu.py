celcius = float(input("Masukan suhu celcius : "))
fahrenheit = float(input("Masukan suhu fahrenheit : "))

celcius = ( fahrenheit -32) * 5/9
fahrenheit = ( celcius * 9/5) + 32
pilihan_konversi = input ("Masukan pilihan : ")
print("Pilih konversi : ")
print(" 1. celcius ke fahrenheit :", fahrenheit)
print(" 2. fahrenheit ke celcius :", celcius)

if pilihan_konversi == '1' :
    print("Suhu dalam fahrenheit ", fahrenheit)
elif pilihan_konversi == '2' :
    print("Suhu dalam celcius  ", celcius)
else:
    print ("Pilihan tidak valid. Silahkan pilih 1 atau 2")

