# --- FUNGSI MATEMATIKA DASAR (IMPLEMENTASI SENDIRI) ---

def hitung_gcd(a, b):
    """Mencari Faktor Persekutuan Terbesar (FPB)"""
    while b != 0:
        a, b = b, a % b
    return a

def cari_modular_inverse(e, phi):
    """Mencari nilai d menggunakan Extended Euclidean Algorithm"""
    d_lama, d_baru = 0, 1
    phi_lama, phi_baru = phi, e
    
    while phi_baru != 0:
        quotient = phi_lama // phi_baru
        phi_lama, phi_baru = phi_baru, phi_lama - quotient * phi_baru
        d_lama, d_baru = d_baru, d_lama - quotient * d_baru
    
    if d_lama < 0:
        d_lama = d_lama + phi
    return d_lama

def pangkat_modular(base, exp, mod):
    """Menghitung (base^exp) % mod secara efisien (Manual Power)"""
    res = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return res

# --- PROSES UTAMA RSA ---

def jalankan_demo_rsa():
    print("=== TUGAS KRIPTOGRAFI: RSA FROM SCRATCH (NO LIBRARIES) ===")
    
    # 1. Input Pesan
    teks_asli = input("1. Masukkan pesan Anda: ")
    
    # 2. Persiapan Bilangan Prima (p dan q)
    # Kita tentukan manual sesuai standar tugas agar tidak perlu library random
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # 3. Menentukan Kunci Publik (e) dan Kunci Privat (d)
    e = 17 # Bilangan prima kecil yang umum digunakan untuk RSA
    d = cari_modular_inverse(e, phi)
    
    print("\n--- TAHAP 1: PEMBANGKITAN KUNCI ---")
    print(f"   > Bilangan Prima: p={p}, q={q}")
    print(f"   > Modulus (n = p*q): {n}")
    print(f"   > Totient (phi): {phi}")
    print(f"   > Public Key (e, n): ({e}, {n})")
    print(f"   > Private Key (d, n): ({d}, {n})")
    
    input("\n[Tekan Enter untuk Proses Enkripsi...]")
    
    # 4. Proses Enkripsi
    # Mengubah karakter -> ASCII -> (ASCII^e % n)
    list_cipher = []
    print("\nProses Enkripsi (Karakter per Karakter):")
    for karakter in teks_asli:
        m = ord(karakter)
        c = pangkat_modular(m, e, n)
        list_cipher.append(c)
        print(f"   - '{karakter}' (ASCII {m}) dipangkatkan {e} mod {n} = {c}")
    
    print(f"\n> Hasil Akhir Ciphertext: {list_cipher}")
    
    input("\n[Tekan Enter untuk Proses Dekripsi...]")
    
    # 5. Proses Dekripsi
    # Mengubah (Cipher^d % n) -> ASCII -> Karakter
    teks_hasil_dekripsi = ""
    print("\nProses Dekripsi (Mengembalikan ke Teks Asli):")
    for c in list_cipher:
        m_asli = pangkat_modular(c, d, n)
        huruf = chr(m_asli)
        teks_hasil_dekripsi += huruf
        print(f"   - Angka {c} dipangkatkan {d} mod {n} = {m_asli} (Karakter '{huruf}')")
    
    print(f"\n> Pesan Berhasil Dikembalikan: {teks_hasil_dekripsi}")
    print("\n=== DEMO SELESAI ===")

if __name__ == "__main__":
    jalankan_demo_rsa()