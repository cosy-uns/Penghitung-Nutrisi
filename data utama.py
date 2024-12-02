import tkinter as tk
from tkinter import ttk  # Import ttk untuk Treeview
from PIL import Image, ImageTk
import json
import os

class DatabaseMakanan:
    def __init__(self, file_json='./database.json'):
        self.file_json = file_json
        self.data_makanan = {}  
        self.ambil_data()

    def ambil_data(self):
        """Memuat data dari file JSON jika ada, jika tidak, buat file kosong."""
        if os.path.exists(self.file_json):
            with open(self.file_json, 'r') as file:
                try:
                    data = json.load(file)  
                    # Pastikan data yang dimuat adalah dictionary.
                    if isinstance(data, dict):
                        self.data_makanan = data
                    else:
                        self.data_makanan = {}
                except json.JSONDecodeError:
                    self.data_makanan = {}
        else:
            # Jika file JSON belum ada, buat file kosong
            with open(self.file_json, 'w') as file:
                json.dump({}, file)

    def simpan_data(self):
        """Simpan data ke file JSON."""
        with open(self.file_json, 'w') as file:
            json.dump(self.data_makanan, file, indent=4)

    def tambah_makanan(self, nama, nutrisi, berat):
        """Menambahkan makanan beserta nutrisinya dan beratnya, lalu simpan ke JSON."""
        self.data_makanan[nama] = {
            "nutrisi": nutrisi, 
            "berat": berat
            }
        self.simpan_data()

    def ambil_nama_makanan(self):
        return list(self.data_makanan.keys())

    def hitung_nutrisi_makanan(self, nama, gram):
        """Menghitung nutrisi berdasarkan berat yang dimasukkan pengguna."""
        if nama in self.data_makanan:
            makanan = self.data_makanan[nama]
            nutrisi = makanan["nutrisi"]
            berat_makanan = makanan["berat"]# Berat yang tercatat dalam database
            # Menghitung nutrisi berdasarkan perbandingan berat
            return {zat: (jumlah * gram) / berat_makanan for zat, jumlah in nutrisi.items()}
        return {}

    
    
    def urutkan_makanan_berdasarkan_nutrisi(self, nutrisi):
        """Mengembalikan daftar makanan yang diurutkan berdasarkan jumlah nutrisi tertentu."""
        if nutrisi not in ["Karbohidrat", "Lemak", "Protein", "Kalori"]:
            return []

        def nutrisi_per_100g(nama_makanan):
            """Mengembalikan nilai nutrisi per 100 gram untuk makanan yang dipilih."""
            makanan = self.data_makanan[nama_makanan]
            berat = makanan["berat"]
            nilai_nutrisi = makanan["nutrisi"]
            # Konversi nutrisi ke skala per 100 gram
            return (nilai_nutrisi.get(nutrisi, 0) * 100) / berat
        # Urutkan berdasarkan nilai nutrisi per 100 gram
        return sorted(
            self.data_makanan.items(),
            key=lambda item: nutrisi_per_100g(item[0]),
            reverse=True
        )
  
class AplikasiNutrisi:
    def __init__(self, jendela):
        self.jendela = jendela
        self.jendela.title("Kalkulator Nutrisi")
        self.database = DatabaseMakanan()

        # Atur ukuran jendela
        lebar_jendela = self.jendela.winfo_screenwidth()
        tinggi_jendela = self.jendela.winfo_screenheight()
        self.jendela.geometry(f"{lebar_jendela}x{tinggi_jendela}")

        # Muat gambar latar belakang
        self.gambar_latar = Image.open("bg Kelompok 15.png").resize((lebar_jendela, tinggi_jendela))
        self.foto_latar = ImageTk.PhotoImage(self.gambar_latar)
        
        # Label untuk latar belakang
        self.label_latar = tk.Label(self.jendela, image=self.foto_latar)
        self.label_latar.place(relwidth=1, relheight=1)

        # Frame utama tanpa latar belakang, cukup menggunakan gambar latar belakang
        self.frame_utama = tk.Frame(self.jendela)  # Pastikan frame_utama sudah didefinisikan
        self.frame_utama.place(relx=0.5, rely=0.23, anchor="center")  # Menempatkan frame di tengah jendela
        
        # Panggil fungsi `on_closing` saat aplikasi ditutup
        self.jendela.protocol("WM_DELETE_WINDOW", self.tutup_aplikasi)
        self.tampilkan_menu_utama()

    def tutup_aplikasi(self):
        """Simpan data saat aplikasi ditutup."""
        self.database.simpan_data()
        self.jendela.destroy()

    def bersihkan_frame(self):
        for widget in self.frame_utama.winfo_children():
            widget.destroy()

    def tampilkan_menu_utama(self):
        self.bersihkan_frame()

        tk.Label(self.frame_utama, text="Pilih Menu", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.frame_utama, text="Tambah Makanan", command=self.tambah_makanan_interface, width=20, height=2).pack(pady=5)
        tk.Button(self.frame_utama, text="Lihat & Urutkan Makanan", command=self.lihat_makanan, width=20, height=2).pack(pady=5)
        tk.Button(self.frame_utama, text="Hitung Nutrisi & Kalori", command=self.hitung_nutrisi_interface, width=20, height=2).pack(pady=5)
        tk.Button(self.frame_utama, text="Keluar", command=self.jendela.quit, width=20, height=2).pack(pady=5)

   
    def tambah_makanan_interface(self):
        self.bersihkan_frame()

        tk.Label(self.frame_utama, text="Tambah Makanan Baru", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.frame_utama, text="Nama Makanan:").pack()
        entri_nama = tk.Entry(self.frame_utama)
        entri_nama.pack()

        tk.Label(self.frame_utama, text="Berat Makanan (gram):").pack()
        entri_berat = tk.Entry(self.frame_utama)
        entri_berat.pack()

        tk.Label(self.frame_utama, text="Karbohidrat (g pada berat tersebut):").pack()
        entri_karbohidrat = tk.Entry(self.frame_utama)
        entri_karbohidrat.pack()

        tk.Label(self.frame_utama, text="Lemak (g pada berat tersebut):").pack()
        entri_lemak = tk.Entry(self.frame_utama)
        entri_lemak.pack()

        tk.Label(self.frame_utama, text="Protein (g pada berat tersebut):").pack()
        entri_protein = tk.Entry(self.frame_utama)
        entri_protein.pack()
        
        tk.Label(self.frame_utama, text="kalori (kkal pada berat tersebut):").pack()
        entri_kalori = tk.Entry(self.frame_utama)
        entri_kalori.pack()

        label_error = tk.Label(self.frame_utama, text="", fg="red")
        label_error.pack()

        def tambah_makanan():
            nama = entri_nama.get()
            try:
                karbohidrat = float(entri_karbohidrat.get())
                lemak = float(entri_lemak.get())
                protein = float(entri_protein.get())
                kalori = float(entri_kalori.get())
                berat = float(entri_berat.get())
                
                nutrisi = {
                    "Karbohidrat": karbohidrat,
                    "Lemak": lemak,
                    "Protein": protein,
                    "Kalori" : kalori
                }
                self.database.tambah_makanan(nama, nutrisi, berat)
                label_hasil.config(text=f"{nama} berhasil ditambahkan.")
            except ValueError:
                label_error.config(text="Kesalahan,input dengan benar.")

        label_hasil = tk.Label(self.frame_utama, text="")
        label_hasil.pack(pady=10)

        tk.Button(self.frame_utama, text="Tambahkan", command=tambah_makanan, width=20).pack(pady=10)
        tk.Button(self.frame_utama, text="Kembali", command=self.tampilkan_menu_utama, width=20).pack(pady=5)

    def lihat_makanan(self):
        self.bersihkan_frame()

        tk.Label(self.frame_utama, text="Data Makanan Saat Ini", font=("Arial", 16)).pack(pady=10)
        if self.database.data_makanan:
            tree = ttk.Treeview(self.frame_utama, columns=("Nama", "Berat", "Karbohidrat", "Lemak", "Protein","Kalori"), show="headings")
            tree.heading("Nama", text="Nama Makanan")
            tree.heading("Berat", text="Berat (gram)")
            tree.heading("Karbohidrat", text="Karbohidrat (g)")
            tree.heading("Lemak", text="Lemak (g)")
            tree.heading("Protein", text="Protein (g)")
            tree.heading("Kalori", text="kalori (kkal)")

            tree.column("Nama", anchor="w", width=200)
            tree.column("Berat", anchor="center", width=100)
            tree.column("Karbohidrat", anchor="center", width=120)
            tree.column("Lemak", anchor="center", width=100)
            tree.column("Protein", anchor="center", width=100)
            tree.column("Kalori", anchor="center", width=100)


            for makanan, data in self.database.data_makanan.items():
                nutrisi = data["nutrisi"]
                berat = data["berat"]
                tree.insert("", "end", values=(makanan, berat, nutrisi['Karbohidrat'], nutrisi['Lemak'], nutrisi['Protein'], nutrisi["Kalori"]))

            tree.pack(pady=10, fill="both", expand=True)
        else:
            tk.Label(self.frame_utama, text="Tidak ada data makanan.").pack()
        def go_sort():
            self.tampilkan_urutan_makanan()

        tk.Button(self.frame_utama, text="Urutkan Berdasarkan Nutrisi", command=go_sort, width=20).pack(pady=5)
        tk.Button(self.frame_utama, text="Kembali ke Menu Utama", command=self.tampilkan_menu_utama, width=20).pack(pady=5)

    def hitung_nutrisi_interface(self):
        self.bersihkan_frame()

        tk.Label(self.frame_utama, text="Hitung Jumlah Nutrisi", font=("Arial", 16)).pack(pady=10)

        nama_makanan = self.database.ambil_nama_makanan()
        if not nama_makanan:
            tk.Label(self.frame_utama, text="Data makanan kosong. Tambahkan makanan terlebih dahulu.").pack()
            tk.Button(self.frame_utama, text="Kembali", command=self.tampilkan_menu_utama, width=20).pack(pady=5)
            return

        tk.Label(self.frame_utama, text="Pilih Makanan:").pack()
        pilihan_makanan = tk.StringVar(self.frame_utama)
        pilihan_makanan.set(nama_makanan[0])
        tk.OptionMenu(self.frame_utama, pilihan_makanan, *nama_makanan).pack()

        tk.Label(self.frame_utama, text="Berat (gram):").pack()
        entri_berat = tk.Entry(self.frame_utama)
        entri_berat.pack()

        label_hasil = tk.Label(self.frame_utama, text="")
        label_hasil.pack(pady=10)

        def hitung():
            makanan_dipilih = pilihan_makanan.get()
            try:
                berat = float(entri_berat.get())
                nutrisi_dihitung = self.database.hitung_nutrisi_makanan(makanan_dipilih, berat)

                hasil = f"Nutrisi pada {berat} gram {makanan_dipilih}:\n"
                hasil += f"Karbohidrat: {nutrisi_dihitung.get('Karbohidrat', 0):.2f}g\n"
                hasil += f"Lemak: {nutrisi_dihitung.get('Lemak', 0):.2f}g\n"
                hasil += f"Protein: {nutrisi_dihitung.get('Protein', 0):.2f}g\n"
                hasil += f"Kalori: {nutrisi_dihitung.get('Kalori', 0):.2f}g\n"
                label_hasil.config(text=hasil)
            except ValueError:
                label_hasil.config(text="Kesalahan: Berat harus berupa angka.")

        tk.Button(self.frame_utama, text="Hitung", command=hitung, width=20).pack(pady=10)
        tk.Button(self.frame_utama, text="Kembali ke Menu Utama", command=self.tampilkan_menu_utama, width=20).pack(pady=5)

    def tampilkan_urutan_makanan(self):
        self.bersihkan_frame()

        tk.Label(self.frame_utama, text="Urutkan Berdasarkan Nutrisi (per 100 gram)", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.frame_utama, text="Pilih Nutrisi yang ingin diurutkan").pack()
        pilihan_nutrisi = tk.StringVar(self.frame_utama)
        pilihan_nutrisi.set("Karbohidrat")
        tk.OptionMenu(self.frame_utama, pilihan_nutrisi, "Karbohidrat", "Lemak", "Protein", "Kalori").pack()
        
        label_hasil = tk.Label(self.frame_utama, text="")
        label_hasil.pack(pady=10)

        def urutkan_makanan():
            nutrisi = pilihan_nutrisi.get()  # Mengambil nilai dari pilihan_nutrisi
            makanan_terurut = self.database.urutkan_makanan_berdasarkan_nutrisi(nutrisi)  # Memanggil fungsi yang benar

            if makanan_terurut:
               hasil = f"Daftar makanan berdasarkan {nutrisi} (per 100 gram):\n"
               for makanan, data in makanan_terurut:
                   berat = data["berat"]
                   nutrisi_data = data["nutrisi"]
                   nilai = (nutrisi_data.get(nutrisi, 0) * 100) / berat
                   hasil += f"{makanan}: {nilai:.2f} {nutrisi.lower()} per 100g\n"
               label_hasil.config(text=hasil)
            else:
               label_hasil.config(text="Tidak ada data untuk diurutkan.")
 
   
        tk.Button(self.frame_utama, text="Urutkan", command=urutkan_makanan, width=20).pack(pady=10)
        tk.Button(self.frame_utama, text="Kembali ke Menu Utama", command=self.tampilkan_menu_utama, width=20).pack(pady=5)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiNutrisi(root)
    root.mainloop()
