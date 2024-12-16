import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from database import DatabaseMakanan
from tkcalendar import DateEntry  # Import DateEntry dari tkcalendar
import json

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
        self.frame_utama = tk.Frame(self.jendela, bg= "#f6efe4")
        self.frame_utama.place(relx=0.5, rely=0.4, anchor="center")
        
        # Label hasil
        self.label_hasil = tk.Label(self.frame_utama, text="", font=("Arial", 14), bg="#f6efe4", fg="black")
        self.label_hasil.pack(pady=10)
        
        self.label_error = tk.Label(self.frame_utama, text="", fg="red")  # Definisikan label_error di sini
        self.label_error.pack()

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
        ButtonLihatKonsumsi = tk.Button(self.frame_utama, text="Lihat Konsumsi Harian", font=("Arial", 15), bg="#dd9871", fg="black", command=self.lihat_konsumsi_harian, width=25, height=2)
        ButtonLihatKonsumsi.pack(pady=5)
        ButtonKeluar = tk.Button(self.frame_utama, text="Keluar", font=("Arial", 15), bg= "#dd9871", fg= "black", command=self.jendela.quit, width=25, height=2)
        ButtonKeluar.pack(pady=5)
        
        
        
    def tambah_makanan_interface(self):
        self.bersihkan_frame()
        LabelTambahMKN = tk.Label(self.frame_utama, text="Tambah Makanan Baru", font=("Arial", 16), bg= "#f6efe4", fg= "black")
        LabelTambahMKN.pack(pady=10)
        self.frame_utama.place(relx=0.5, rely=0.45, anchor="center")
        
        LabelNama = tk.Label(self.frame_utama, text="Nama Makanan:", font=("Arial", 10), bg= "#f6efe4", fg= "black")
        LabelNama.pack()
        self.entri_nama = tk.Entry(self.frame_utama)
        self.entri_nama.pack()

        LabelBerat = tk.Label(self.frame_utama, text="Berat Makanan (gram):", font=("Arial", 10), bg= "#f6efe4", fg= "black")
        LabelBerat.pack()
        self.entri_berat = tk.Entry(self.frame_utama)
        self.entri_berat.pack()

        LabelKarbo = tk.Label(self.frame_utama, text="Karbohidrat (g pada berat tersebut):", font=("Arial", 10), bg= "#f6efe4", fg= "black")
        LabelKarbo.pack()
        self.entri_karbohidrat = tk.Entry(self.frame_utama)
        self.entri_karbohidrat.pack()

        LabelLemak = tk.Label(self.frame_utama, text="Lemak (g pada berat tersebut):", font=("Arial", 10), bg= "#f6efe4", fg= "black")
        LabelLemak.pack()
        self.entri_lemak = tk.Entry(self.frame_utama)
        self.entri_lemak.pack()

        LabelProtein = tk.Label(self.frame_utama, text="Protein (g pada berat tersebut):", font=("Arial", 10), bg= "#f6efe4", fg= "black")
        LabelProtein.pack()
        self.entri_protein = tk.Entry(self.frame_utama)
        self.entri_protein.pack()
        
        LabelKalori = tk.Label(self.frame_utama, text="Kalori (kkal pada berat tersebut):", font=("Arial", 10), bg= "#f6efe4", fg= "black")
        LabelKalori.pack()
        self.entri_kalori = tk.Entry(self.frame_utama)
        self.entri_kalori.pack()

        label_error = tk.Label(self.frame_utama, text="", fg="red")
        label_error.pack()

        def tambah_makanan():
            nama = self.entri_nama.get()
            try:
                karbohidrat = float(self.entri_karbohidrat.get())
                lemak = float(self.entri_lemak.get())
                protein = float(self.entri_protein.get())
                kalori = float(self.entri_kalori.get())
                berat = float(self.entri_berat.get())
                
                nutrisi = {
                    "Karbohidrat": karbohidrat,
                    "Lemak": lemak,
                    "Protein": protein,
                    "Kalori" : kalori
                }
                self.database.tambah_makanan(nama, nutrisi, berat)
                self.label_hasil.config(text=f"{nama} berhasil ditambahkan.")
                self.label_error.config(text="")  # Reset label_error
            except ValueError:
                self.label_error.config(text="Kesalahan,input dengan benar.")

        label_hasil = tk.Label(self.frame_utama, text="")
        label_hasil.pack(pady=10)

        ButtonTambahMKN = tk.Button(self.frame_utama, text="Tambahkan", font=("Arial", 15), bg= "#dd9871", fg= "black", command=tambah_makanan, width=15)
        ButtonTambahMKN.pack(pady=5)
        ButtonKembali = tk.Button(self.frame_utama, text="Kembali", font=("Arial", 15), bg= "#dd9871", fg= "black", command=self.tampilkan_menu_utama, width=15)
        ButtonKembali.pack(pady=5)

    def lihat_konsumsi_harian(self):
        self.bersihkan_frame()

        tk.Label(self.frame_utama, text="Konsumsi Harian", font=("Arial", 16), bg="#f6efe4", fg="black").pack(pady=10)

        try:
            with open("konsumsi_harian.json", "r") as file:
                data = json.load(file)

            # Frame for Treeview and Scrollbar
            frame_tree = tk.Frame(self.frame_utama)
            frame_tree.pack(pady=10, fill="both", expand=True)

            # Create Treeview
            tree = ttk.Treeview(frame_tree, columns=("Tanggal", "Karbohidrat", "Lemak", "Protein", "Kalori", "Makanan"), show="headings")
            tree.heading("Tanggal", text="Tanggal")
            tree.heading("Karbohidrat", text="Karbohidrat (g)")
            tree.heading("Lemak", text="Lemak (g)")
            tree.heading("Protein", text="Protein (g)")
            tree.heading("Kalori", text="Kalori (kkal)")
            tree.heading("Makanan", text="Makanan")

            # Initialize column widths (adjust as needed)
            column_widths = {
                "Tanggal": 100,
                "Karbohidrat": 120,
                "Lemak": 100,
                "Protein": 100,
                "Kalori": 100,
                "Makanan": 200  # Initial width for "Makanan }
            }
            # Insert data into the Treeview
            for entry in data:
                tanggal = entry["tanggal"]
                total_nutrisi = entry["total_nutrisi"]
                makanan_list = ", ".join([f"{item['makanan']} ({item['berat']}g)" for item in entry["konsumsi_harian"]])
                tree.insert("", "end", values=(tanggal, total_nutrisi["Karbohidrat"], total_nutrisi["Lemak"], total_nutrisi["Protein"], total_nutrisi["Kalori"], makanan_list))

                # Update column widths based on the length of the data
                column_widths["Tanggal"] = max(column_widths["Tanggal"], len(tanggal) * 10)
                column_widths["Karbohidrat"] = max(column_widths["Karbohidrat"], len(str(total_nutrisi["Karbohidrat"])) * 10)
                column_widths["Lemak"] = max(column_widths["Lemak"], len(str(total_nutrisi["Lemak"])) * 10)
                column_widths["Protein"] = max(column_widths["Protein"], len(str(total_nutrisi["Protein"])) * 10)
                column_widths["Kalori"] = max(column_widths["Kalori"], len(str(total_nutrisi["Kalori"])) * 10)
                column_widths["Makanan"] = max(column_widths["Makanan"], len(makanan_list) * 10)

            # Set column widths
            for col, width in column_widths.items():
                tree.column(col, anchor="center", width=width)

            # Add a scrollbar
            scrollbar = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side="right", fill="y")
            tree.pack(pady=10, fill="both", expand=True)

        except FileNotFoundError:
            tk.Label(self.frame_utama, text="File konsumsi_harian.json tidak ditemukan.", bg="#f6efe4", fg="red").pack()
        except json.JSONDecodeError:
            tk.Label(self.frame_utama, text="Kesalahan dalam membaca file JSON.", bg="#f6efe4", fg="red").pack()
        except Exception as e:
            tk.Label(self.frame_utama, text=f"Kesalahan: {str(e)}", bg="#f6efe4", fg="red").pack()

        ButtonKembali = tk.Button(self.frame_utama, text="Kembali", font=("Arial", 15), bg="#dd9871", fg="black", command=self.tampilkan_menu_utama, width=15)
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
                tree.insert("", "end", values=(makanan, berat, nutrisi.get("Karbohidrat", 0), nutrisi.get("Lemak", 0), nutrisi.get("Protein", 0), nutrisi.get("Kalori", 0)))

            tree.pack(pady=10, fill="both", expand=True)
        else:
            tk.Label(self.frame_utama, text="Tidak ada data makanan.").pack()

        # Tombol untuk urutan berdasarkan nutrisi
        ButtonUrut = tk.Button(self.frame_utama, text="Urutkan Berdasarkan Nutrisi", font=("Arial", 15), bg="#dd9871", fg="black", command=self.tampilkan_urutan_makanan, width=25)
        ButtonUrut.pack(pady=5)

        # Tombol untuk kembali ke menu utama
        ButtonKembali = tk.Button(self.frame_utama, text="Kembali ke Menu Utama", font=("Arial", 15), bg="#dd9871", fg="black", command=self.tampilkan_menu_utama, width=25)
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

        ButtonUrut = tk.Button(self.frame_utama, text="Urutkan", font=("Arial", 15), bg="#dd9871", fg="black", command=urutkan_makanan, width=20)
        ButtonUrut.pack(pady=5)
        ButtonKembali = tk.Button(self.frame_utama, text="Kembali ke Menu Utama", font=("Arial", 15), bg="#dd9871", fg="black", command=self.tampilkan_menu_utama, width=20)
        ButtonKembali.pack(pady=5)

    def hitung_nutrisi_interface(self):
        self.bersihkan_frame()

        LabelHitung = tk.Label(self.frame_utama, text="Hitung Jumlah Nutrisi dan Kalori Harian", font=("Arial", 16), bg="#f6efe4", fg="black")
        LabelHitung.pack(pady=10)

        # Input untuk tanggal menggunakan DateEntry
        LabelTanggal = tk.Label(self.frame_utama, text="Pilih Tanggal:", font=("Arial", 16), bg="#f6efe4", fg="black")
        LabelTanggal.pack()
        self.entri_tanggal = DateEntry(self.frame_utama, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.entri_tanggal.pack()

        # Input untuk makanan menggunakan Listbox
        LabelMakanan = tk.Label(self.frame_utama, text="Pilih Makanan (Ctrl untuk memilih lebih dari satu):", font=("Arial", 16), bg="#f6efe4", fg="black")
        LabelMakanan.pack()

        makanan_options = list(self.database.data_makanan.keys())  # Mengambil daftar makanan dari database
        self.listbox_makanan = tk.Listbox(self.frame_utama, selectmode=tk.MULTIPLE, height=5)
        for makanan in makanan_options:
            self.listbox_makanan.insert(tk.END, makanan)
        self.listbox_makanan.pack()

        label_makanan_pilih = tk.Label(self.frame_utama, text="", bg="#f6efe4", fg="black")
        label_makanan_pilih.pack(pady=10)

        # Label untuk mengarahkan input berat
        label_berat = tk.Label(self.frame_utama, text="Masukkan Berat untuk Makanan yang Dipilih (gram):", font=("Arial", 14), bg="#f6efe4", fg="black")
        label_berat.pack(pady=10)

        self.entri_berat_list = []  # List untuk menyimpan entri berat
        frame_berat = tk.Frame(self.frame_utama, bg="#f6efe4")  # Frame untuk entri berat
        frame_berat.pack()

        def update_weight_entries():
            # Hapus entri berat sebelumnya
            for widget in frame_berat.winfo_children():
                widget.destroy()
            self.entri_berat_list.clear()

            # Ambil makanan yang dipilih
            selected_indices = self.listbox_makanan.curselection()
            for index in selected_indices:
                makanan = makanan_options[index]

                # Label untuk nama makanan
                tk.Label(frame_berat, text=f"Berat {makanan} (gram):", font=("Arial", 10), bg="#f6efe4", fg="black").pack(anchor="w")
                # Entri untuk berat makanan
                entri_berat = tk.Entry(frame_berat)
                entri_berat.pack()
                self.entri_berat_list.append(entri_berat)

        # Bind event untuk memperbarui entri berat setiap kali ada makanan yang dipilih
        self.listbox_makanan.bind("<<ListboxSelect>>", lambda event: update_weight_entries())

        self.label_hasil = tk.Label(self.frame_utama, text="", font=("Arial", 14), bg="#f6efe4", fg="black")
        self.label_hasil.pack(pady=10)

        def hitung_kalori_harian():
            try:
                tanggal = self.entri_tanggal.get()
                selected_indices = self.listbox_makanan.curselection()
                total_nutrisi = {"Karbohidrat": 0, "Lemak": 0, "Protein": 0, "Kalori": 0}

                # Iterasi melalui makanan yang dipilih
                for idx, entry in zip(selected_indices, self.entri_berat_list):
                    makanan = makanan_options[idx]
                    berat = float(entry.get())  # Berat makanan dari entri
                    data_makanan = self.database.data_makanan[makanan]
                    nutrisi = data_makanan["nutrisi"]
                    berat_awal = data_makanan["berat"]

                    # Hitung kontribusi nutrisi per makanan
                    for nutrisi_name, value in nutrisi.items():
                        total_nutrisi[nutrisi_name] += (value * berat) / berat_awal

                # Tampilkan hasil
                hasil = f"Total Nutrisi pada {tanggal}:\n"
                hasil += f"Karbohidrat: {total_nutrisi['Karbohidrat']:.2f} g\n"
                hasil += f"Lemak: {total_nutrisi['Lemak']:.2f} g\n"
                hasil += f"Protein: {total_nutrisi['Protein']:.2f} g\n"
                hasil += f"Kalori: {total_nutrisi['Kalori']:.2f} kkal"
                self.label_hasil.config(text=hasil)
            except ValueError:
                self.label_hasil.config(text="Harap masukkan berat dalam format angka!", fg="red")

        ButtonHitung = tk.Button(self.frame_utama, text="Hitung Kalori Harian", font=("Arial", 16), bg="#dd9871", fg="black", command=hitung_kalori_harian, width=20)
        ButtonHitung.pack(pady=5)

        ButtonSimpan = tk.Button(self.frame_utama, text="Simpan Konsumsi Harian", font=("Arial", 16), bg="#dd9871", fg="black", command=self.simpan_konsumsi_harian, width=20)
        ButtonSimpan.pack(pady=5)

        ButtonKembali = tk.Button(self.frame_utama, text="Kembali ke Menu Utama", font=("Arial", 16), bg="#dd9871", fg="black", command=self.tampilkan_menu_utama, width=20)
        ButtonKembali.pack(pady=5)

    def simpan_konsumsi_harian(self):
        """Simpan data konsumsi harian ke file JSON."""
        try:
            tanggal = self.entri_tanggal.get()  # Menggunakan self.
            selected_indices = self.listbox_makanan.curselection()  # Menggunakan self.
            total_nutrisi = {"Karbohidrat": 0, "Lemak": 0, "Protein": 0, "Kalori": 0}
            makanan_options = list(self.database.data_makanan.keys())  # Mendapatkan daftar makanan dari database
            konsumsi_harian = []  # List untuk menyimpan makanan dan berat yang dipilih

            # Iterasi melalui makanan yang dipilih
            for idx, entry in zip(selected_indices, self.entri_berat_list):
                makanan = makanan_options[idx]
                berat = float(entry.get())  # Berat makanan dari entri
                data_makanan = self.database.data_makanan[makanan]
                nutrisi = data_makanan["nutrisi"]
                berat_awal = data_makanan["berat"]

                # Hitung kontribusi nutrisi per makanan
                for nutrisi_name, value in nutrisi.items():
                    total_nutrisi[nutrisi_name] += (value * berat) / berat_awal

                # Simpan makanan dan berat yang dipilih
                konsumsi_harian.append({"makanan": makanan, "berat": berat})

            # Simpan data ke konsumsi_harian.json
            with open("konsumsi_harian.json", "r+") as file:
                try:
                    data = json.load(file)  # Pastikan data adalah list
                except json.JSONDecodeError:
                    data = []  # Jika file kosong, buat list baru

                # Pastikan data adalah list sebelum menambahkan
                if not isinstance(data, list):
                    data = []  # Jika data bukan list, buat list baru

                data.append({
                    "tanggal": tanggal,
                    "total_nutrisi": total_nutrisi,
                    "konsumsi_harian": konsumsi_harian  # Menyimpan makanan dan berat
                })

                file.seek(0)
                json.dump(data, file, indent=4)

            self.label_hasil.config(text="Data konsumsi harian berhasil disimpan.", fg="green")  # Menggunakan self.
        except Exception as e:
            self.label_hasil.config(text=f"Kesalahan: {str(e)}", fg="red")  # Menggunakan self.