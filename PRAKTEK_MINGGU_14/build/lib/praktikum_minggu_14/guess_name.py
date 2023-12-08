def guess_number():
    angka_rahasia=9
    batas=3
    penghitung=0

    while penghitung < batas:
        user = int(input("Masukan angka > "))
        if user == angka_rahasia:
            print("Selamat tebakan anda benar")
            break
        else :
            print("tebakan anda salah")
            penghitung += 1
    else :
        print("gagal")

guess_number()