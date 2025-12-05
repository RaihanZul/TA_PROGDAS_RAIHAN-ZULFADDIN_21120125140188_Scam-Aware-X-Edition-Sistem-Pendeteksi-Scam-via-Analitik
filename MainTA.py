import tkinter as tk
from tkinter import ttk, messagebox
from MethodTA import ClassMethod
import threading
import time


class ClassMain:
    def __init__(self, root):
        self.root = root
        self.root.title("🛡️ Scam Aware X-Edition")
        self.root.geometry("650x580")

        # Detector
        self.detector = ClassMethod()

        # Pilihan Tema
        self.themes = {
            "Dark": {
                "bg": "#1b1f23", "fg": "white",
                "button_bg": "#2ecc71", "button_fg": "black",
                "progress": "#2ecc71"
            },
            "Light": {
                "bg": "#f4f4f4", "fg": "black",
                "button_bg": "#3498db", "button_fg": "white",
                "progress": "#3498db"
            },
            "Neon Green": {
                "bg": "#0b0f0c", "fg": "#39ff14",
                "button_bg": "#39ff14", "button_fg": "black",
                "progress": "#39ff14"
            },
            "Red Alert": {
                "bg": "#2b0c0c", "fg": "#ff6b6b",
                "button_bg": "#ff3b3b", "button_fg": "black",
                "progress": "#ff3b3b"
            },
            "Blue Cyber": {
                "bg": "#0d1b2a", "fg": "#8ecae6",
                "button_bg": "#219ebc", "button_fg": "white",
                "progress": "#219ebc"
            },
        }

        # Tema Default
        self.active_theme = "Dark"
        self.apply_theme()

        # Frame Utama
        self.frame = ttk.Frame(self.root, padding=15)
        self.frame.pack(fill="both", expand=True)

        # Judul Projek
        self.lbl_title = ttk.Label(
            self.frame,
            text="🛡️ Scam Aware X-Edition",
            font=("Arial", 22, "bold"),
            foreground=self.themes[self.active_theme]["button_bg"]
        )
        self.lbl_title.pack()

        # Theme Selector
        ttk.Label(
            self.frame,
            text="🎨 Pilih Tema UI:",
            font=("Arial", 11)
        ).pack(pady=5)

        self.cmb_theme = ttk.Combobox(
            self.frame,
            values=list(self.themes.keys()),
            state="readonly",
            width=20
        )
        self.cmb_theme.current(0)
        self.cmb_theme.pack(pady=5)
        self.cmb_theme.bind("<<ComboboxSelected>>", self.change_theme)

        ttk.Label(
            self.frame,
            text="💬 Masukkan chat/teks mencurigakan:",
            font=("Arial", 12)
        ).pack(pady=8)

        # Text Input
        self.txt_input = tk.Text(
            self.frame,
            height=8,
            relief="solid",
            borderwidth=1
        )
        self.txt_input.pack(fill="x")

        # Button Analisis
        self.btn = ttk.Button(
            self.frame,
            text="🔍 Analisis Sekarang",
            command=self.start_loading
        )
        self.btn.pack(pady=15)

        # Tombol Clear
        self.btn_clear = ttk.Button(
            self.frame,
            text="🧹 Clear Pesan",
            command=self.clear_text
        )
        self.btn_clear.pack()

        # Progress Bar
        self.progress = ttk.Progressbar(
            self.frame,
            orient="horizontal",
            mode="determinate",
            length=400
        )
        self.progress.pack(pady=5)
        self.progress.pack_forget()

        # Label hasil
        self.lbl_result = tk.Label(
            self.frame,
            text="",
            font=("Arial", 11),
            justify="left",
            bg=self.themes[self.active_theme]["bg"],
            fg=self.themes[self.active_theme]["fg"]
        )
        self.lbl_result.pack(pady=10)

        self.refresh_colors()

    # --------------------------------
    # THEME ENGINE
    # --------------------------------
    def apply_theme(self):
        theme = self.themes[self.active_theme]

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TLabel", background=theme["bg"], foreground=theme["fg"])
        style.configure("TFrame", background=theme["bg"])

        style.configure(
            "TButton",
            background=theme["button_bg"],
            foreground=theme["button_fg"],
            font=("Arial", 10, "bold"),
            padding=5
        )
        style.map(
            "TButton",
            background=[("active", theme["button_bg"])],
            foreground=[("active", theme["button_fg"])]
        )

        style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor=theme["bg"],
            background=theme["progress"],
            lightcolor=theme["progress"],
            darkcolor=theme["progress"]
        )

    def refresh_colors(self):
        theme = self.themes[self.active_theme]
        self.root.configure(bg=theme["bg"])
        self.frame.configure(style="TFrame")

        self.txt_input.configure(
            bg="#0e1317" if self.active_theme == "Dark" else theme["bg"],
            fg=theme["fg"],
            insertbackground=theme["fg"],
            highlightbackground=theme["button_bg"]
        )

        self.lbl_title.configure(foreground=theme["button_bg"])
        self.lbl_result.configure(bg=theme["bg"], fg=theme["fg"])

        self.progress.configure(style="Custom.Horizontal.TProgressbar")

    def change_theme(self, event):
        self.active_theme = self.cmb_theme.get()
        self.apply_theme()
        self.refresh_colors()

    # --------------------------------
    # CLEAR TEXT
    # --------------------------------
    def clear_text(self):
        self.txt_input.delete("1.0", tk.END)
        self.lbl_result.config(text="")

    # --------------------------------
    # BAGIAN LOADING
    # --------------------------------
    def start_loading(self):
        text = self.txt_input.get("1.0", tk.END).strip()

        if text == "":
            messagebox.showwarning("Peringatan", "⚠️ Teks tidak boleh kosong!")
            return

        self.lbl_result.config(text="⏳ Mengolah data… Harap tunggu…")
        self.progress.pack()
        self.progress["value"] = 0

        threading.Thread(target=self.simulate_loading, args=(text,)).start()

    def simulate_loading(self, text):
        for i in range(0, 101, 5):
            time.sleep(0.045)
            self.progress["value"] = i

        self.show_result(text)

    def show_result(self, text):
        result = self.detector.analyze(text)

        # Jika kosong → tampilkan sebagai string kosong
        detected = ", ".join(result["keywords"].keys()) if result["keywords"] else  "Aman, tidak ada kata mencurigakan"
        heur = ", ".join(result["heuristic"].keys()) if result["heuristic"] else "Aman, tidak ada kata mencurigakan"

        hasil = (
            f"HASIL ANALISIS\n\n"
            f"📌 Status: {result['status']}\n\n"
            f"📂 Kategori: {result['category']}\n\n"
            f"🧩 Keyword Terdeteksi:\n{detected}\n\n"
            f"🧠 Heuristik Manipulatif:\n{heur}\n\n"
            f"🎯 Skor Ancaman: {result['score']}\n"
            f"📊 Confidence: {result['confidence']}%"
        )

        self.lbl_result.config(text=hasil)
        self.progress.pack_forget()


if __name__ == "__main__":
    root = tk.Tk()
    app = ClassMain(root)
    root.mainloop()
