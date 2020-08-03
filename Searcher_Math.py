import os
import sys
import time

#Login
def Login():
    print("Welcome Silah kan Masuk Sebelum Masuk")
    
    print("  _____        _________________   ______________               ____    _____        ___                                    ")
    print(" |     |      |                 | |              |             |    |  |      \     |   |                                   ")
    print(" |     |      |     _______     | |     _________|             |    |  |       \    |   |                             ")
    print(" |     |      |    |       |    | |    |   _______             |    |  |   |\   \   |   |                              ")
    print(" |     |      |    |       |    | |    |  |       |  ________  |    |  |   | \   \  |   |                             ")
    print(" |     |      |    |       |    | |    |  |__     | |        | |    |  |   |  \   \ |   |                                  ")
    print(" |     |_____ |    |_______|    | |    |_____|    | |________| |    |  |   |   \   \|   |                              ")
    print(" |           ||                 | |               |            |    |  |   |    \       |                               ")
    print(" |___________||_________________| |_______________|            |____|  |___|     \______|                                 ")
    
    print("Note : Type `pls` for Get The Log-In Password, But This is Not Administrator Password")
    password = input("Masukan Password : ")
    
    if password == 'uwau':
        cls()
        print("Welcome Back")
        print("                      ````........````                      ")
        print("          `:s/`    ``````````````````````    .oy/`          ")
        print("       -.+Nm-   ``.````  ``  ``  ``  ````.``   /NN/::       ")
        print("     .hosNo:  ```   .````.``o/oy:`.````.   ```  /oN/hh`     ")
        print("   `.dN`ooh- .`    .    .  `s /Ms  .    .    `. :ds+-Ms:`   ")
        print("  `d`MsyNo` .```` .    ``    .s-   ``    . ````. `omhdh-d   ")
        print("  sM`mh+o` .     .`````.`````//`````.`````.     . -o/hy/M/  ")
        print("  hM:+oN/ .`     .     .     ss     .     .     `. +Ns:oMo  ")
        print(" -oMomm:  .     ``     .     --     .     ``     .  :mNsM:/ ")
        print(" d`dmh-+ ``     .`     . `/`+ss+`/` .     ``     `` s-sNs.N ")
        print(" Ny.y-N/ `.`````..`.-:+shMh `yy` hMhs+:-.`..`````.` /N:o`dm ")
        print(" yMo.Nm   .     ```NMMMMMM/ `++` /MMMMMMN```     .   mN-hMo ")
        print(" -mMsM/:  .     `.sMMMMMMMs  dd  sMMMMMMMs.`     .  +:MyMy-`")
        print(" h.smd`N. `.     -NMMMMMMMN.`MM`.NMMMMMMMN-     .` :N`hd/:d ")
        print(" +No:o:M+  `` ```/MMMMMMMMMm:MM:mMMMMMMMMM/``` ``  oM:/:hN: ")
        print("  +NN+:Ms-- `.`  yMMMMMMMMMMMMMMMMMMMMMMMMy  `.` /-yM:yMd-  ")
        print("   :omdmd N+  .` NMMMMMMMMMMMMMMMMMMMMMMMMN `.  sm mmmh//   ")
        print("   -y::sm:yM/  `:MMMMMMMMMMMMMMMMMMMMMMMMMM:`  +Ms/h/:oh.   ")
        print("    `sNho+.mN-+.-MMMMMMMMMMMMMMMMMMMMMMMMMM::o-Nd-+ymm+     ")
        print("      `+dNNhdd-mhomMMMMMMMMMMMMMMMMMMMMMMmsdm-dmdMms/       ")
        print("       `/++++++.smddmMMMMMMMMMMMMMMMMMMmdddo-oo+++o/`       ")
        print("         .+hNMMNNmdhdMMMMMMMMMMMMMMMMMMhyhdNMMNds/`         ")
        print("            `///::/smMMMMMMMMMMMMMMMMMMmy+/:///.            ")
        print("              .+syyyNMMMMMMMMMMMMMMMMMMmosso/.              ")
        print("                    NMMMMMMMMMMMMMMMMMMN                    ")
        print("                    .:+syhdmmNNmmdhys+:.                    ")
        time.sleep(3)
        cls()
        Menu_Utama()
    elif password == 'pls':
        cls()
        print("Password is uwau")
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
    print("Welcome To ===Searcher_Tools===")
    print("Program Coder")
    print("Program Lenguage = Python 3")
    print("===AFIF_NAUFAL_ZAHRAN===")
    print("Pilih Program")
    print("[1]Pencari Luas")
    print("[2]Calculator")
    print("[3]WIFI_Booster")
    print("[4]Versions")
    print("[5]Testing")
    print("[0]Quit_Program")
    print("Note : Masukan Angka Yang Ada Di Kolom Pemilihan Di Pilih : ")

    menu = int(input("Pilih : "))

    if menu == 1:
        pencari_luas()
    elif menu == 2:
        Calculator()
    elif menu == 3:
        fake_wifi()
    elif menu == 0:
        Quit()
    elif menu == 4:
        Versions()
    elif menu == 5:
        Tester()
    else:
        print("Program Tidak Di Temukan")
        delay()
        Menu_Utama()

#Tester
def Tester():
    cls()
    test = int(input("Test Angka : "))
    data_int = test;

    data_bool = bool(data_int)
    print("Data = ", data_bool,)
    print("Tipe Data = ", type(data_bool))

#Versions
def Versions():
    print("Searcher Tools Versions 1.0")
    Display_Menu()

#Display_Menu
def Display_Menu():
    input("Enter Untuk Kembali")
    Menu_Utama()

#delay
def delay():
    time.sleep(1)

#clear_System
def cls():
    os.system('clear')

#fake_wifi
def fake_wifi():
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
    print("[5]Perpangkatan")
    print("[6]Sisa Bagi")
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
    elif pilih == '5':
        Perpangkat()
    elif pilih == '6':
        Sisa_Bagi()
    elif pilih == '0':
        Menu_Utama()

#Persenan
def Sisa_Bagi():
    cls()
    print("Rumus Sisa Bagi Sisa Bagi Dari Pembagian Num / Num1")

    num = int(input("Num1 : "))
    print("//")
    num1 = int(input("Num2 : "))

    hasil = num // num1

    print("Hasil = ", hasil)

#Perpangkatan
def Perpangkatan():
    cls()
    print("Rumus Perpangkatan : Num pangkat Num2")
    print("** = Pangkat Dalam bahasa Pemograman Python")

    num = int(input("Num : "))

    print("**")

    num1 = int(input("Num1 : "))

    hasil = num ** num1

    print("Hasil = ", hasil)

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
    print("-")
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
    print("+")
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
    print("X")
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
        Persegi_Panjang
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

Login()
