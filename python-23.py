# Decorators
# Python'da decorator'lar, argüman olarak fonksiyon alıp,
# sonuçta yine fonksiyon döndüren fonksiyonlara denir.

def linkYap(f):
    def yaz():
        return "<a href='http://www." + f() + ".com'>Link</a"
    return yaz

def linkYap2(g):
    def yaz2():
        return "<a href='http://www." + g() + ".org'>Link</a"
    return yaz2
def adres():
    return "google"
a = linkYap(adres)
print(a())

def adres():
    return "facebook"
a = linkYap(adres)
print(a())
def adres():
    return "instagram"
a = linkYap(adres)
print(a())
def adres():
    return "snapchat"
a = linkYap(adres)
print(a())
def adres():
    return "mackolik"
a = linkYap(adres)
print(a())
def adres():
    return "galatasaray"
a = linkYap2(adres)
print(a())
def adres():
    return "udemy"
a = linkYap(adres)
print(a())
def adres():
    return "youtube"
a = linkYap(adres)
print(a())
def adres():
    return "youtube"
a = linkYap(adres)
print(a())

@linkYap2
def adr():
    return "python"
print(adr())

@linkYap    #fonksiyonu decoratora bağla
def adr():
    return "python"
print(adr())
