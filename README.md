# 📌 Otomasi Pengambilan Mata Kuliah KRS



Script ini dibuat untuk membantu mahasiswa melakukan **otomasi pengisian Kartu Rencana Studi (KRS)** secara cepat menggunakan **Python + Selenium**.

Program dapat berjalan dalam **mode manual** (sesuai jadwal jam/menit/detik KRS dibuka) maupun **mode otomatis** (melakukan pengecekan berkala hingga semua mata kuliah berhasil diamankan).



---



## 🚀 Fitur

- Login otomatis ke portal mahasiswa.

- Mendukung **mode manual** (start sesuai waktu yang ditentukan).

- Mendukung **mode otomatis** (looping hingga matkul didapat).

- Membaca akun, mata kuliah, dan kelas dari file eksternal.

- Validasi pengguna dengan Google Spreadsheet.

- Output status berhasil/gagal setiap percobaan.



---



## 🛠️ Persyaratan

Pastikan sudah menginstall:

- Python 3.8 atau lebih baru

- Google Chrome

- [ChromeDriver](https://chromedriver.chromium.org/downloads) (versi sesuai Chrome Anda)

- Library Python:

```bash
pip install selenium pandas numpy
```


## 📑 Cara Penggunaan



1. Clone repository

&nbsp;  ```bash

&nbsp;  git clone https://github.com/irpan06/KRS-Automation.git

&nbsp;  cd KRS-Automation



2. Isi data akun

&nbsp;  - `nim.txt` → masukkan NIM Anda  

&nbsp;  - `pw.txt` → masukkan password  

&nbsp;  - `matkul.txt` → daftar kode/nama mata kuliah, contoh:  

&nbsp;    ```txt

&nbsp;    FIS101, MAT102, KIM103

&nbsp;    ```

&nbsp;  - `kelas.txt` → daftar kelas yang sesuai, contoh:  

&nbsp;    ```txt

&nbsp;    A, B, C

&nbsp;    ```



3. Jalankan program

   ```bash

   python krs.py



4. Pilih mode

&nbsp;  - `1` Mode Manual → program akan menunggu hingga jam, menit, detik yang ditentukan.  

&nbsp;  - `2` Mode Otomatis → program akan looping hingga semua matkul berhasil diamankan.





## ⚠️ Disclaimer



- Script ini dibuat hanya untuk tujuan **pembelajaran**.  

- Risiko penggunaan sepenuhnya ditanggung pengguna.  

- Gunakan secara bijak sesuai aturan akademik masing-masing universitas.  

























