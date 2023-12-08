# sistem konversi berat

def weight_conversation():
    weight =  int(input("berapa berat mu lurd :"))
    types =  input("masukan satuan k untuk kg dan l untuk pounds :")

    if types.upper() == "K":
        print("Berat anda :", round(weight*2.2), "pounds")
    elif types.upper() == "L": 
        print("Berat anda :", round(weight/2.2), "kilo")
