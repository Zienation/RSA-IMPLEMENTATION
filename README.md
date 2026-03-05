# RSA Cryptography: Implementation From Scratch (Python)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Topic](https://img.shields.io/badge/Topic-Cryptography-green.svg)

Proyek ini adalah implementasi algoritma **RSA (Rivest-Shamir-Adleman)** menggunakan bahasa pemrograman Python tanpa menggunakan library kriptografi eksternal. Fokus utama proyek ini adalah mendemonstrasikan logika matematika di balik keamanan kunci asimetris.

---

## 📌 Pengantar RSA
**RSA** adalah algoritma kriptografi kunci publik yang paling banyak digunakan di dunia. Keamanan RSA didasarkan pada tingkat kesulitan dalam memfaktorkan perkalian dua bilangan prima besar.

Algoritma ini menggunakan sepasang kunci:

1. **Public Key** → digunakan untuk **enkripsi** dan boleh dibagikan.
2. **Private Key** → digunakan untuk **dekripsi** dan harus dijaga kerahasiaannya.

RSA banyak digunakan pada berbagai sistem keamanan digital seperti:

- HTTPS
- SSL/TLS
- Digital Signature
- Secure Email

---

# 🛠️ Langkah-Langkah Menjalankan Kode

1. **Pastikan Python Terinstal**

Cek versi Python dengan:

```bash
python --version
```

atau

```bash
python3 --version
```

2. **Download File**

Simpan kode Python dengan nama:

```
rsa_demo.py
```

3. **Buka Terminal / Command Prompt**

Masuk ke folder tempat file disimpan.

4. **Jalankan Program**

```bash
python rsa_demo.py
```

5. **Masukkan Pesan**

Program akan meminta input pesan yang ingin dienkripsi.

6. **Program Akan Menampilkan**

- proses pembangkitan kunci
- proses enkripsi
- proses dekripsi

---

# 🔑 Proses Pembangkitan Kunci RSA

Langkah pertama dalam RSA adalah menghasilkan **public key** dan **private key**.

### 1. Menentukan dua bilangan prima

Pada program ini digunakan:

```
p = 61
q = 53
```

### 2. Menghitung modulus

```
n = p × q
```

```
n = 61 × 53 = 3233
```

### 3. Menghitung Euler Totient

```
φ(n) = (p − 1)(q − 1)
```

```
φ(n) = 60 × 52 = 3120
```

### 4. Menentukan Public Key (e)

Bilangan **e** harus memenuhi:

```
1 < e < φ(n)
gcd(e, φ(n)) = 1
```

Dalam program digunakan:

```
e = 17
```

### 5. Menghitung Private Key (d)

Nilai **d** dihitung menggunakan **Extended Euclidean Algorithm**

```
d ≡ e⁻¹ mod φ(n)
```

Hasilnya:

```
Public Key  = (17, 3233)
Private Key = (2753, 3233)
```

---

# 🔐 Proses Enkripsi

Setelah public key tersedia, pesan dapat dienkripsi.

### Langkah-langkah

1. Setiap karakter diubah menjadi **ASCII**

Contoh:

```
H → 72
```

2. Menggunakan rumus RSA:

```
c = m^e mod n
```

Dimana:

```
m = plaintext
e = public key
n = modulus
c = ciphertext
```

3. Hasilnya berupa **angka ciphertext**

Contoh:

```
Ciphertext = [3000, 28, 2726, ...]
```

Program melakukan proses ini **untuk setiap karakter**.

---

# 🔓 Proses Dekripsi

Dekripsi dilakukan menggunakan **private key (d)**.

Rumus yang digunakan:

```
m = c^d mod n
```

Langkahnya:

1. Setiap angka ciphertext dipangkatkan dengan **d**
2. Hasilnya dikembalikan menjadi **ASCII**
3. ASCII diubah kembali menjadi **karakter**

Contoh:

```
3000 → 72 → H
```

Sehingga pesan asli dapat dikembalikan.

---

# ⚙️ Fungsi Matematika yang Digunakan

Program ini mengimplementasikan fungsi matematika sendiri tanpa library eksternal.

### 1️⃣ GCD (Greatest Common Divisor)

Digunakan untuk memastikan bahwa:

```
gcd(e, φ(n)) = 1
```

### 2️⃣ Modular Inverse

Digunakan untuk mencari **private key (d)** menggunakan **Extended Euclidean Algorithm**.

### 3️⃣ Modular Exponentiation

Digunakan untuk menghitung:

```
(base^exp) mod n
```

secara efisien menggunakan metode **Fast Modular Exponentiation**.

---

# 📊 Alur Proses RSA

```
Plaintext
    ↓
Konversi ke ASCII
    ↓
Enkripsi (m^e mod n)
    ↓
Ciphertext
    ↓
Dekripsi (c^d mod n)
    ↓
ASCII
    ↓
Plaintext kembali
```

---

# 💻 Contoh Output Program

```
=== TUGAS KRIPTOGRAFI: RSA FROM SCRATCH ===

Masukkan pesan Anda: HALO

--- PEMBANGKITAN KUNCI ---
p = 61
q = 53
n = 3233
phi = 3120

Public Key  = (17, 3233)
Private Key = (2753, 3233)

--- ENKRIPSI ---
'H' → 3000
'A' → 2790
'L' → 1307
'O' → 1313

Ciphertext: [3000, 2790, 1307, 1313]

--- DEKRIPSI ---
3000 → H
2790 → A
1307 → L
1313 → O

Pesan berhasil dikembalikan: HALO
```

---

# ✅ Kelebihan RSA

- Menggunakan **sistem kunci publik dan privat**
- Sangat aman jika menggunakan bilangan prima besar
- Banyak digunakan dalam sistem keamanan modern
- Mendukung **digital signature**

---

# ❌ Kekurangan RSA

- Proses komputasi relatif **lebih lambat**
- Membutuhkan **bilangan prima sangat besar**
- Tidak efisien untuk mengenkripsi data berukuran besar
- Biasanya dikombinasikan dengan **kriptografi simetris**

---

# 📚 Kesimpulan

Proyek ini menunjukkan implementasi sederhana algoritma **RSA Cryptography From Scratch** menggunakan Python tanpa library kriptografi.

Tujuan utama proyek ini adalah untuk memahami konsep dasar:

- Pembangkitan kunci RSA
- Enkripsi pesan
- Dekripsi pesan
- Operasi matematika modular

Implementasi ini cocok untuk **pembelajaran kriptografi dasar** dan pemahaman konsep keamanan kunci publik.

---
