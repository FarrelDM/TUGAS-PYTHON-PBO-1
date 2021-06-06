class karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        karyawan.jumlah_karyawan += 1
    
    def tampilkan_jumlah(self):
        print("total karyawan: ", karyawan.jumlah_karyawan)
    
    def tampilkan_profil(self):
        print("nama: ", self.nama)
        print("gaji: ", self.gaji)

#membuat objek pertama dari kelas karyawan
karyawan1 = karyawan("Saras", 1000000)
#membuat objek kedua dari kelas karyawan
karyawan2 = karyawan("Buba", 2000000)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
print("Total karyawan: ", karyawan.jumlah_karyawan)