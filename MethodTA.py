
class ClassMethod:
    def __init__(self):
       
        # SCAM / PENIPUAN UMUM
        self.keywords_scam = [
            "otp", "kode otp", "transfer", "pin", "pin atm", "rekening", "no rek",
            "blokir akun", "akun diblokir", "verifikasi", "reset password",
            "hadiah", "menang undian", "pajak hadiah", "admin biaya", "konfirmasi data",
            "data diri", "nik", "kk", "ktp", "kartu keluarga", "foto ktp", "swafoto ktp",
            "upgrade akun", "penipuan", "scam", "kode rahasia", "6 digit",
            "refund", "pengembalian dana", "klaim hadiah", "subsidi",
            "kurir", "paket ditahan", "bea cukai", "customs"
        ]

        # JUDI ONLINE (JUDOL)
        self.keywords_judol = [
            "slot", "judi", "bet", "betting", "toto", "togel", "jackpot", "deposit",
            "withdraw", "wd", "maxwin", "gacor", "bo slot", "bandar", "hoki",
            "spin", "buyspin", "bonus new member", "freebet", "slot88", "slot gacor",
            "raja judi", "slot terpercaya", "bet kecil", "modal receh"
        ]

        # INVESTASI BODONG / TRADING PALSU
        self.keywords_invest = [
            "profit", "cuan", "keuntungan", "trading", "robot trading",
            "auto profit", "tanpa rugi", "tanpa risiko", "return tinggi",
            "bunga per hari", "deposit investasi", "jual beli dolar", "koin",
            "crypto palsu", "mining palsu", "arisan", "arisan online", "ponzi",
            "invest cepat", "modal kecil profit besar",
            "profit harian", "jamin profit", "uang berkembang",
            "forex tipu", "binary option", "invest aman", "trading sinyal",
            "copytrade palsu"
        ]

    # Method untuk mencari kata
    def find_keywords(self, text):
        text = text.lower()
        detected = []

        # Perulangan (Modul 3)
        for w in self.keywords_scam + self.keywords_judol + self.keywords_invest:
            if w.lower() in text:
                detected.append(w)

        return detected

    # Hitung skor
    def calculate_score(self, detected):
        score = 0

        # Pengkondisian (Modul 2)
        for w in detected:
            if w in self.keywords_scam:
                score += 2
            elif w in self.keywords_judol:
                score += 3
            elif w in self.keywords_invest:
                score += 1

        return score

    # Analisis akhir
    def analyze(self, text):
        detected = self.find_keywords(text)
        score = self.calculate_score(detected)

        if score >= 12:
            status = "⚠️ Sangat Tinggi — Potensi penipuan serius!"
        elif score >= 6:
            status = "⚠️ Sedang — Waspada, banyak indikasi."
        elif score >= 1:
            status = "⚠️ Rendah — Ada indikasi mencurigakan."
        else:
            status = "✔ Aman — Tidak ditemukan tanda scam."

        return status, detected, score
