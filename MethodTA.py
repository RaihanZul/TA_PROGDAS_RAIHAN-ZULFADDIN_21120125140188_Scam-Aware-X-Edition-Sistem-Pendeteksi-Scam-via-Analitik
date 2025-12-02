class ClassMethod:
    def __init__(self):

        self.keywords_scam = [
            "otp", "kode otp", "transfer", "pin", "pin atm", "rekening", "no rek",
            "blokir akun", "akun diblokir", "verifikasi", "reset password",
            "hadiah", "menang undian", "pajak hadiah", "admin biaya", "konfirmasi data",
            "data diri", "nik", "kk", "ktp", "kartu keluarga", "foto ktp", "swafoto ktp",
            "upgrade akun", "penipuan", "scam", "kode rahasia", "6 digit",
            "refund", "pengembalian dana", "klaim hadiah", "subsidi",
            "kurir", "paket ditahan", "bea cukai", "customs","akun anda akan dinonaktifkan",
            "kami dari pihak keamanan", "kode verifikasi", "verifikasi ulang akun",
            "akun anda terdeteksi", "aktivitas mencurigakan", "keamanan akun",
            "pemulihan akun","akses tidak sah","tidakan diperlukan","keamanan otomatis",
            "verifikasi kepemilikan", "validasi identitas", "informasi penting akun",
            "butuh data anda","silakan isi formulir","pembaruan data","syarat validasi",
            "cek data pribadi","pembekuan akun","akun anda dibekukan","permintaan data sensitif",
            "konfirmasi kepemilikan", "unggah identitas",
            "nomor rahasia", "kode keamanan","kode masuk","pemblokiran otomatis","notifikasi keamanan",
            "aktivasi ulang akun", "verifikasi lanjutan", "token keamanan", "akses darurat",
            "bantuan keamanan","ini sangat penting",
            "pesan resmi","kode pemulihan","info penting bank","cek rekening","pembaruan kartu atm",
            "atm terblokir","akun tersuspend","hubungi admin","bantuan pelanggan","kami dari bank",
            "pihak bank resmi","tim keamanan pusat"
        ]

        self.keywords_judol = [
            "slot", "judi", "bet", "betting", "toto", "togel", "jackpot", "deposit",
            "withdraw", "wd", "maxwin", "gacor", "bo slot", "bandar", "hoki",
            "spin", "buyspin", "bonus new member", "freebet", "slot88", "slot gacor",
            "raja judi", "slot terpercaya", "bet kecil", "modal receh",
            "parlay", "judi bola", "mix parlay", "bola online", "zeus",
            "scatter", "free spin", "freegame", "rtp live", "rtp slot",
            "room gacor", "jp max", "auto maxwin", "modal receh",
            "bonus harian", "event slot", "jp scatter",
            "sweet bonanza", "olympus", "starlight", "gates of olympus",
            "spin cepat", "turbo spin", "slot higgs",
            "chip gratis", "claim chip", "agen slot", "slot gacor hari ini",
            "info rtp", "situs resmi slot", "slot deposit pulsa",
            "deposit qris", "agen judi", "judi terpercaya",
            "gacor malam ini", "spin manual", "buy freespin", "buy bonus",
            "slot online indonesia", "casino online", "live casino",
            "pola gacor", "jam hoki", "slot login", "akun pro",
            "maxbet", "habanero", "pragmatic play", "pg soft",
            "mega win", "super win", "big win",
            "slot gampang jp", "situs taruhan", "agen bola",
            "bandar bola", "prediksi bola", "mix match"
        ]

        self.keywords_invest = [
            "profit", "cuan", "keuntungan", "trading", "robot trading",
            "auto profit", "tanpa rugi", "tanpa risiko", "return tinggi",
            "bunga per hari", "deposit investasi", "jual beli dolar", "koin",
            "crypto palsu", "mining palsu", "arisan", "arisan online", "ponzi",
            "invest cepat", "modal kecil profit besar",
            "profit harian", "jamin profit", "uang berkembang",
            "forex tipu", "binary option", "invest aman", "trading sinyal",
            "copytrade palsu","anti rugi", "dijamin profit", "pasti untung",
            "keuntungan konsisten", "return tetap", "penghasilan pasif",
            "passive income", "roi tinggi", "retur cepat",
            "investasi aman", "tanpa risiko", "keuntungan mingguan",
            "return pasti", "penghasilan otomatis", "pendapatan tetap",
            "uang cepat berkembang", "bonus harian investasi",
            "penghasilan mudah", "invest tanpa modal",
            "tim analis profesional", "admin fee investasi",
            "penarikan instan", "profit sharing palsu",
            "crypto investasi", "staking bodong",
            "mining tanpa alat", "trading tanpa belajar",
            "paket investasi premium", "level investor",
            "komunitas investor", "mentor trading",
            "profit otomatis", "sinyal akurat",
            "analisa profit", "funding member",
            "komisi sponsor", "komisi downline"
        ]

        self.heuristic_patterns = [
            "jangan bilang siapa pun",
            "jangan beri tahu orang lain",
            "segera lakukan",
            "wajib segera",
            "ini rahasia",
            "akses anda dibatasi",
            "kami tidak bertanggung jawab",
            "jika tidak segera",
            "ikuti instruksi berikut",
            "jangan tunda",
            "ini sangat mendesak",
            "waktu terbatas",
            "hanya hari ini",
            "jangan abaikan pesan ini",
            "pesan terakhir",
            "penangguhan akun",
            "akun anda bermasalah",
            "kedaluwarsa",
            "akses darurat"
        ]

    def find_keywords(self, text):
        text = text.lower()
        detected = {}

        # Perulangan
        for word in self.keywords_scam:
            if word in text:
                detected[word] = "scam"

        for word in self.keywords_judol:
            if word in text:
                detected[word] = "judol"

        for word in self.keywords_invest:
            if word in text:
                detected[word] = "invest"

        return detected

    def detect_heuristic(self, text):
        text = text.lower()
        found = {}
        for h in self.heuristic_patterns:
            if h in text:
                found[h] = "manipulatif"
        return found

    # HITUNG SKOR FINAL
    def analyze(self, text):

        detected = self.find_keywords(text)
        heur = self.detect_heuristic(text)

        score = 0

        # bobot dinamis
        for w, cat in detected.items():
            if cat == "scam":
                if "otp" in w: score += 6
                elif "hadiah" in w: score += 4
                else: score += 2

            elif cat == "judol":
                score += 3

            elif cat == "invest":
                if "tanpa rugi" in w or "dijamin" in w:
                    score += 5
                else:
                    score += 2

        # bobot heuristik
        score += len(heur) * 4

        # kategori dominan
        if len(detected) > 0:
            categories = [v for v in detected.values()]
            category = max(set(categories), key=categories.count)
        else:
            category = "tidak ada"

        # confidence
        confidence = min(100, score * 8)

        # status interpretasi
        if score >= 20:
            status = " Sangat Tinggi"
        elif score >= 12:
            status = " Tinggi"
        elif score >= 1:
            status = " Sedang"
        else:
            status = " Aman"

        return {
            "status": status,
            "score": score,
            "category": category,
            "keywords": detected,
            "heuristic": heur,
            "confidence": confidence
        }
