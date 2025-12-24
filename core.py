import random
import os
from pathlib import Path

class FakeTR:
    def __init__(self, data_dosyasi=None):
        self.veriler = {}
        if data_dosyasi is None:
            base_path = Path(__file__).parent
            data_dosyasi = base_path / "data.txt"
        self.dosya_oku(data_dosyasi)

    def dosya_oku(self, dosya_adi):
        mevcut_kategori = None
        try:
            with open(dosya_ani, "r", encoding="utf-8") as f:
                for satir in f:
                    satir = satir.strip()
                    if not satir or satir.startswith("#"):
                        continue
                    if satir.startswith("###") and satir.endswith("###"):
                        mevcut_kategori = satir[3:-3].strip()
                        self.veriler[mevcut_kategori] = []
                    elif mevcut_kategori:
                        if satir:
                            self.veriler[mevcut_kategori].append(satir.strip())
        except FileNotFoundError:
            raise FileNotFoundError(f"{dosya_adi} dosyası bulunamadı!")

    def rastgele(self, kategori):
        liste = self.veriler.get(kategori, [])
        if not liste:
            return f"[HATA: {kategori} kategorisi boş veya yok]"
        return random.choice(liste)


    def isim(self, cinsiyet="rastgele"):
        if cinsiyet == "Erkek" or (cinsiyet == "rastgele" and random.random() < 0.5):
            return self.rastgele("IsimErkek")
        else:
            return self.rastgele("IsimKadin")

    def soyisim(self):
        return self.rastgele("Soyisim")

    def ad_soyad(self, cinsiyet="rastgele"):
        return f"{self.isim(cinsiyet)} {self.soyisim()}"

    def tc(self):
        return ''.join(str(random.randint(0,9)) for _ in range(11))

    def telefon(self):
        return f"05{random.randint(30,59)} {random.randint(100,999)} {random.randint(10,99)} {random.randint(10,99)}"

    def il(self):
        return self.rastgele("Il")

    def burc(self):
        return self.rastgele("Burc")

    def telefon_model(self):
        return self.rastgele("TelefonModel")

    def meslek(self):
        return self.rastgele("Meslek")

    def araba(self):
        return self.rastgele("ArabaMarkaModel")

    def ip(self):
        return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"

    def adres(self):
        sokak_tipi = random.choice(["Cadde", "Sokak", "Bulvarı", "Mahallesi"])
        return f"{self.il()} {random.randint(1,999)} {sokak_tipi} No:{random.randint(1,150)} D:{random.randint(1,40)}"
