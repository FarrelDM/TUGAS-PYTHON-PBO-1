class induk:    #mendefinisikan kelas induk
    parent_attr = 100

    def __init__(self):
        print ("memanggil konstruktor induk:")
    
    def parent_method(self):
        print ('Memanggil metode induk')

    def set_attr(self, attr):
        induk.parent_attr = attr

    def get_attr(self):
        print ("atribut induk :", induk.parent_assr)

class anak(induk):  #mendefinisikan kelas anak
    def __init__(self):
        print ("memanggil konstruktor anak")
    
    def child_method(self):
        print ('memanggil metode anak')

c = anak()  #instansiasi kelas anak
c.child_method()    #anak memanggil metodenya

c.parent_method()   #memanggil metode induk
c.set_attr(200)     #kembalu memanggil metode induk
c.get_attr()        #kembali memanggil metode induk