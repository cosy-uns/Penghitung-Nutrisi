import json
import os

class DatabaseMakanan:
    def __init__(self, file_json='./database.json'):
        self.file_json = file_json
        self.data_makanan = {}  
        self.ambil_data()

    def ambil_data(self):
        """Memuat data dari file JSON jika ada, jika tidak, maka akan dibuat buat file kosong."""
        if os.path.exists(self.file_json):
            with open(self.file_json, 'r') as file:
                try:
                    data = json.load(file)  
                    if isinstance(data, dict):
                        self.data_makanan = data
                    else:
                        self.data_makanan = {}
                except json.JSONDecodeError:
                    self.data_makanan = {}
        else:
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
            berat_makanan = makanan["berat"]#
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
            return (nilai_nutrisi.get(nutrisi, 0) * 100) / berat
        return sorted(
            self.data_makanan.items(),
            key=lambda item: nutrisi_per_100g(item[0]),
            reverse=True
        )