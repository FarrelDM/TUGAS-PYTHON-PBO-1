class karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji, umur):
        self.nama = nama
        self.gaji = gaji
        self.umur = umur
        karyawan.jumlah_karyawan += 1
    
    def tampilkan_jumlah(self):
        print("total karyawan: ", karyawan.jumlah_karyawan)
    
    def tampilkan_profil(self):
        print("nama: ", self.nama)
        print("gaji: ", self.gaji)
        print()