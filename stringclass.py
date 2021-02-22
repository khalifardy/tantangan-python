# pertanyaan buatlah sebuah class string dengan minimal dua metode, untuk mengambil input
# Dan mencetak input dengan string huruf besar semua

class String(object):
    def __init__(self):
        self.string = " "

    def get_string(self):
        self.string = input("masukan kata :") 

    def print_string(self):
        print(self.string.upper())



nama = String()
nama.get_string()
nama.print_string()

#fungsi Upper(), untuk mengembalikan string menjadi huruf besar semua


        
        