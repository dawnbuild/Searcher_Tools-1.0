import os
import sys
import time

#Login
def Login():
    print("Welcome Silah kan Masuk Sebelum Masuk")
    
    print("  ____        _________________     _______________      ____    _____        ___                                    ")
    print(" |    |      |                 |   |               |    |    |  |      \     |   |                                   ")
    print(" |    |      |    _________    |   |      _________|    |    |  |       \    |   |                             ")
    print(" |    |      |   |         |   |   |     |  ________    |    |  |    |\  \   |   |                              ")
    print(" |    |      |   |         |   |   |     | |        |   |    |  |    | \  \  |   |                             ")
    print(" |    |      |   |         |   |   |     | |__      |   |    |  |    |  \  \ |   |                                  ")
    print(" |    |_____ |   |_________|   |   |     |____|     |   |    |  |    |   \  \|   |                              ")
    print(" |          ||                 |   |                |   |    |  |    |    \      |                               ")
    print(" |__________||_________________|   |________________|   |____|  |____|     \_____|                                 ")
    
    password = input("Masukan Password : ")
    
    if password == 'zahran':
        cls()
        print("Welcome Back")
        delay()
        cls()
        Menu_Utama()
    elif password == 'pls':
        cls()
        print("Password is zahran")
        delay()
        cls()
        Login()

    else:
        cls()
        print("Maaf Password Salah")
        delay()
        cls()
        Login()

#Menu_Utama
def Menu_Utama():
    cls()
    print("Welcome To ---Searcher_Tools---")
    print("Program Coder")
    print("---AFIF_NAUFAL_ZAHRAN---")
    print("Pilih Program")
    print("[1]Pencari Luas")
    print("[2]Calculator")
    print("[3]WIFI_Booster")
    print("[4]Version")
    print("[0]Quit_Program")
    print("Note : Masukan Angka Yang Ada Di Kolom Pemilihan Di Pilih : ")

    menu = int(input("Pilih : "))

    if menu == 1:
        pencari_luas()
    elif menu == 2:
        Calculator()
    elif menu == 3:
        fake_wifi()
    elif menu == 4:
        Version()
    elif menu == 0:
        Quit()
    else:
        print("Program Tidak Di Temukan")
        delay()
        Menu_Utama()

#Display_Menu
def Display_Menu():
    input("Enter Untuk Kembali")
    Menu_Utama()

#delay
def delay():
    time.sleep(1.3)

#clear_System
def cls():
    os.system('cls')

#fake_wifi
def fake_wifi():
    cls()
    print("Welcome To Wifi Booster")
    print("Wifi Booster Script By ---Coder_Builder---")
    print("Note : This Wifi Booster Will Not Ham your Computer System or Wifi System")

    passw = input("Administrator Require : ")

    if passw == 'zahran':
        print("Nice Your Wifi Has Been Boosted by ---zahran---")
        os.system('ping -l 100 192.168.100.1 -t')
    else:
        print("Sorry Password Wrong")
        input("Enter To Back")
        fake_wifi()

#Calculator
def Calculator():
    cls()
    print("Welcome")
    print("[1]Perkalian")
    print("[2]Pertambahan")
    print("[3]Perkurangan")
    print("[4]Pembagian")
    print("[0]Back To Menu")

    pilih = input("Pilih : ")

    if pilih == '1':
        Perkalian()
    elif pilih == '2':
        Pertambahan()
    elif pilih == '3':
        Pengurangan()
    elif pilih == '4':
        Pembagian()
    elif pilih == '0':
        Menu_Utama()
    else:
        print("Script Tidak Di TEMUKAN")
        Display_Menu()

#Pembagian
def Pembagian():
    cls()
    print("Welcome")
    print("Rumus Perkalian, Num1 / Num2")
    
    Num1 = int(input("Num1 : "))
    print("/")
    Num2 = int(input("Num2 : "))

    hasil = Num1 / Num2

    print("Hasil = ",hasil,)
    Display_Menu()

#Perkurangan
def Pengurangan():
    cls()
    print("Welcome")
    print("Rumus Penguangan, Num1 - Num2")
    
    Num1 = int(input("Num1 : "))

    Num2 = int(input("Num2 : "))

    hasil = Num1 - Num2

    print("Hasil = ",hasil,)
    Display_Menu()

#Pertmabahan
def Pertambahan():
    cls()
    print("Welcome")
    print("Rumus Perkalian, Num1 + Num2")
    
    Num1 = int(input("Num1 : "))

    Num2 = int(input("Num2 : "))

    hasil = Num1 + Num2

    print("Hasil = ",hasil,)
    Display_Menu()

#Perkalian
def Perkalian():
    cls()
    print("Welcome")
    print("Rumus Perkalian, Num1 X Num2")
    
    Num1 = int(input("Num1 : "))

    Num2 = int(input("Num2 : "))

    hasil = Num1 * Num2

    print("Hasil = ",hasil,)
    Display_Menu()


#LUAS
def pencari_luas():
    cls()
    print("Welcome")
    print("[1]Persegi")
    print("[2]Lingkaran")
    print("[3]Persegi_Panjang")
    print("[0]Back To Main Menu")

    pilih = int(input("Pilih : "))

    if pilih == 1:
        Persegi()
    elif pilih == 2:
        Lingkaran()
    elif pilih == 3:
        Persegi_Panjang()
    elif pilih == 0:
        Display_Menu()
    else:
        print("Selebih Nya Cari Sendiri :V ")
        delay()
        pencari_luas()

#Persegi
def Persegi():
    print("Welcome")
    print("Rumus Mencari Luas Persegi")
    print("Sisi X Sisi")

    sisi = int(input("Masukan Sisi : "))

    luas = sisi * sisi

    print("Luas Persegi Dari Sisi",sisi,"Adalah = ",luas,)
    Display_Menu()

#Lingkaran
def Lingkaran():
    print("Welcome")
    print("Rumus Luas Lingkaran πR²")

    Ruas = int(input("Ruas : "))

    luas = 3.14 * Ruas * Ruas

    print("Luas Lingkaran Adalah = ",luas,)
    Display_Menu()

#Persegi_Panjang
def Persegi_Panjang():
    print("Welcome")
    print("Rumus Panjang X Lebar")

    Panjang = int(input("Panjang : "))

    Lebar = int(input("Lebar : "))

    luas = Panjang * Lebar

    print("Luas Persegi Panjang Adalah =",luas,)
    Display_Menu()

#Version
def Version():
    cls()
    print("Script Version 1.0")
    Display_Menu()

Login()
