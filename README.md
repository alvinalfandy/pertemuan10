# Pertemuan-10

| Variable | Isi |
| -------- | --- |
| **Nama** | Alvin alfandy |
| **NIM** | 312310473 |
| **Kelas** | TI.23.A.5 |
| **Mata Kuliah** | Bahasa Pemrograman |

# Latihan 

1. membuat kontak awal /
``` b = {'ari' : '085267888', 'dina' : 087677776} ```
2. menampilkan kontak ari /
``` print(b['ari'])```
3. menambhkan kontak riko /
``` b['riko']= 087888999```
4. mengubah kontak dina /
```b['dina]= '089555777```
5. menampilkan semua nama /
``` print(b.keys()) ```
6. menampilkan semua nomor /
``` print(b.values()) ```
7. menampilkan semua nama dan nomor /
``` print(b) ```
8. menghapus kontak dina /
``` del b['dina'] ``` /

## berikut adalah kode programnya 


```python
b={'ari':'085267888','dina':'087677776'}
print('Kontak awal')
print('==============================')
print('    nama    |   nomor telepon')
print('==============================')
print('1.    ari   |   085267888','\n2.    dina    |   087677776')

# tamprintilkan kontak ari
print('\nTampilkan Kontak Ari')
print('1.    ari      |   ',b['ari'])
print('\nMenambah Kontak Riko')
b['riko']='087654544'
print('1.   ari      |   ',b['ari'])
print('2.   dina     |   ',b['dina'])
print('3.   riko     |   ',b['riko'])
print('\nMengubah nomor Dina ke')
b['dina']='088999776'
print('1.   ari      |   ',b['ari'])
print('2.   dina     |   ',b['dina'])
print('3.   riko     |   ',b['riko'])
print('\nMenampilkan semua nama')
print(b.keys())
print('\nMenampilkan semua nomor')
print(b.values())
print('\nMenampilkan semua nama dan nomor')
print(b)
print('\nMenghapus kontak dina')
del b['dina']
print(b,'\n')
``````

## dan ini adalah hasil program nya
![Alt text](gambar/image.png) \

# tugas praktikum
program sederhana yang akan menampilkan daftar nilai mahasiswa \
## Flowchart 
![gambar](gambar/flowchart.png)  \
1. membuat lopping agar program terus berjalan:
``` sh while True :
    c = input("\n(L)ihat, (T)ambah,(U)bah, (C)ari, (K)eluar): ")
```
2. membuat formatif if untuk memasukan pilihan , contoh pilihan (t): \
if (c.lower() == 't'):                                               
      ```  print('\nTambah Data Mahasiswa Baru')
        nama= input("Masukkan Nama\t\t: ")                                        
        nim= input("Masukkan NIM\t\t: ")                                         
        nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))                              
        nilaiUts= int(input("Masukkan Nilai UTS\t: "))                                   
        nilaiUas= int(input("Masukkan Nilai UAS\t: "))                                    
        nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)              
        dataMhs[nama]= nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir                         
        print("\nData Berhasil Ditambahkan!")```
3. membuat percabangan elif untuk menjalankan pilihan yang lain
elif (c.lower() == 'u'):                                                                    
        print('\nMengedit Data Mahasiswa')
        nama = input("Masukkan Nama: ")                                                         
        if nama in dataMhs.keys():                              
            nim= input("Masukkan NIM Baru\t: ")                              
            nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))                           
            nilaiUts= int(input("Masukkan Nilai UTS\t: "))                           
            nilaiUas= int(input("Masukkan Nilai UAS\t: "))                           
            nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)          
            dataMhs[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir                      
            print("\nData Berhasil Di Update!")```
4. menggunakan else apabila salah memasukan pilihan 
else:
        print("Pilih menu yang tersedia: ")                                                   
## ini adalah contoh output untuk (t)

![Alt text](gambar/image-1.png) 

## ini adalah contoh output untuk (u): 

![Alt text](gambar/image-2.png)

## output cari (c)
![Alt text](gambar/image-3.png) 

## output hapus (h)
![Alt text](gambar/image-4.png) 

## output l atau lihat 
![Alt text](gambar/image-5.png)
