class siswa:
    def __init__ (self):
        self_nama = "bagus"
    
    #memberi tahu bahwa nama adalah properti dari objek
    @property
    def nama(self):
        pass

    #memberikan fngsi getter pada property nama
    @nama.getter
    def nama(self):
        return self.__nama

    #memberikan fungsi setter pada property nama
    @nama.setter
    def nama(self, nama):
        self.__nama = nama

m = siswa()
m.nama + "abdul"
print(m.nama)