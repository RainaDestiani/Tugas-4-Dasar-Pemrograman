pilihan = ["batu", "gunting", "kertas"]

pemain1 = input("Pemain 1 lakukan pilihanmu : ")
pemain2 = input("Pemain 2 lakukan pilihanmu : ")

if pemain1 == pemain2 :
    print ("Ini seri")
elif pemain1 == "batu" and pemain2 == "gunting":
    print("pemain 1 menang")
elif pemain1 == "kertas" and pemain2 == "batu":
    print("pemain 1 menang")
elif pemain1 == "gunting" and pemain2 == "kertas":
    print("pemain 1 menang")
else:
    print("pemain 2 menang")