dataMhs = {}                                                                                     
print("==================================================================")
print("|      PROGRAM INPUT NILAI MAHASISWA MENGGUNAKAN DICTIONARY      |")
print("==================================================================")

while True:                                                                                  
    c = input("\n(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar: ")                                
    if (c.lower() == 't'):                                               
        print('\nTambah Data Mahasiswa Baru')
        nama= input("Masukkan Nama\t\t: ")                                        
        nim= input("Masukkan NIM\t\t: ")                                         
        nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))                              
        nilaiUts= int(input("Masukkan Nilai UTS\t: "))                                   
        nilaiUas= int(input("Masukkan Nilai UAS\t: "))                                    
        nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)              
        dataMhs[nama]= nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir                         
        print("\nData Berhasil Ditambahkan!")
    elif (c.lower() == 'u'):                                                                    
        print('\nMengubah Data Mahasiswa')
        nama = input("Masukkan Nama: ")                                                         
        if nama in dataMhs.keys():                              
            nim= input("Masukkan NIM Baru\t: ")                              
            nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))                           
            nilaiUts= int(input("Masukkan Nilai UTS\t: "))                           
            nilaiUas= int(input("Masukkan Nilai UAS\t: "))                           
            nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)          
            dataMhs[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir                      
            print("\nData Berhasil Di Update!")
        else:                                                                                    
            print("Data tidak ditemukan!")                                                       
    elif (c.lower() == 'c'):                                                                    
        print('\nCari Data Mahasiswa')
        nama = input("Masukan Nama:  ")                                                          
        if nama in dataMhs.keys():                                                               
            print("\n                   DAFTAR NILAI MAHASISWA                   ")
            print("==============================================================")
            print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==============================================================")
            print("| {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(nama, nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir)) 
            print("==============================================================")
        else:
            print("Datanya {0} Tidak Ada ".format(nama))                                        
    elif (c.lower() == 'h'):                                                                    
        nama = input("Masukkan Nama Yang Akan Dihapus:  ")                                                        
        if nama in dataMhs.keys():                                                              
            del dataMhs[nama]                                                                   
            print("Data Telah dihapus!")
        else:
            print("Data Mahasiswa Tidak Ada".format(nama))                                     
    elif (c.lower() == 'l'):                                                                    
        if dataMhs.items():                                                                     
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            i = 0
            for x in dataMhs.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))  
            print("==================================================================")
        else:
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                          TIDAK ADA DATA!                       |")
            print("==================================================================")         
    elif (c.lower() == 'k'):                                                                   
        print('\n')
        print(23*'=')
        print("Nama\t: Irfan Maulana Falah\nKelas\t: TI.21.C5\nNIM\t: 312110560")
        print(23*'=')
        break                                                                                 

    else:
        print("Pilih menu yang tersedia: ")                                                    