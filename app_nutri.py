import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from database import DatabaseMakanan

class AplikasiNutrisi:
    def __init__(self, jendela):
        self.jendela = jendela
        self.jendela.title("Kalkulator Nutrisi")
        self.database = DatabaseMakanan()

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
        self.frame_utama = tk.Frame(self.jendela, bg= "#f6efe4")  # Pastikan frame_utama sudah didefinisikan
        self.frame_utama.place(relx=0.5, rely=0.4, anchor="center")  # Menempatkan frame di tengah jendela
        
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

        LabelPilihMenu = tk.Label(self.frame_utama, text="Pilih Menu", font=("Arial", 25), bg= "#f6efe4", fg= "black")
        LabelPilihMenu.pack(pady=10)
        ButtonTambah = tk.Button(self.frame_utama, text="Tambah Makanan", font=("Arial", 15), bg= "#dd9871", fg= "black", command=self.tambah_makanan_interface, width=25, height=2)
        ButtonTambah.pack(pady=5)
        ButtonLihat = tk.Button(self.frame_utama, text="Lihat & Urutkan Makanan", font=("Arial", 15), bg= "#dd9871", fg= "black", command=self.lihat_makanan, width=25, height=2)
        ButtonLihat.pack(pady=5)
        ButtonHitung = tk.Button(self.frame_utama, text="Hitung Nutrisi & Kalori", font=("Arial", 15), bg= "#dd9871", fg= "black", command=self.hitung_nutrisi_interface, width=25, height=2)
        ButtonHitung.pack(pady=5)
        ButtonKeluar = tk.Button(self.frame_utama, text="Keluar", font=("Arial", 15), bg= "#dd9871", fg= "black", command=self.jendela.quit, width=25, height=2)
        ButtonKeluar.pack(pady=5)  

   
    def tambah_makanan_interface(self):
        self.bersihkan_frame()
        LabelTambahMKN = tk.Label(self.frame_utama, text="Tambah Makanan Baru", font=("Arial", 16), bg= "#f6efe4", fg= "black")
        LabelTambahMKN.pack(pady=10)
        self.frame_utama.place(relx=0.5, rely=0.45, anchor="center")  # Menempatkan frame di tengah jendela

        LabelNama = tk.Label(self.frame_utama, text="Nama Makanan:", font=("Arial", 10), bg= "#f6efe4", fg= "black")
        LabelNama.pack()
        entri_nama = tk.Entry(self.frame_utama)
        entri_nama.pack()

        LabelBerat = tk.Label(self.frame_utama, text="Berat Makanan (gram):", font=("Arial", 10), bg= "#f6efe4", fg= "black")
        LabelBerat.pack()
        entri_berat = tk.Entry(self.frame_utama)
        entri_berat.pack()

        LabelKarbo = tk.Label(self.frame_utama, text="Karbohidrat (g pada berat tersebut):", font=("Arial", 10), bg= "#f6efe4", fg= "black")
        LabelKarbo.pack()
        entri_karbohidrat = tk.Entry(self.frame_utama)
        entri_karbohidrat.pack()

        LabelLemak = tk.Label(self.frame_utama, text="Lemak (g pada berat tersebut):", font=("Arial", 10), bg= "#f6efe4", fg= "black")
        LabelLemak.pack()
        entri_lemak = tk.Entry(self.frame_utama)
        entri_lemak.pack()

        LabelProtein = tk.Label(self.frame_utama, text="Protein (g pada berat tersebut):", font=("Arial", 10), bg= "#f6efe4", fg= "black")
        LabelProtein.pack()
        entri_protein = tk.Entry(self.frame_utama)
        entri_protein.pack()
        
        LabelKalori = tk.Label(self.frame_utama, text="Kalori (kkal pada berat tersebut):", font=("Arial", 10), bg= "#f6efe4", fg= "black")
        LabelKalori.pack()
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

        ButtonTambahMKN = tk.Button(self.frame_utama, text="Tambahkan", font=("Arial", 15), bg= "#dd9871", fg= "black", command=tambah_makanan, width=15)
        ButtonTambahMKN.pack(pady=5)
        ButtonKembali = tk.Button(self.frame_utama, text="Kembali", font=("Arial", 15), bg= "#dd9871", fg= "black", command=self.tampilkan_menu_utama, width=15)
        ButtonKembali.pack(pady=5)

    def lihat_makanan(self):
        self.bersihkan_frame()

        tk.Label(self.frame_utama, text="Data Makanan Saat Ini", font=("Arial", 16), bg="#f6efe4", fg="black").pack(pady=10)
    
        if self.database.data_makanan:
            # Membuat Treeview
            tree = ttk.Treeview(
                self.frame_utama, 
                columns=("Nama", "Berat", "Karbohidrat", "Lemak", "Protein", "Kalori"), 
                show="headings"
            )
        
            # Menentukan heading
            tree.heading("Nama", text="Nama Makanan")
            tree.heading("Berat", text="Berat (gram)")
            tree.heading("Karbohidrat", text="Karbohidrat (g)")
            tree.heading("Lemak", text="Lemak (g)")
            tree.heading("Protein", text="Protein (g)")
            tree.heading("Kalori", text="Kalori (kkal)")

            # Menentukan lebar kolom dan perataan
            tree.column("Nama", anchor="center", width=200)
            tree.column("Berat", anchor="center", width=100)
            tree.column("Karbohidrat", anchor="center", width=120)
            tree.column("Lemak", anchor="center", width=100)
            tree.column("Protein", anchor="center", width=100)
            tree.column("Kalori", anchor="center", width=100)

            # Mengosongkan isi Treeview sebelumnya
            for i in tree.get_children():
                tree.delete(i)

            # Mengisi Treeview dengan data makanan
            for makanan, data in self.database.data_makanan.items():
                nutrisi = data["nutrisi"]
                berat = data["berat"]
                tree.insert("", "end", values=(makanan,berat, nutrisi.get("Karbohidrat", 0), nutrisi.get("Lemak", 0), nutrisi.get("Protein"),nutrisi.get("Kalori", 0) ) )

            tree.pack(pady=10, fill="both", expand=True)
        else:
            tk.Label(self.frame_utama, text="Tidak ada data makanan.").pack()

        # Tombol untuk urutan berdasarkan nutrisi
        ButtonUrut = tk.Button(self.frame_utama, text="Urutkan Berdasarkan Nutrisi", font=("Arial", 15), bg="#dd9871", fg="black",  command=self.tampilkan_urutan_makanan, width=25)
        ButtonUrut.pack(pady=5)

        # Tombol untuk kembali ke menu utama
        ButtonKembali = tk.Button(self.frame_utama, text="Kembali ke Menu Utama", font=("Arial", 15), bg="#dd9871", fg="black",  command=self.tampilkan_menu_utama,  width=25)
        ButtonKembali.pack(pady=5)
    def tampilkan_urutan_makanan(self):
        self.bersihkan_frame()

        LabelUrutkan = tk.Label(self.frame_utama, text="Urutkan Berdasarkan Nutrisi (per 100 gram)", font=("Arial", 16), bg="#f6efe4", fg="black")
        LabelUrutkan.pack(pady=10)

        LabelPilih = tk.Label(self.frame_utama, text="Pilih Nutrisi yang ingin diurutkan", font=("Arial", 16), bg="#f6efe4", fg="black")
        LabelPilih.pack()
        pilihan_nutrisi = tk.StringVar(self.frame_utama)
        pilihan_nutrisi.set("Karbohidrat")
        MenuNutrisi = tk.OptionMenu(self.frame_utama, pilihan_nutrisi, "Karbohidrat", "Lemak", "Protein", "Kalori")
        MenuNutrisi.pack(pady=5)

        # Treeview untuk menampilkan tabel
        tampilan_tabel = ttk.Treeview(self.frame_utama, columns=("Nama", "Nutrisi per 100g"), show="headings")
        tampilan_tabel.heading("Nama", text="Nama Makanan")
        tampilan_tabel.heading("Nutrisi per 100g", text="Nutrisi (per 100g)")

        tampilan_tabel.column("Nama", anchor="center", width=200)
        tampilan_tabel.column("Nutrisi per 100g", anchor="center", width=150)
        tampilan_tabel.pack(pady=10, fill="both", expand=True)

        def urutkan_makanan():
            nutrisi = pilihan_nutrisi.get()
            makanan_terurut = self.database.urutkan_makanan_berdasarkan_nutrisi(nutrisi)

            # Hapus semua data di Treeview sebelum menambahkan sebuah data baru
            for item in tampilan_tabel.get_children():
                tampilan_tabel.delete(item)

            if makanan_terurut:
                for makanan, data in makanan_terurut:
                    berat = data["berat"]
                    nutrisi_data = data["nutrisi"]
                    nilai = (nutrisi_data.get(nutrisi, 0) * 100) / berat
                    tampilan_tabel.insert("", "end", values=(makanan, f"{nilai:.2f} {nutrisi.lower()}"))
            else:
                 tampilan_tabel.insert("", "end", values=("Tidak ada data", ""))

        ButtonUrut = tk.Button(self.frame_utama, text="Urutkan", font=("Arial", 15), bg= "#dd9871", fg= "black", command=urutkan_makanan, width=20)
        ButtonUrut.pack(pady=5)
        ButtonKembali = tk.Button(self.frame_utama, text="Kembali ke Menu Utama", font=("Arial", 15), bg= "#dd9871", fg= "black", command=self.tampilkan_menu_utama, width=20)
        ButtonKembali.pack(pady=5)
        
    def hitung_nutrisi_interface(self):
        self.bersihkan_frame()

        LabelHitung = tk.Label(self.frame_utama, text="Hitung Jumlah Nutrisi", font=("Arial", 16), bg= "#f6efe4", fg= "black")
        LabelHitung.pack(pady=10)   

        nama_makanan = self.database.ambil_nama_makanan()
        if not nama_makanan:
            LabelError1 = tk.Label(self.frame_utama, text="Data makanan kosong. Tambahkan makanan terlebih dahulu.", font=("Arial", 16), bg= "#f6efe4", fg= "black")
            LabelError1.pack(pady=10)
            ButtonKembali = tk.Button(self.frame_utama, text="Kembali", font=("Arial", 16), bg= "#f6efe4", fg= "black", command=self.tampilkan_menu_utama, width=20)
            ButtonKembali.pack(pady=5)
            return

        LabelPilihMakan = tk.Label(self.frame_utama, text="Pilih Makanan:", font=("Arial", 16), bg= "#f6efe4", fg= "black")
        LabelPilihMakan.pack()
        pilihan_makanan = tk.StringVar(self.frame_utama)
        pilihan_makanan.set(nama_makanan[0])
        OptionMakanan = tk.OptionMenu(self.frame_utama, pilihan_makanan, *nama_makanan)
        OptionMakanan.pack(pady=5)

        LabelBerat = tk.Label(self.frame_utama, text="Berat (gram):", font=("Arial", 16), bg= "#f6efe4", fg= "black")
        LabelBerat.pack()
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
                hasil += f"Kalori: {nutrisi_dihitung.get('Kalori', 0):.2f}kkal\n"
                label_hasil.config(text=hasil, bg="#f6efe4")
            except ValueError:
                label_hasil.config(text="Kesalahan: Berat harus berupa angka.")

        ButtonHitung = tk.Button(self.frame_utama, text="Hitung", font=("Arial", 16), bg= "#dd9871", fg= "black", command=hitung, width=20)
        ButtonHitung.pack(pady=5)
        ButtonKembali = tk.Button(self.frame_utama, text="Kembali ke Menu Utama", font=("Arial", 16), bg= "#dd9871", fg= "black", command=self.tampilkan_menu_utama, width=20)
        ButtonKembali.pack(pady=5)