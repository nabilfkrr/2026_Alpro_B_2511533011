total_belanja_3011 = float(input("Masukkan total belanja (Rp) : "))

input_member_3011 = input("Apakah anda memiliki member? (y/t) : ").strip().lower()
is_member_3011 = input_member_3011 in ["y", "ya"]

input_promo_3011 = input("Apakah kode promo anda valid? (y/t) : ").strip().lower()
kode_promo_valid_3011 = input_promo_3011 in ["y", "ya"]

total_diskon_persen_3011 = 0

if total_belanja_3011 > 1000000:
    total_diskon_persen_3011 += 10

if is_member_3011:
    total_diskon_persen_3011 += 5

if kode_promo_valid_3011 :
    total_diskon_persen_3011 += 15

nominal_diskon_3011 = total_belanja_3011 * (total_diskon_persen_3011 / 100)
total_bayar_3011 = total_belanja_3011 - nominal_diskon_3011
print ("\n-- Rincian Pembayaran --")
print (f"total Diskon : {total_diskon_persen_3011} %  (Rp {nominal_diskon_3011:,.0f})")
print (f"total Bayar : Rp {total_bayar_3011:,.0f}")

print (f"Total diskon yang anda dapatkan : {total_diskon_persen_3011}%")