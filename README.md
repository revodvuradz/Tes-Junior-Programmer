📦 Django Produk Management System

Aplikasi ini dibuat untuk memenuhi technical test programmer menggunakan Django Framework sebagai backend dan Bootstrap untuk tampilan antarmuka. Sistem ini mampu mengambil data dari API eksternal, menyimpannya ke database, serta menyediakan fitur lengkap untuk mengelola data produk.

🚀 Fitur Utama

- Mengambil data produk dari API eksternal
- Menyimpan data produk ke database
- Menampilkan produk dengan filter status "bisa dijual"
- Fitur pencarian real-time tanpa perlu menekan tombol Enter
- Pagination otomatis (maksimal 10 data per halaman)
- Tampilan responsif menggunakan Bootstrap

🚀 Fitur CRUD Produk:
- Tambah produk
- Edit produk
- Hapus produk dengan konfirmasi
- Validasi form:
 -- Nama produk wajib diisi
 -- Harga harus berupa angka

🧠 Struktur Database

📌 Tabel Kategori
| Field         | Keterangan           |
| ------------- | -------------------- |
| id_kategori   | Primary Key          |
| nama_kategori | Nama kategori produk |

📌 Tabel Status
| Field       | Keterangan    |
| ----------- | ------------- |
| id_status   | Primary Key   |
| nama_status | Status produk |

📌 Tabel Produk
| Field       | Keterangan                    |
| ----------- | ----------------------------- |
| id_produk   | Primary Key                   |
| nama_produk | Nama produk                   |
| harga       | Harga produk                  |
| kategori_id | Foreign Key ke tabel Kategori |
| status_id   | Foreign Key ke tabel Status   |

📹 Video Dokumentasi

Berikut video dokumentasi yang memperlihatkan hasil akhir program dan cara kerja fitur-fiturnya:
🔗 https://drive.google.com/file/d/1x_e5PDSr45L1W0CnF3UFmh0d3yeMO0Dj/view?usp=sharing

🧩 Penutup

Aplikasi ini dibangun sesuai dengan ketentuan soal dengan fokus pada:
- Struktur database yang rapi
- Validasi input yang aman
- Tampilan antarmuka yang bersih dan responsif