import os
import shutil
import sys

#fungsi tampilan utama
def tampilanUtama():
    print(''' 
    [1]     Membuat directori
    [2]     Lis directori
    [3]     Menghapus directori
    [4]     Mengubah directori
    [5]     Membuat file format txt   
    [6]     Membaca file format txt
    [7]     Update file txt
    [8]     Delete file txt
    [9]     Shutdown
    [10]    Restart
    [11]    Keluar''')
    while True: 
        try:
            pilihan = int(input("Inputkan pilihan anda: "))
            if pilihan == 1:
                createDirectory()
            elif pilihan == 2:
                listDirectori()
            elif pilihan == 3:
                deleteDirectory()
            elif pilihan == 4:
                changeDirectory()
            elif pilihan == 5:
                makeFileTxt()
            elif pilihan == 6: 
                readFileTxt()
            elif pilihan == 7:
                updateFileTxt()
            elif pilihan == 8:
                deleteFileTxt()    
            elif pilihan == 9:
                shutdown()
            elif pilihan == 10: 
                restart()
            elif pilihan == 11:
                sys.exit(0)
            else:
                print("Pilihan anda tidak tersedia")
        except ValueError:
            print("Inputkan angka dari 1 sampai 11")

#fungsi membuat direktori
def createDirectory():
    buat_directori = str(input("Nama directory: "))
    os.mkdir(buat_directori)
    print(f"Direktori {buat_directori} berhasil dibuat")    
    tampilanUtama()

#fungsi menghapus direktori
def deleteDirectory():
    hapus_directory = str(input("Nama directory yang ingin dihapus: "))
    try:
        os.rmdir(hapus_directory)
        print(f"Direktori {hapus_directory} berhasil dihapus")
    except: 
        shutil.rmtree(hapus_directory)
        print(f"Direktori {hapus_directory} berhasil dihapus")
    tampilanUtama()
    
#fungsi list directory
def listDirectori(): 
    disini = os.listdir()
    print(disini)
    tampilanUtama()

#fungsi mengubah atau berpindah direntory
def changeDirectory():
    print(os.listdir())
    ubah_directori = str(input("Pindah ke: "))
    os.chdir(ubah_directori)
    print(os.getcwd())
    kembali = os.path.dirname(os.path.abspath(__file__))
    print("Apakah anda ingin kembali ke directory awal?") 
    print("tekan 1 untuk kembali, tekan 2 untuk tetap pada directori")
    pilih = int(input("pilih: "))
    if pilih == 1 :
        os.chdir(kembali)
        tampilanUtama()
    elif pilih == 2 :
        tampilanUtama()
    else :
        print("Pilihan anda tidak ada...")

#fungsi membuat file dengan format txt
def makeFileTxt():
    nama_file = str(input("Nama file: "))
    ketik_file = input("Inputkan ketikan: ")
    with  open(nama_file, "a") as f:   
        f.write(ketik_file)
    tampilanUtama()

#fungsi menghapus file
def deleteFileTxt():
    nama_file = str(input("Nama file: "))
    os.remove(nama_file)
    tampilanUtama()

#fungsi membaca file
def readFileTxt():
    nama_file = str(input("Nama file: "))
    f = open(nama_file, "r")
    print(f.read())
    tampilanUtama()

#fungsi update file
def updateFileTxt():
    pilih = (input("Pilih file yang ingin diupdate: "))
    with open(pilih, "r") as f:
        print(f.read())     
    with open(pilih, "w") as f:
        ketikan = str(input("Masukan ketikan: "))
        f.write(ketikan)
    print(f"file {pilih} berhasil di-update")
    tampilanUtama()
def shutdown():
    os.system("shutdown now")
def restart():
    os.system("shudwown -r now")
#memanggil fungsi tampilanUtama   
tampilanUtama()