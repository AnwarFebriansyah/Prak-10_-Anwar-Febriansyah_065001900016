# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:46:24 2021

@author: HP
"""
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