#jawaban no 1
kendaraan =['Vario','sepeda motor', 150, 'hitam', 2]
print("kendaraan saya")
print(kendaraan)
print("=======")
#tambahkan dari list tersetbut di belakang dengan value : [harga kendaraan,  tipe kendaraan,]
#kendaraan.append(200000)
#kendaraan.append('matic')
kendaraan.extend([200000,'matic'])
print(kendaraan)
print("======")
#tambahkan setelah jenis kendaraan dengan value [merk kendaraan]
kendaraan.insert(2, 'honda')
print(kendaraan)
print("======")

#jawaban no 2
#buat program phyton dengan match case untuk menghitung luas bangun datar :
print('Ini adalah program sederhana untuk menghitung luas bangun datar')
print('Pilih menu angka 1-3 : \n1. persegi\n2. lingkaran\n3 segitiga')
pilihMenu = int(input('Silahkan pilih menu dengan mengetikkan angka 1-3: '))
match pilihMenu:
    case 1:
        print("Ini adalah menu untuk menghitung luas persegi")
        sisi = int(input('silakan masukan nilai yang mau dihitung: '))
        hitung = sisi * sisi
        print("Luas persegi adalah : " , hitung )
    case 2:
        print("Ini adalah menu untuk menghitung luas lingkaran")
        phi = 22/7
        r = int(input('silahkan masukkan nilai jari-jari: '))
        hitung = phi * r * r
        print("Luas lingkaran adalah : ", hitung )
    case 3:
        print("Ini adalah menu untuk menghitung luas segitiga")
        alas = int(input('silahkan masukkan nilai alas: '))
        tinggi = int(input('silahkan masukkan nilai tinggi: '))
        hitung = 1/2 * alas * tinggi
        print("Luas segitiga adalah: ", hitung)
    case _:
        print("Pilihan tidak valid, silahkan pilih dari 1-3")