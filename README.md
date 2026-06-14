Clickjacking Vulnerability Checker

Deskripsi
Clickjacking Vulnerability Checker merupakan aplikasi web sederhana berbasis Flask yang digunakan untuk memeriksa apakah suatu website memiliki perlindungan terhadap serangan clickjacking.
Aplikasi akan mengirim request ke URL yang dimasukkan pengguna, kemudian memeriksa HTTP Response Header seperti X-Frame-Options dan Content-Security-Policy (frame-ancestors) untuk menentukan apakah website tersebut aman atau rentan terhadap serangan clickjacking.

Fitur
- Input URL website
- Pemeriksaan header HTTP
- Deteksi proteksi X-Frame-Options
- Deteksi Content-Security-Policy
- Menampilkan status aman atau rentan
- Dijalankan menggunakan Docker

Teknologi yang Digunakan
- Python 3.12
- Flask
- Requests
- Docker
- Docker Compose
- HTML

Cara Menjalankan Aplikasi
Menjalankan Secara Langsung
python app.py

Buka browser:
http://localhost:15000

Menjalankan Menggunakan Docker
docker compose up --build

Buka browser:
http://localhost:15000

Struktur Project
tugas-jarkom-tk25/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md

Cara Kerja

1. Pengguna memasukkan URL website.
2. Aplikasi mengirim HTTP Request ke website tujuan.
3. Aplikasi membaca HTTP Response Header.
4. Sistem memeriksa keberadaan:
   - X-Frame-Options
   - Content-Security-Policy (frame-ancestors)
5. Hasil ditampilkan sebagai:
   - Terlindungi dari Clickjacking
   - Rentan terhadap Clickjacking

Author
Dafidz Afriday Islamika
D3 Teknik Komputer
Universitas Duta Bangsa Surakarta

Nama : Dafidz Afriday Islamika
Prodi: D3 Teknik Komputer
Universitas Duta Bangsa Surakarta
