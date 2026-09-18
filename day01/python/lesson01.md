## Python Environment & Interactive Input

## A. Learning Objectives

1. Memverifikasi instalasi Python di OS Archlinux.
2. Menulis dan menjalankan script Python melalui terminal menggunakan Neovim.
3. Membuat program menjadi interaktif dengan meminta input dari user.

## B. Theory

1. Python Environment di Arch
Jika HTML dibaca browser, maka Python butuh program interpreter. Ia bertugas membaca kode, dan menerjemahkan agar bisa dieksekusi komputer.
2. Fungsi input()
Di pre-learn, kita menggunakan nama_user = "Budi" (variabel data statis). Jika kita ingin interaktif, maka fungsi input() bisa digunakan untuk mengehentikan program (sementara) dan menunggu user menginputkan sesuatu lalu disimpan menjadi variabel.

Example:

# Meminta user memasukkan data
target_ip = input("Masukkan IP Address yang ingin dicek: ")

# Menampilkan data yang dimasukkan
print("Memulai pemindaian pada IP: " + target_ip)

3. Code Explanation
a. target_ip adalah variabel kosong yang akan diisi input user.
b. input("blabla") adalah fungsi yang digunakan untuk meminta input user.
c. print("blabla") adalah fungsi yang digunakan untuk mencetak ke layar.
d. # adalah Comment (komentar), digunakan sebagai catatan dan tidak akan dieksekusi.

## C. Practice

# 1. Exercise 1 (Environment Check - Easy)
1. Buka terminal.
2. python --version.
3. Catat output. (Python 3.14.7)

# 2. Exercise 2 (Script Pertama - Medium)
1. Buat file baru (.py)
2. Isi dengan kodingan (Harus ada variabel minimal 3, input dan print)
3. Simpan dan jalankan dengan python/python3

# 3. Exercise 3 (Challenge)
Modifikasi file yang sudah dibuat, lebih variatif.

## D. Knowledge Check

1. Explain: Mengapa kita membutuhkan variabel saat menggunakan fungsi input()? Agar inputan dari user bisa dipakai untuk fungsi yang lain.
Apa yang terjadi jika kita hanya menulis input() tanpa memasukkan ke variabel? Bisa, namun kita tidak bisa menggunakan inputan dari user untuk apapun. Bisa kita temukan dikasus video game (Press button to continue)
2. Predict: Pada Arch, apa yang terjadi jika salah mengetik huruf besar/kecil pada perintah Print("halo") (menggunakan 'P' besar)? Print isn't defined
