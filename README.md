# Kelas A, Kelompok 15, Daftar Anggota Team:
1. I0324002, Anastasya Gerarda Siahaan, anastasyasiahaan
2. I0324020, Muhammad Farhan Ahda Fadhila, farhanahda
3. I0324027, Yamilla Kirana Paramita, yamillakirana
4. I0324040, Cosy Shofwan, cosy-uns
# Penghitung Nilai Nutrisi dalam Makanan
Program ini adalah penghitung nutrisi makanan berbasis desktop yang membantu pengguna mengelola kandungan nutrisi makanan. Aplikasi ini memiliki dua fungsi utama: menghitung nutrisi makanan yang sudah ada atau menambahkan makanan baru ke dalam basis data. Pengguna dapat memilih makanan dari daftar, memasukkan jumlah porsinya, dan aplikasi akan menghitung total nutrisi seperti lemak, protein, vitamin, dan mineral. Jika pengguna ingin menambah makanan baru, aplikasi menyediakan antarmuka untuk memasukkan informasi nutrisi. Setelah data makanan baru ditambahkan, daftar lengkap makanan, termasuk data lama dan baru, akan ditampilkan. Aplikasi ini memastikan basis data selalu terkini dan sesuai kebutuhan diet pengguna.
# Fitur Aplikasi
1. Tambah Makanan
   fitur ini berfungsi untuk menambahkan data-data pada makanan yang terdiri dari nama makanan,berat makanan tersebut dalam gram, serta nutrisi-nutrisi yang terkandung di dalam makanan tersebut seperti karbohidrat,lemak,protein dalam satuan gram dan kalori dalam satuan kkal. 
2. Lihat & urutkan makanan
   fitur ini berfungsi untuk melihat data-data makanan yang telah ditambahkan sebelumnya dalam bentuk tabel, selain itu terdapat fitur tambahan di mana pengguna bisa untuk memilih melihat urutan makanan berdasarkan nutrisi tertinggi yang dipilih oleh pengguna dalam per 100 gram.
3. Hitung Nutrisi & kalori
   fitur ini berfungsi untuk menghitung jumlah nutrisi dalam makanan dalam jumlah berat yang berbeda-beda yang bertujuan untuk mengukur asupan makanan yang pas untuk tubuh.
4. Lihat Konsumsi Harian
   fitur ini berfungsi untuk melihat makanan apa saja yang sudah kita hitung nutrisinya dan kita simpan data perhitungannya.
#  Library Yang Digunakan
1. tkinter: Untuk membuat GUI aplikasi.
2. ttk: Untuk membuat widget dengan tema yang lebih modern.
3. PIL (Pillow): Untuk memanipulasi gambar (misalnya membuka dan menampilkan gambar latar belakang).
4. json: Untuk menangani data dalam format JSON (seperti membaca dan menulis data makanan).
5. os: Untuk berinteraksi dengan sistem file (memeriksa dan menangani file).
# Diagram Alir
1. Diagram Alir 1

![Flowchart penghitung nutrisi](https://github.com/user-attachments/assets/0df9982e-381e-4cbe-8660-1d5cf41fb2e8)

2. Diagram Alir 2
   
![Diagram Tanpa Judul drawio (1)](https://github.com/user-attachments/assets/ba4f257e-436d-422a-b3fb-9b578712ba77)

3. Diagram Alir 3 (FIX)
![Flowchart-PenghitungNutrisi drawio](https://github.com/user-attachments/assets/4a6c6ece-5040-407b-85ed-051b923e9b05)

4. Diagram Alir 4 (revisi)
![Flowchart-PenghitungNutrisi-v4 drawio](https://github.com/user-attachments/assets/dca050ba-8a53-418a-a05c-bc1b23fb1c7d)

Program dimulai dengan menampilkan menu utama yang memberikan pengguna empat pilihan: menambahkan data makanan, menghitung jumlah nutrisi, menampilkan data makanan, atau keluar dari sistem.
- Jika pengguna memilih untuk menambahkan data makanan, sistem akan meminta pengguna untuk menginput nama makanan, kadar kalori, karbohidrat, protein, lemak, dan berat makanan (dalam gram). Data yang dimasukkan kemudian disimpan, dan pengguna dapat melihat daftar makanan yang telah diinput.
- Jika pengguna memilih untuk menghitung jumlah nutrisi, sistem akan meminta pengguna untuk memilih jenis makanan dari data yang sudah ada, makanan bisa lebih dari satu pilihan, dan memasukkan berat makanan yang diinginkan. Berdasarkan informasi tersebut, sistem menghitung total nutrisi (kalori, karbohidrat, protein, dan lemak) sesuai dengan berat makanan yang dimasukkan, dan hasilnya ditampilkan kepada pengguna. Setelahnya, pengguna bisa memilih untuk menyimpan data hitungan nutrisi makanan yang nantinya dapat dilihat di fitur lihat konsumsi harian.
- Pilihan ketiga adalah menampilkan data makanan yang sudah tersimpan. Dalam opsi ini, pengguna juga diberikan kesempatan untuk mengurutkan data makanan berdasarkan salah satu dari empat kriteria: kalori, karbohidrat, protein, atau lemak. Sistem kemudian akan menampilkan daftar makanan yang diurutkan sesuai dengan kriteria yang dipilih.
- Pilihan lainnya adalah melihat data konsumsi harian. Dalam opsi ini, pengguna dapat melihat data makanan yang telah dihitung nutrisinya. Agar data makanan yang telah dihitung nutisinya muncul, pengguna harus terlebih dahulu menghitung nutrisi makanan di fitur hitung nutrisi makanan dan memilih opsi simpan perhitungan nutrisi.
- Jika pengguna memilih opsi keluar, sistem akan berhenti dan proses berakhir. Diagram ini dirancang untuk membantu pengguna dalam mengelola informasi makanan dan nutrisinya secara sistematis dan interaktif.

# SiteMap
![Sitemap Penghitung Nutrisi](https://github.com/user-attachments/assets/b9b2de2a-4e98-4c60-94c5-ea8624df7462)
