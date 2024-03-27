import random

class Personel:
    def __init__(self, adi, departmani, calisma_yili, maasi):
        self.adi = adi
        self.departmani = departmani
        self.calisma_yili = calisma_yili
        self.maasi = maasi
        self.kod = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))

class Firma:
    def __init__(self, firma_adi, kurulus_yili):
        self.firma_adi = firma_adi
        self.kurulus_yili = kurulus_yili
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        print("Firma Çalışanları:")
        for personel in self.personel_listesi:
            print("Kod:", personel.kod)
            print("Adı:", personel.adi)
            print("Departmanı:", personel.departmani)
            print("Çalışma Yılı:", personel.calisma_yili)
            print("Maaşı:", personel.maasi)
            print("----------------------")

    def maaş_zammı(self, personel_kod, zam_orani):
        for personel in self.personel_listesi:
            if personel.kod == personel_kod:
                personel.maasi *= (1 + zam_orani / 100)
                print("Maaş güncellendi.")
                break
        else:
            print("Belirtilen kodda bir personel bulunamadı.")

    def personel_cikart(self, personel_kod):
        for personel in self.personel_listesi:
            if personel.kod == personel_kod:
                self.personel_listesi.remove(personel)
                print("Personel başarıyla çıkarıldı.")
                break
        else:
            print("Belirtilen kodda bir personel bulunamadı.")

# Menüyü gösteren fonksiyon
def menu_goster():
    print("1. Personel Ekle")
    print("2. Personel Listele")
    print("3. Maaş Zammı Uygula")
    print("4. Personel Çıkar")
    print("5. Çıkış")

# Ana kod kısmı
firma = Firma("ABC Şirketi", 2000)

while True:
    menu_goster()
    secim = input("Yapmak istediğiniz işlemi seçiniz: ")

    if secim == "1":
        adi = input("Personelin adını giriniz: ")
        departmani = input("Personelin departmanını giriniz: ")
        calisma_yili = int(input("Personelin çalışma yılını giriniz: "))
        maasi = float(input("Personelin maaşını giriniz: "))
        yeni_personel = Personel(adi, departmani, calisma_yili, maasi)
        firma.personel_ekle(yeni_personel)
        print("Personel başarıyla eklendi. Kodu:", yeni_personel.kod)

    elif secim == "2":
        firma.personel_listele()

    elif secim == "3":
        personel_kod = input("Maaşına zam yapmak istediğiniz personelin kodunu giriniz: ")
        zam_orani = float(input("Zam oranını giriniz (%): "))
        firma.maaş_zammı(personel_kod, zam_orani)

    elif secim == "4":
        personel_kod = input("Çıkarmak istediğiniz personelin kodunu giriniz: ")
        firma.personel_cikart(personel_kod)

    elif secim == "5":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
