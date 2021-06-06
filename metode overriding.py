class induk:
    def my_method(self):
        print("memanggil metode induk")

class anak(induk):
    def my_method(self):
        print("memanggil metode anak")

c = anak
c.my_method()
