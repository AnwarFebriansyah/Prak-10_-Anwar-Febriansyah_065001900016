class Mahasiswa:
    def __init__(self):
        self.nama = ""
        self.prak1 = 0
        self.prak2 = 0
        self.prak3 = 0
    def getRata(self):
        return (self.prak1+self.prak2+self.prak3)/3

datamhs = list()
while True:
    print("PROGRAM LIST")
    print(" 1. Input Data")
    print(" 2. View Data")
    print(" 3. Hitung Nilai Rata-Rata Praktikum Tiap Mahasiswa")
    print(" 4. Hitung Nilai Rata-Rata Tiap Praktikum")
    print(" 5. Mencari Nilai Rata-Rata Praktikum Mahasiswa")
    print(" 6. Update Nilai Praktikum Mahasiswa")
    print(" 7. Exit")
 
    menu = input("Pilih menu yang tersedia : ")
    if menu == '1':
        print("[1. INPUT DATA]")
        mhs = Mahasiswa()
        mhs.nama = input("Masukkan nama mahasiswa : ")
        mhs.prak1 = int(input("Masukkan nilai praktikum 1 : "))
        mhs.prak2 = int(input("Masukkan nilai praktikum 2 : "))
        mhs.prak3 = int(input("Masukkan nilai praktikum 3 : "))
        datamhs.append(mhs)
    elif menu == '2':
        print("[2. VIEW DATA]")
        print("{:^15}|{:^8}|{:^8}|{:^8}".format("NAMA","PRAK 1","PRAK 2","PRAK 3"))
        for mhs in datamhs:
            print("{:^15} {:^8} {:^8} {:^8}".format(mhs.nama,mhs.prak1,mhs.prak2,mhs.prak3))
    elif menu == '3':
        print("[3. HITUNG RATA-RATA PRAK TIAP MAHASISWA]")
        for mhs in datamhs:
            print(mhs.nama+" = "+str(mhs.getRata()))
    elif menu == '4':
        print("[4. HITUNG RATA-RATA TIAP PRAK]")
        print("Rerata Prak 1 : "+str(sum(mhs.prak1 for mhs in datamhs)/len(datamhs)))
        print("Rerata Prak 2 : "+str(sum(mhs.prak2 for mhs in datamhs)/len(datamhs)))
        print("Rerata Prak 3 : "+str(sum(mhs.prak3 for mhs in datamhs)/len(datamhs)))
    elif menu == '5':
        print("[5. MENCARI NILAI RATA-RATA PRAK TIAP MAHASISWA]")
        key_nama = input("Masukkan nama mahasiswa : ")
        for mhs in datamhs:
            if mhs.nama == key_nama:
                print("Rerata nilai praktikum "+mhs.nama+" = "+str(mhs.getRata()))
                break
    elif menu == '6':
        print("[6. UPDATE NILAI PRAK MAHASISWA]")
        key_nama = input("Masukkan nama mahasiswa : ")
        for mhs in datamhs:
            if mhs.nama == key_nama:
                prakke = input("Ingin update nilai praktikum ke-:")
                if prakke == '1':
                    mhs.prak1 = int(input("Nilai Baru : "))
                elif prakke == '2':
                    mhs.prak2 = int(input("Nilai Baru : "))
                elif prakke == '3':
                    mhs.prak3 = int(input("Nilai Baru : "))
                break
    elif menu == '7':
        print("[7. EXIT]")
        exit("TERIMA KASIH!")
    print("")
