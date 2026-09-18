print("=== SISTEM TRANSAKSI TOKO ===")

# INPUT
nama_3011           = input("\nMasukkan Nama Pelanggan : ")
status_3011         = input("Masukkan Status Pelanggan (member/nonmember) : ")
totalBelanja_3011   = int(input("Masukkan Total Belanja : "))
jumlahBarang_3011   = int(input("Masukkan Jumlah Barang : "))
kodePromo_3011      = input("Masukkan Kode Promo : ").strip().upper()

# KONSTANTA
minBelanja_3011     = 200000
minBarang_3011      = 3
diskonMember_3011   = 10

daftarPromo_3011    = ["MERIAH10", "MERIAH20", "GRATISONGKIR"]
diskonPromo_3011    = {"MERIAH10": 10, "MERIAH20": 20, "GRATISONGKIR": 0}

# OPERATOR PERBANDINGAN
syaratBelanja_3011  = totalBelanja_3011 >= minBelanja_3011
syaratBarang_3011   = jumlahBarang_3011 >= minBarang_3011
isMember_3011       = status_3011.lower() == "member"

# OPERATOR KEANGGOTAAN
promoTersedia_3011  = kodePromo_3011 in daftarPromo_3011
promoTidakAda_3011  = kodePromo_3011 not in daftarPromo_3011

# OPERATOR LOGIKA
dapatDiskon_3011    = isMember_3011 and syaratBelanja_3011
dapatPromo_3011     = promoTersedia_3011 and (syaratBelanja_3011 or syaratBarang_3011)
cekNot_3011         = not promoTidakAda_3011

# OPERATOR ARITMATIKA
persenDiskon_3011   = 0
if dapatPromo_3011:
    persenDiskon_3011 = diskonPromo_3011[kodePromo_3011]
elif dapatDiskon_3011:
    persenDiskon_3011 = diskonMember_3011

besarDiskon_3011    = totalBelanja_3011 * persenDiskon_3011 // 100
totalBayar_3011     = totalBelanja_3011 - besarDiskon_3011
rataRata_3011       = totalBelanja_3011 // jumlahBarang_3011
sisaBelanja_3011    = totalBelanja_3011 % jumlahBarang_3011
point_3011          = totalBelanja_3011 // 10000

# OPERATOR PENUGASAN
ongkir_3011         = 15000
if kodePromo_3011 == "GRATISONGKIR" and promoTersedia_3011:
    ongkir_3011     -= ongkir_3011     
totalBayar_3011     += ongkir_3011     

# OPERATOR IDENTITAS
refStatus_3011      = status_3011           
kopiStatus_3011     = status_3011[:]       
identitasSama_3011  = refStatus_3011 is status_3011
identitasBeda_3011  = kopiStatus_3011 is not status_3011
nilaiSama_3011      = kopiStatus_3011 == status_3011

# OPERATOR BITWISE

bitMember_3011      = 0b0001 if isMember_3011      else 0b0000
bitBelanja_3011     = 0b0010 if syaratBelanja_3011 else 0b0000
bitBarang_3011      = 0b0100 if syaratBarang_3011  else 0b0000
bitPromo_3011       = 0b1000 if promoTersedia_3011 else 0b0000

kodeTranasksi_3011  = bitMember_3011 | bitBelanja_3011 | bitBarang_3011 | bitPromo_3011  
cekMemberBit_3011   = kodeTranasksi_3011 & 0b0001  
cekPromoBit_3011    = kodeTranasksi_3011 & 0b1000  
kodeReferensi_3011  = 0b1011
bedaStatus_3011     = kodeTranasksi_3011 ^ kodeReferensi_3011   
shiftKiri_3011      = kodeTranasksi_3011 << 1                   

akseMember_3011     = bool(kodeTranasksi_3011 & 0b0001)
aksePromo_3011      = bool(kodeTranasksi_3011 & 0b1000)
akseFreeShip_3011   = kodePromo_3011 == "GRATISONGKIR" and promoTersedia_3011

print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan   : {nama_3011}")
print(f"Status Pelanggan : {status_3011}")
print(f"Total Belanja    : Rp{totalBelanja_3011:,}")
print(f"Jumlah Barang    : {jumlahBarang_3011}")
print(f"Kode Promo       : {kodePromo_3011}")

 
print("\n=== HASIL VALIDASI ===")
  
print(f"Belanja >= Rp200.000       : {syaratBelanja_3011}")
print(f"Jumlah Barang >= 3         : {syaratBarang_3011}")
print(f"Status Member              : {isMember_3011}")
print(f"Kode Promo Tersedia        : {promoTersedia_3011}")
print(f"Mendapatkan Diskon Member  : {dapatDiskon_3011}")
print(f"Mendapatkan Promo          : {dapatPromo_3011}")

 
print("\n=== HASIL PERHITUNGAN ===")
  
print(f"Persentase Diskon          : {persenDiskon_3011}%")
print(f"Besarnya Diskon            : Rp{besarDiskon_3011:,}")
print(f"Ongkos Kirim               : Rp{ongkir_3011:,}")
print(f"Total Pembayaran           : Rp{totalBayar_3011:,}")
print(f"Rata-rata Harga Barang     : Rp{rataRata_3011:,}")
print(f"Sisa Pembagian (%)         : Rp{sisaBelanja_3011:,}")
print(f"Poin Pelanggan             : {point_3011} poin")

 
print("\n=== HAK AKSES PELANGGAN ===")
  
print(f"Kode Hak Akses (desimal)   : {kodeTranasksi_3011}")
print(f"Kode Hak Akses (biner)     : {format(kodeTranasksi_3011, '04b')}")
print(f"Member Access              : {akseMember_3011}")
print(f"Promo Access               : {aksePromo_3011}")
print(f"Free Shipping Access       : {akseFreeShip_3011}")

 
print("\n=== OPERATOR IDENTITAS ===")
  
print(f"refStatus is status_3011       : {identitasSama_3011}")
print(f"kopiStatus is not status_3011  : {identitasBeda_3011}")
print(f"kopiStatus == status_3011      : {nilaiSama_3011}")
print("-> is  : membandingkan IDENTITAS objek di memori")
print("-> ==  : membandingkan NILAI/ISI objek")

 
print("\n=== OPERASI BITWISE ===")
  
print("\n=== Kode Status Transaksi ===")
print(f"  0001 | 0010 | 0100 | 1000")
print(f"  Kode Biner   : {format(kodeTranasksi_3011, '04b')}")
print(f"  Kode Desimal : {kodeTranasksi_3011}")

print("\n=== Pemeriksaan Status ===")
print(f"  Cek Member : {format(kodeTranasksi_3011,'04b')} & 0001 = {format(cekMemberBit_3011,'04b')} ({cekMemberBit_3011})")
print(f"  Cek Promo  : {format(kodeTranasksi_3011,'04b')} & 1000 = {format(cekPromoBit_3011,'04b')} ({cekPromoBit_3011})")

print("\n=== Perbandingan Status ===")
print(f"  Kode Transaksi : {format(kodeTranasksi_3011,'04b')}")
print(f"  Kode Referensi : {format(kodeReferensi_3011,'04b')}")
print(f"  Hasil      : {format(bedaStatus_3011,'04b')} ({bedaStatus_3011})")

print("\n=== Shift ===")
print(f"  {format(kodeTranasksi_3011,'04b')} << 1")
print(f"  Hasil Biner   : {bin(shiftKiri_3011)[2:]}")
print(f"  Hasil Desimal : {shiftKiri_3011}")

 
print("=== SELESAI ===")
  
