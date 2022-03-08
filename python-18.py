#Polymorphism - Çok Biçimlilik

class kedi:
    def ses(self):
        print("miyav")

class kopek:
    def ses(self):
        print("hav hav")
class kus:
    def ses(self):
        print("cik cik")


def hayvanSesi(hayvan):
    hayvan.ses()

ke = kedi()
ko = kopek()
ku = kus()

hayvanSesi(ke)
hayvanSesi(ko)
hayvanSesi(ku)
