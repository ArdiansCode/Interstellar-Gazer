# Interstellar Gazer

Interstellar Gazer adalah aplikasi berbasis web yang dirancang untuk membantu para fotografer astrofotografi, astronom amatir, dan pemburu bintang dalam menemukan waktu terbaik untuk melihat atau memotret langit malam. 

Aplikasi ini menganalisis data perkiraan cuaca selama 15 hari ke depan menggunakan parameter cuaca tingkat lanjut dan algoritma machine learning untuk merekomendasikan 10 waktu paling ideal.

---

## Fitur Utama

* **Analisis Rekomendasi Otomatis**: Sistem mengevaluasi data cuaca secara simultan untuk menentukan status kelayakan langit malam menjadi dua kategori, yaitu SUPER IDEAL atau CUKUP OKE.
* **Indikator Parameter Langit**: Menampilkan informasi penting yang dibutuhkan untuk pengamatan bintang, meliputi tutupan awan (cloud cover), fase bulan (moon phase), jarak pandang (visibility dalam satuan kilometer), dan kecepatan angin (wind speed).
* **Antarmuka Sinematik Modern**: Memanfaatkan Tailwind CSS v4 dengan tema warna Gray Monochrome yang bersih. Dilengkapi latar belakang video bintang bergerak yang transparan serta efek full-screen loading overlay.
* **Pencarian Lokasi Spesifik**: Mendukung input lokasi hingga tingkat desa atau kecamatan untuk akurasi data cuaca yang lebih baik.

---

## Teknologi dan Prasyarat

Aplikasi ini dibangun menggunakan teknologi berikut:

* **Backend**: Python 3.x, Flask Framework
* **Pengolahan Data**: Pandas, NumPy, Scikit-Learn
* **Frontend**: HTML5, Tailwind CSS v4 (via CDN), Vanilla JavaScript
* **Sumber Data**: Visual Crossing Weather API

---

## Struktur Direktori Proyek

```text
interstellar-gazer/
│
├── app.py                  # Berkas utama aplikasi Flask dan logika analitik
├── requirements.txt         # Daftar dependensi library Python
├── README.md               # Dokumentasi proyek
│
├── static/                 # Direktori untuk aset statis frontend
│   ├── bg-stars.mp4        # Video latar belakang bintang bergerak (dioptimasi < 3MB)
│   └── logostar.png        # Logo aplikasi / Favicon browser
│
└── templates/              # Direktori untuk template HTML
    └── index.html          # Halaman antarmuka utama aplikasi
```

---

## Panduan Instalasi dan Penggunaan

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek di lingkungan lokal Anda:

### 1. Klon Repositori
Unduh proyek ini ke komputer lokal Anda menggunakan Git:
```bash
git clone https://github.com
cd interstellar-gazer
```

### 2. Buat dan Aktifkan Virtual Environment
Disarankan menggunakan virtual environment agar dependensi tidak bertabrakan dengan proyek lain:

* **Pengguna Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
* **Pengguna macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instal Dependensi Python
Instal seluruh library yang diperlukan melalui berkas requirements.txt:
```bash
pip install -r requirements.txt
```
Catatan: Jika berkas requirements.txt belum tersedia, Anda dapat menginstal library utama secara manual menggunakan perintah:
`pip install Flask pandas requests scikit-learn`

### 4. Konfigurasi API Key
Buka berkas app.py, lalu cari variabel API_KEY dan ganti dengan kunci API valid yang Anda dapatkan dari Visual Crossing Weather:
```python
API_KEY = "ISI_DENGAN_API_KEY_VISUAL_CROSSING_ANDA"
```

### 5. Jalankan Aplikasi Flask
Mulai server lokal dengan menjalankan perintah berikut:
```bash
python app.py
```
Setelah server aktif, buka browser Anda dan akses alamat http://127.0.0.1:5000.

---

## Parameter Penilaian Kelayakan Langit

Aplikasi menentukan status rekomendasi berdasarkan standar observasi astronomi berikut:

* **Tutupan Awan (Cloud Cover)**: Semakin rendah persentase tutupan awan, semakin tinggi peluang langit terbuka. Nilai di bawah 20% sangat direkomendasikan.
* **Fase Bulan (Moon Phase)**: Cahaya bulan yang terlalu terang dapat menyamarkan cahaya bintang. Aplikasi memprioritaskan waktu di sekitar fase bulan baru (new moon) dengan persentase cahaya rendah.
* **Jarak Pandang (Visibility)**: Menunjukkan transparansi udara dalam satuan Kilometer (KM). Jarak pandang di atas 10 KM menandakan udara bersih bebas kabut atau polusi tebal.
* **Kecepatan Angin (Wind Speed)**: Angin yang terlalu kencang dapat mengaburkan fokus lensa kamera saat melakukan teknik long-exposure.

---

## Catatan Pengembangan

* **Optimasi Kinerja**: Pastikan berkas bg-stars.mp4 di dalam folder static telah dikompresi dengan baik (disarankan di bawah 3 MB). Video yang terlalu besar dapat memperlambat waktu pemuatan halaman pertama kali.
* **Penanganan Transparansi**: Elemen UI utama dibungkus menggunakan kelas koordinasi indeks z (relative z-10) untuk memastikan teks dan tabel tetap berada di atas lapisan video latar belakang dan dapat berinteraksi dengan normal.
