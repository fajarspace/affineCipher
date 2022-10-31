import math;

print("Nama : Fajar Agung Nugroho")
print("NIM  : 312010448")

def enkripsi():
    enkripTeks = '';
    counter = 0;
    plainTeks = input("Masukkan plainTeks: \n");
    plainTeks = plainTeks.upper();

    print('Masukkan kunci pertama, pastikan itu adalah bilangan relatif prima sampai 26: ');
    inputTipe = 'kunciA';
    kunciA = int(validasiTipe(inputTipe));
    print('Masukkan kunci kedua: ');
    inputTipe = 'kunciB';
    kunciB = int(validasiTipe(inputTipe));
    print ("Hasil:")
    hasil = len(plainTeks);
    
    for prosesEnkripsi in range(hasil):
        angka = ord(plainTeks[prosesEnkripsi]);
        if angka >= 65 and angka <= 90:
            enkripAngka = ((angka - 65) * kunciA + kunciB) % 26;
            enkripTeks += chr(enkripAngka + 65);
            counter += 1;
        elif angka == 32:
            enkripTeks += chr(angka);
            counter += 1;
    return enkripTeks;

def dekripsi():
    plainTeks = '';
    counter = 0;
    enkripTeks = input('Masukkan cipher text: \n');
    enkripTeks = enkripTeks.upper();
    
    print('Masukkan kunci pertama yang telah digunakan, Pastikan itu adalah bilangan relatif prima sampai 26: ');
    inputTipe = 'kunciA';
    kunciA = int(validasiTipe(inputTipe));
    print('Masukkan kunci kedua: ');
    inputTipe = 'kunciB';
    kunciB = int(validasiTipe(inputTipe));
    print ("Hasil:")
    hasil = len(enkripTeks);

    kunciA_inverse = int(inverse(kunciA, 26));
    for prosesDekripsi in range(hasil):
        enkripAngka = ord(enkripTeks[prosesDekripsi]);
        if enkripAngka >= 65 and enkripAngka <= 90:
            angka = (((enkripAngka - 65) - kunciB) * kunciA_inverse) % 26;
            plainTeks += chr(angka + 65);
            counter += 1;
        elif enkripAngka == 32:
            plainTeks += chr(enkripAngka);
            counter += 1;
    return plainTeks;


def validasiTipe(inputTipe):
    kunciA = input('');
    while kunciA.isdigit() == False:
        kunciA = input('Bukan Angka yang valid. Coba lagi: \n');
    if inputTipe == 'kunciA':
        validasiBilPrima(kunciA);
    return kunciA;

def validasiBilPrima(kunciA):
    inputTipe = 'kunciA';
    prosesValidasiA = math.gcd(int(kunciA), 26);
    while prosesValidasiA != 1:
        print('Angka ini bukan bilangan relatif prima sampai 26. Coba lagi: ');
        validasiTipe(inputTipe);
        break;

def inverse(a, m):
    a1 = 1;
    a2 = a;

    b1 = 0;
    b2 = m;

    while b2 != 0:
        x = a2 // b2;
        b1, b2, a1, a2 = (a1 - x * b1), (a2 - x * b2), b1, b2;
    return a1 % m;

def main():
    pilihan = '';
    while pilihan != '3':
        pilihan = input('\nKetik Angka yang tersedia. \n1. Encrypt\n2. Decrypt\n3. Keluar\n');
        if pilihan == '1':
            print(enkripsi());
        elif pilihan == '2':
            print(dekripsi());
        elif pilihan == '3':
            break;
        else:
            print('Kamu menginput pilihan yang salah.');
            pilihan = main();
    return pilihan;
main();
