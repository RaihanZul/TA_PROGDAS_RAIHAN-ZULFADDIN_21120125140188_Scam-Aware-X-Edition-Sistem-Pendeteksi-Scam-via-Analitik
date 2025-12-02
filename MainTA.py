import tkinter as tk
from tkinter import ttk, messagebox
from MethodTA import ClassMethod
import threading
import time

class ClassMain:
    def __init__(self, root):
        self.root = root
        self.root.title("🛡️ Scam Aware X-Edition")
        self.root.geometry("650x480")
        self.root.configure(bg="#1b1f23")  # background gelap modern

        # Style Kontras
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TLabel", background="#1b1f23", foreground="white")
        style.configure("TFrame", background="#1b1f23")
        style.configure("TButton", font=("Arial", 10, "bold"),
                        background="#2ecc71", foreground="black")
        style.map("TButton",
                  background=[("active", "#27ae60")],
                  foreground=[("active", "white")])

        style.configure("Green.Horizontal.TProgressbar",
                        troughcolor="#0e1317",
                        bordercolor="#0e1317",
                        background="#2ecc71",
                        lightcolor="#27ae60",
                        darkcolor="#27ae60")

        # Detector Logic
        self.detector = ClassMethod()

        # Frame utama
        frame = ttk.Frame(self.root, padding=15)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame,
                  text="🛡️ Scam Aware X-Edition",
                  font=("Arial", 22, "bold"),
                  foreground="#2ecc71").pack()

        ttk.Label(frame,
                  text="💬 Masukkan chat/teks mencurigakan:",
                  font=("Arial", 12)).pack(pady=8)

        self.txt_input = tk.Text(frame, height=8, bg="#0e1317",
                                 fg="white", insertbackground="white",
                                 relief="solid", borderwidth=1,
                                 highlightbackground="#2ecc71")
        self.txt_input.pack(fill="x")

        self.btn = ttk.Button(frame, text="🔍 Analisis Sekarang",
                              command=self.start_loading)
        self.btn.pack(pady=15)

        # Progress Bar (Loading)
        self.progress = ttk.Progressbar(frame,
                                        style="Green.Horizontal.TProgressbar",
                                        orient="horizontal",
                                        mode="determinate",
                                        length=400)
        self.progress.pack(pady=5)
        self.progress.pack_forget()

        self.lbl_result = ttk.Label(frame, text="", font=("Arial", 11), foreground="white")
        self.lbl_result.pack(pady=10)

    # Mulai loading bar
    def start_loading(self):
        text = self.txt_input.get("1.0", tk.END).strip()

        if text == "":
            messagebox.showwarning("Peringatan", "⚠️ Teks tidak boleh kosong!")
            return

        self.lbl_result.config(text="⏳ Mengolah data… Harap tunggu…")
        self.progress.pack()
        self.progress["value"] = 0

        # Thread agar GUI tidak freeze
        threading.Thread(target=self.simulate_loading, args=(text,)).start()

    # Proses loading untuk olah data
    def simulate_loading(self, text):
        for i in range(0, 101, 5):
            time.sleep(0.05)
            self.progress["value"] = i

        # Setelah selesai -> tampilkan hasil
        self.show_result(text)

    #  Menampilkan output program
    def show_result(self, text):
        status, detected, score = self.detector.analyze(text)

        emoji_status = "🟢" if "Aman" in status else "🟡" if "Rendah" in status else "🟠" if "Sedang" in status else "🔴"

        hasil = (
            f"{emoji_status} *HASIL ANALISIS*\n\n"
            f"📌 Status: {status}\n\n"
            f"🧩 Kata Terdeteksi:\n{detected}\n\n"
            f"🎯 Skor Ancaman: {score}"
        )

        self.lbl_result.config(text=hasil)
        self.progress.pack_forget()


# MAIN PROGRAM
if __name__ == "__main__":
    root = tk.Tk()
    app = ClassMain(root)
    root.mainloop()
