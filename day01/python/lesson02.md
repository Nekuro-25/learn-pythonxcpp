## Lesson 02 - Data Types, Casting, & F-Strings

# A. Learning Objectives

1. Membedakan tipe data teks (String) dan angka bulat (Integer).
2. Memahami mengapa fungsi input() membutuhkan Type Conversion (Casting).
3. Menggunakan fitur F-Strings untuk membuat output lebih rapi dan "Pythonic".

# B. Theory

1. String (Teks) vs Integer (Angka)
Di mata Python, angka 5 dan "5" berbeda.
5 adalah Integer, "5" String. 5 + 5 menjadi 10, "5" tambah "5" menjadi 55.
2. Type Conversion (Casting)
Kode input() selalu menghasilkan string (SELALU). Gunakan int(input(..)) untuk mengkonversi ke integer.
3. F-Strings (Format Strings)
Python modern punya F-Strings, dengan huruf f di depan tanda kutip, lalu variabel dalam kurung kurawal {}.

# C. Example

nama_hacker = "Nekuro"
target_port = 80

# Cara lama (seperti practice01.py)
print("Hacker " + nama_hacker + " menyerang port " + str(target_port))

# Cara modern (F-String) -> Lebih mudah dibaca!
print(f"Hacker {nama_hacker} menyerang port {target_port}")

# D. Practice

1. Exercise 1 - Refactoring (Medium)
Revisi kode practice01.py, gunakan F-Strings.
2. Exercise 2 - SOC Calculation (Challenge)
Buat skrip, minta input angka (Berapa banyak percobaan login gagal yang terdeteksi?). 
Simpan dalam variabel integer. 
Sistem terblokir dalam beberapa percobaan, hitung sisa percobaan.
Cetak dengan F-Strings

# Knowledge Check
1. Explain: Apa yang terjadi jika kode ini dijalankan tanpa diubah menjadi int()?

gagal_hari_ini = input("Login gagal: ") # user mengetik angka 3
total_gagal = gagal_hari_ini * 5
print(total_gagal)

Operasi akan berjalan namun hasilnya tidak akan sesuai harapan. Dengan kode seperti itu akan menghasilkan perkalian antara string 3 dan angka 5 yang akan menghasilkan "33333"/string 3 5x

2. Predict: Apa output dari perintah ini di Python: print(type("100")) dan print(type(100))? (Silakan coba di terminalmu jika ragu).

Saya tebak, "100" akan menghasilkan string dan 100 akan menghasilkan integer, karena type akan memunculkan tipe dari data (tebakan saja)
